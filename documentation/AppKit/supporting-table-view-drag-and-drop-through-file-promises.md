# Supporting Table View Drag and Drop Through File Promises

**Framework**: AppKit

Share data between macOS apps during drag and drop by using an item provider.

**Availability**:
- macOS 10.13+
- Xcode 13.1+

#### Overview

A file promise is a possible future file sent by an app of a specified type. When working with drag and drop, use file promises to indicate intent for a future drag operation. The future drag operation promises the delivery of the file at drop time. This avoids loading or performing any actions on the file until the promise completes. Use the [`NSFilePromiseProvider`](nsfilepromiseprovider.md) class when creating file promises. Use the [`NSFilePromiseReceiver`](nsfilepromisereceiver.md) to receive file promises.

Implement drag and drop with an [`NSTableView`](nstableview.md) by using a dragging pasteboard. When a drag starts, you adopt the [`NSPasteboardWriting`](nspasteboardwriting.md) protocol to write data to the [`NSPasteboard`](nspasteboard.md). When a drag occurs, you determine the valid drop target. When the drag ends, you read the drag data from the [`NSPasteboard`](nspasteboard.md). Adopt [`NSTableViewDataSource`](nstableviewdatasource.md) to handle with these drag operations.

##### Display Files to Drag and Drop

This sample code project displays a list of image files from the Pictures folder found in the user’s home directory. It allows those pictures to be dragged within the table view, to be reordered, and dragged out to be copied to other apps. Pictures are also dragged in from other apps like Finder, Mail, Safari, and Photos.

The sample shows how to support both `URL` and file promises drags when accepting images from Mail, Safari, Photos, and other apps that support drag and drop. It also demonstrates how to provide file promises to other apps.

##### Test Drag and Drop By Creating or Receiving File Promises

To see this sample in action, build and run the project, then drag an image from another app or location, such as Finder, Mail, Photos or Safari, into the app’s window. Dragging the image into the window imports it into a form that the sample app can parse and consume. There are multiple ways to drag and drop image files to and from the sample app. The way a user drags a file determines how files are promised to and from the destination. If the user drags an image file from the app to the Finder, the Finder uses the `NSFilePromiseProvider` to make a copy. If the user drags a photo from Photos, the sample app uses `NSFilePromiseReceiver` to receive a copy.

Below are the various ways a drag and drop can occur that will involve either a `NSFilePromiseProvider` or a `NSFilePromiseReceiver`.

Drag sent by `NSFilePromiseProvider`:

- Drag an image out to the Finder.
- Drag an image out to Mail.
- Drag an image out to Photos.

Drag received by `NSFilePromiseReceiver`:

- Drag an image in from Safari (from a website with a jpg, png, etc).
- Drag an image in from Photos.
- Drag multiple images in from Photos — helps test receiving multiple file promises.
- Drag in a very large photo from Photos app — helps test the progress UI when receiving large photos.

In addition, a drag and drop involves just the image file’s URL, without a file promise:

- Drag an image from Finder.
- Drag an image from a Mail attachment.

This sample app also supports drag and drop of images from within the table view that don’t involve a URL. In this case photos are re-ordered using the row number of the photo as the drag reference.

##### Support Image Import By Accepting File Promises

When setting up the table view to support drag and drop, register drag pasteboard types to the table view. This sample registers three pasteboard types. `NSFilePromiseReceiver` provides the first. This type allows the table view to accept file promises that handle dragged images from apps like Safari or Photos. The second, `.fileURL`, accepts drags as file URLs. The third type is `itemDragType`, a custom pasteboard type that accepts table view cell rows to drag within the table view.

The sample registers these pasteboard types in the view controller’s `viewDidLoad` function:

```swift
tableView.registerForDraggedTypes(
    NSFilePromiseReceiver.readableDraggedTypes.map { NSPasteboard.PasteboardType($0) })

tableView.registerForDraggedTypes([
    .fileURL, // Accept dragging of image file URLs from other apps.
    .rowDragType]) // Intra drag of row items numbers within the table.
```

Handle file promises before handling file URLs, because the file promise generally represents the higher-quality image and should take precedence when both types are supported. Provide a background operation queue so the read-and-write operation doesn’t block the main thread. Until the file promise is fulfilled, this app shows a spinning indicator to give the user immediate feedback that the app is processing the drop. Continue to handle file URLs, in case the app from which the user drags the image doesn’t provide file promises.

