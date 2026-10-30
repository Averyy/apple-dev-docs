# Supporting drag and drop through file promises

**Framework**: AppKit  
**Role**: Sample Code  
**Download**: [SupportingDragAndDropThroughFilePromises.zip](https://docs-assets.developer.apple.com/published/e4886157ddec/SupportingDragAndDropThroughFilePromises.zip)

Receive and provide file promises to support dragged app files and pasteboard operations.

**Availability**:
- macOS 27.0+
- Xcode 27.0+

## Overview

This sample code project is a meme generator that combines an image and text into a JPEG you can export. It accepts images from Mail, Safari, Photos, and other apps as either file URLs or file promises, and it provides a file promise when you drag the finished meme out to another app. Gesture recognizers handle selecting, editing, and moving text, and starting the drag that exports the meme.

Your app may need to support file promises because drag and drop uses an `NSPasteboard` that’s separate from the copy-and-paste clipboard. When the source app needs time to produce the file, as Photos does when it exports an image, it can put a file promise on that pasteboard instead of a file URL, so it doesn’t block the main thread. Unlike a URL, a file promise is read and written later, asynchronously, on a background queue.

## Support image import by accepting file promises

To accept file promises, such as dragged images from Safari or Mail, register the drag types that [NSFilePromiseReceiver](./nsfilepromisereceiver.md) provides. The sample registers them in `viewDidLoad` of its image canvas view controller:

```swift
view.registerForDraggedTypes(NSFilePromiseReceiver.readableDraggedTypes.map { NSPasteboard.PasteboardType($0) })
```

Handle file promises before file URLs, because a file promise generally represents the higher-quality image and takes precedence when a drop includes both. The sample receives the promised file on a background operation queue so the main thread stays responsive, and it shows a progress indicator in the image view subclass until the file arrives. The system calls the completion handler on that queue, so the sample hops back to the main actor before it updates the interface. When a drop contains a file promise, the sample receives it:

```swift
case let filePromiseReceiver as NSFilePromiseReceiver:
    self.prepareForUpdate()
    filePromiseReceiver.receivePromisedFiles(atDestination: self.destinationURL, options: [:],
                                             operationQueue: self.workQueue) { @Sendable (fileURL, error) in
        // The system calls this handler on `workQueue`, so hop back to the main actor.
        Task { @MainActor in
            if let error = error {
                self.handleError(error)
            } else {
                self.handleFile(at: fileURL)
            }
        }
    }
```

For apps that don’t provide file promises, the sample also handles file URLs, as shown below:

```swift
case let fileURL as URL:
    self.handleFile(at: fileURL)
```

## Support image export by providing file promises

To export the composite image in a format that other apps like Safari, Mail, and Finder can consume, the sample puts an [NSFilePromiseProvider](./nsfilepromiseprovider.md) on the dragging pasteboard and conforms to [NSFilePromiseProviderDelegate](./nsfilepromiseproviderdelegate.md) by implementing three methods: [filePromiseProvider(_:fileNameForType:)](./nsfilepromiseproviderdelegate/filepromiseprovider%28_,filenamefortype%29.md), [operationQueue(for:)](./nsfilepromiseproviderdelegate/operationqueue%28for%29.md), and [filePromiseProvider(_:writePromiseTo:completionHandler:)](./nsfilepromiseproviderdelegate/filepromiseprovider%28_,writepromiseto,completionhandler%29.md). The system can call these methods from a background queue, not only from the main actor, so the sample marks each of them `nonisolated`.

The `filePromiseProvider(_:fileNameForType:)` method provides the file name. Your app can take the `fileType` parameter into account, but the sample returns a hard-coded string for simplicity, shown below:

```swift
nonisolated func filePromiseProvider(_ filePromiseProvider: NSFilePromiseProvider, fileNameForType fileType: String) -> String {
    let droppedFileName = NSLocalizedString("DropFileTitle", comment: "")
    return droppedFileName + ".jpg"
}
```

The [`operationQueue(for:)`](./nsfilepromiseproviderdelegate/operationqueue%28for%29.md) method is optional. It tells the system which queue to use when it writes the file. Without it, the system uses the main queue, which blocks the app’s UI while writing large files. To avoid that, the sample provides a background queue:

```swift
nonisolated func operationQueue(for filePromiseProvider: NSFilePromiseProvider) -> OperationQueue {
    return workQueue
}
```

The `filePromiseProvider(_:writePromiseTo:completionHandler:)` method writes the file to disk when the system fulfills the file promise. The system calls it on the queue from the previous method. Convert your app’s content to a file format that other apps are likely to understand, as this sample does with JPEG. The sample writes the JPEG data for a snapshot of the canvas to the URL the system provides, and reports any failure through the completion handler, shown here:

```swift
nonisolated func filePromiseProvider(_ filePromiseProvider: NSFilePromiseProvider,
                                     writePromiseTo url: URL,
                                     completionHandler: @escaping (Error?) -> Void) {
    do {
        guard let snapshot = filePromiseProvider.userInfo as? ImageCanvas.SnapshotItem,
              let jpegData = snapshot.jpegRepresentation else {
            throw RuntimeError.unavailableSnapshot
        }
        try jpegData.write(to: url)
        completionHandler(nil)
    } catch {
        completionHandler(error)
    }
}
```

## Recognize clicks and drags with gesture recognizers

The image canvas uses gesture recognizers to select, edit, and move text, and to drag the composite image out of the window. Each recognizer has a target and an action, and the canvas is the [NSGestureRecognizerDelegate](./nsgesturerecognizerdelegate.md) for all of them. The recognizers work the same way with a pointer or with direct touches on a Mac with a touch display.

The sample creates two [NSClickGestureRecognizer](./nsclickgesturerecognizer.md) instances, setting [numberOfClicksRequired](./nsclickgesturerecognizer/numberofclicksrequired.md) to `2` on the instance for double clicks, as shown below:

```swift
private lazy var singleClickRecognizer = NSClickGestureRecognizer(target: self, action: #selector(handleSingleClick(_:)))
private lazy var doubleClickRecognizer: NSClickGestureRecognizer = {
    let recognizer = NSClickGestureRecognizer(target: self, action: #selector(handleDoubleClick(_:)))
    recognizer.numberOfClicksRequired = 2
    return recognizer
}()
```

The sample also creates an [NSPanGestureRecognizer](./nspangesturerecognizer.md), which recognizes a press followed by movement, such as dragging a text box, and adds all three recognizers to the canvas, as shown below:

```swift
private func configureGestureRecognizers() {
    let panRecognizer = NSPanGestureRecognizer(target: self, action: #selector(handlePan(_:)))

    for recognizer in [singleClickRecognizer, doubleClickRecognizer, panRecognizer] {
        recognizer.delegate = self
        addGestureRecognizer(recognizer)
    }
}
```

A single click selects a text field, and a double click starts editing it. Because both gestures begin with a click, the canvas implements [gestureRecognizer(_:shouldRequireFailureOf:)](./nsgesturerecognizerdelegate/gesturerecognizer%28_,shouldrequirefailureof%29.md) so the single-click recognizer waits for the double-click recognizer to fail, and a double click doesn’t also select the text field, as shown below:

```swift
func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
                       shouldRequireFailureOf otherGestureRecognizer: NSGestureRecognizer) -> Bool {
    return gestureRecognizer === singleClickRecognizer && otherGestureRecognizer === doubleClickRecognizer
}
```

Clicks and drags in the text field’s field editor should move the insertion point and select text. The canvas implements [gestureRecognizerShouldBegin(_:)](./nsgesturerecognizerdelegate/gesturerecognizershouldbegin%28_%29.md) to keep the recognizers from beginning while a person is editing text, as shown below:

```swift
func gestureRecognizerShouldBegin(_ gestureRecognizer: NSGestureRecognizer) -> Bool {
    let hitView = subviewHit(at: gestureRecognizer.location(in: self))
    return hitView == nil || hitView !== window?.fieldEditor(false, for: nil)
}
```

On the canvas, dragging does one of two things: it moves a text box, or it exports the meme. The [`NSPanGestureRecognizer`](./nspangesturerecognizer.md) handles both, and the sample’s action method, `handlePan(_:)`, checks the recognizer’s `state` to tell when a pan begins or changes, and when the system cancels it.

When a pan begins on a text box, the method moves the text box to follow the pointer and keeps it inside the image. If the system cancels the gesture, the method returns the text box to where it started. When a pan begins anywhere else on the canvas while an image is loaded, the method starts a dragging session that exports the composite image as a file promise, as shown below:

```swift
@objc
private func handlePan(_ sender: NSPanGestureRecognizer) {
    switch sender.state {
    case .began:
        if let textField = hitTextField(at: sender.location(in: self)) {
            select(textField)
            draggedTextField = textField
            draggedTextFieldStartOrigin = textField.frame.origin
        } else if image != nil {
            select(nil)
            beginImageDraggingSession(for: sender)
        }
    case .changed:
        guard let textField = draggedTextField else { return }
        let translation = sender.translation(in: self)
        let movedOrigin = CGPoint(x: draggedTextFieldStartOrigin.x + translation.x,
                                  y: draggedTextFieldStartOrigin.y + translation.y)
        textField.frame = constrainRectToBounds(CGRect(origin: movedOrigin, size: textField.frame.size))
    case .cancelled:
        // Move the text field back to its position at the start of the pan.
        if let textField = draggedTextField {
            textField.frame.origin = draggedTextFieldStartOrigin
        }
        draggedTextField = nil
    case .ended, .failed:
        draggedTextField = nil
    default:
        break
    }
}
```

## See Also

### File Promises
- [Supporting Table View Drag and Drop Through File Promises](./supporting-table-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [Supporting Collection View Drag and Drop Through File Promises](./supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [class NSFilePromiseProvider](./nsfilepromiseprovider.md)
  An object that provides a promise for the pasteboard.
- [protocol NSFilePromiseProviderDelegate](./nsfilepromiseproviderdelegate.md)
  A set of methods that provides the name of the promised file and writes the file to the destination directory when the file promise is fulfilled.
- [class NSFilePromiseReceiver](./nsfilepromisereceiver.md)
  An object that receives a file promise from the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/supporting-drag-and-drop-through-file-promises)*