```swift
func handlePromisedDrops(draggingInfo: NSDraggingInfo, toRow: Int) -> Bool {
    var handled = false
    if let promises = draggingInfo.draggingPasteboard.readObjects(forClasses: [NSFilePromiseReceiver.self], options: nil) {
        if !promises.isEmpty {
            // We have incoming drag item(s) that are file promises.

            // At the start of insertion(s), clear the current table view selection.
            tableView.deselectAll(self)
            
            for promise in promises {
                if let promiseReceiver = promise as? NSFilePromiseReceiver {
                    // Show the progress indicator as we start receiving this promised file.
                    progressIndicator.isHidden = false
                    progressIndicator.startAnimation(self)
                    
                    // Ask our file promise receiver to fulfull on their promise.
                    promiseReceiver.receivePromisedFiles(atDestination: destinationURL,
                                                         options: [:],
                                                         operationQueue: filePromiseQueue) { (fileURL, error) in
                        /** Finished copying the promised file.
                            Back on the main thread, insert the newly created image file into the table view.
                        */
                        OperationQueue.main.addOperation {
                            if error != nil {
                                self.reportURLError(fileURL, error: error!)
                            } else {
                                _ = self.insertURL(fileURL, toRow: toRow)

                                /** Select the newly inserted photo,
                                    extend the selection so to accumulate multiple selected photos.
                                */
                                let indexSet = IndexSet(integer: toRow)
                                self.tableView.selectRowIndexes(indexSet, byExtendingSelection: true)
                            }
                            // Stop the progress indicator as we are done receiving this promised file.
                            self.progressIndicator.isHidden = true
                            self.progressIndicator.stopAnimation(self)
                        }
                    }
                }
            }
            handled = true
        }
    }
    return handled
}
```

##### Support Image Export By Providing File Promises

To write images from the table view, the sample app creates formats that other apps like Safari, Mail, and Finder can consume, write an `NSFilePromiseProvider` instance to the dragging pasteboard, and conform to [`NSFilePromiseProviderDelegate`](nsfilepromiseproviderdelegate.md) by implementing three delegate functions.

Use the first function to provide the title of the file to be promised. This sample uses the last component of the photo item’s `fileURL` to determine the promised file name.

```swift
func filePromiseProvider(_ filePromiseProvider: NSFilePromiseProvider, fileNameForType fileType: String) -> String {
    // Return the photoItem's URL file name.
    let photoItem = photoFromFilePromiserProvider(filePromiseProvider: filePromiseProvider)
    return (photoItem?.fileURL.lastPathComponent)!
}
```

Provide a background operation queue in [`operationQueue(for:)`](nsfilepromiseproviderdelegate/operationqueue(for:).md), so the file write happens without blocking the app’s UI. This function is optional, but defaulting to the main queue will block the app’s UI for writing large files to disk. When possible, provide a background queue.

```swift
func operationQueue(for filePromiseProvider: NSFilePromiseProvider) -> OperationQueue {
    return filePromiseQueue
}
```

The third delegate function performs the actual writing of the file to disk when it is time to fulfill the file promise. Add custom logic necessary to transform the image from the app into a file format that other apps are likely to understand, such as the image formats that this sample uses.

```swift
func filePromiseProvider(_ filePromiseProvider: NSFilePromiseProvider,
                         writePromiseTo url: URL,
                         completionHandler: @escaping (Error?) -> Void) {
    do {
        if let photoItem = photoFromFilePromiserProvider(filePromiseProvider: filePromiseProvider) {
            /** Copy the file to the location provided to us. We always do a copy, not a move.
                It's important you call the completion handler.
            */
            try FileManager.default.copyItem(at: photoItem.fileURL, to: url)
        }
        completionHandler(nil)
    } catch let error {
        OperationQueue.main.addOperation {
            self.presentError(error, modalFor: self.view.window!,
                              delegate: nil, didPresent: nil, contextInfo: nil)
        }
        completionHandler(error)
    }
}
```

Implement `NSTableViewDelegate` [`tableView(_:pasteboardWriterForRow:)`](nstableviewdatasource/tableview(_:pasteboardwriterforrow:).md) so the table view uses the file promise provider when the image files are dragged out. It returns an instance of [`NSPasteboardItem`](nspasteboarditem.md) or a custom object that implements the `NSPasteboardWriting` protocol.

```swift
func tableView(_ tableView: NSTableView, pasteboardWriterForRow row: Int) -> NSPasteboardWriting? {
    /** Return a custom NSFilePromiseProvider.
        Here we provide a custom provider, offering the row to the drag object, and it's URL.
    */
    var provider: FilePromiseProvider
    
    let photoItem = contentArray[row]
    let photoFileExtension = photoItem.fileURL.pathExtension

    if #available(macOS 11.0, *) {
        let typeIdentifier = UTType(filenameExtension: photoFileExtension)
        provider = FilePromiseProvider(fileType: typeIdentifier!.identifier, delegate: self)
    } else {
        let typeIdentifier =
              UTTypeCreatePreferredIdentifierForTag(kUTTagClassFilenameExtension, photoFileExtension as CFString, nil)
        provider = FilePromiseProvider(fileType: typeIdentifier!.takeRetainedValue() as String, delegate: self)
    }

    // Send over the row number and photo's url dictionary.
    provider.userInfo = [FilePromiseProvider.UserInfoKeys.rowNumberKey: row,
                         FilePromiseProvider.UserInfoKeys.urlKey: photoItem.fileURL as Any]
    return provider
}
```

Returning a non-nil value will make the table view cell draggable. To drag image files from the table view to other apps, the table view’s drag operation mask is set by the table view’s view controller to work outside the app using [`setDraggingSourceOperationMask(_:forLocal:)`](nstableview/setdraggingsourceoperationmask(_:forlocal:).md).

```swift
tableView.setDraggingSourceOperationMask(.copy, forLocal: false)
```

##### Validate the Table Drop

To allow the table view to determine a valid drop target, implement [`tableView(_:validateDrop:proposedRow:proposedDropOperation:)`](nstableviewdatasource/tableview(_:validatedrop:proposedrow:proposeddropoperation:).md). UIKit calls this delegate function when a drag is moved over the table view and before the dragging object is dropped by the user. Specify how to respond to a proposed drop operation, which will be either on or above a cell. In this sample, users can drop items between cells to insert them.

##### Accept the Drop Onto the Table

To allow the table view to accept the drop when the user releases the mouse button over it, implement this delegate function [`tableView(_:acceptDrop:row:dropOperation:)`](nstableviewdatasource/tableview(_:acceptdrop:row:dropoperation:).md).

```swift
func tableView(_ tableView: NSTableView,
               acceptDrop info: NSDraggingInfo,
               row: Int,
               dropOperation: NSTableView.DropOperation) -> Bool {
    // Check where the dragged items are coming.
    if dragSourceIsFromOurTable(draggingInfo: info) {
        /** Drag source came from our own table view.
            Move each dragged photo item to their new place.
        */
        dropInternalPhotos(tableView, draggingInfo: info, toRow: row)
    } else {
        /** The drop source is from another app (Finder, Mail, Safari, etc.) and there may be more than one file.
            Drop each dragged image file to their new place.
        */
        dropExternalPhotos(tableView, draggingInfo: info, toRow: row)
    }
    return true
}
```

This function handles the data from the dragging pasteboard after the user drops the image onto the table view.

##### Drag and Drop to Reorder Table Rows

To reorder image files within the table view, the sample app defines and registers a custom pasteboard type:

```swift
extension NSPasteboard.PasteboardType {
    static let rowDragType = NSPasteboard.PasteboardType("com.mycompany.mydragdrop")
}
```

When using that custom pasteboard type, the user then drags and drops images within the table view to be reordered:

```swift
func dropInternalPhotos(_ tableView: NSTableView, draggingInfo: NSDraggingInfo, toRow: Int) {
    var indexesToMove = IndexSet()
    
    draggingInfo.enumerateDraggingItems(
        options: NSDraggingItemEnumerationOptions.concurrent,
        for: tableView,
        classes: [NSPasteboardItem.self],
        searchOptions: [:],
        using: {(draggingItem, idx, stop) in
            if  let pasteboardItem = draggingItem.item as? NSPasteboardItem,
                let photoRow = pasteboardItem.propertyList(forType: .rowDragType) as? Int {
                    indexesToMove.insert(photoRow)
                }
        })
            
    // Move/drop the photos in their correct place using their indexes.
    moveObjectsFromIndexes(indexesToMove, toIndex: toRow)
    
    // Set the selected rows to those that were just moved.
    let rowsMovedDown = rowsMovedDownward(toRow, indexSet: indexesToMove)
    let selectionRange = toRow - rowsMovedDown..<toRow - rowsMovedDown + indexesToMove.count
    let indexSet = IndexSet(integersIn: selectionRange)
    tableView.selectRowIndexes(indexSet, byExtendingSelection: false)
}
```

## See Also

- [Supporting Drag and Drop Through File Promises](supporting-drag-and-drop-through-file-promises.md)
  Receive and provide file promises to support dragged app files and pasteboard operations.
- [Supporting Collection View Drag and Drop Through File Promises](supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [class NSFilePromiseProvider](nsfilepromiseprovider.md)
  An object that provides a promise for the pasteboard.
- [protocol NSFilePromiseProviderDelegate](nsfilepromiseproviderdelegate.md)
  A set of methods that provides the name of the promised file and writes the file to the destination directory when the file promise is fulfilled.
- [class NSFilePromiseReceiver](nsfilepromisereceiver.md)
  An object that receives a file promise from the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/supporting-table-view-drag-and-drop-through-file-promises)*