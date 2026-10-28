# stopRecording(handler:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Stops the current recording.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit SCStream with SCRecordingOutput instead

## Declaration

```swift
func stopRecording(handler: ((RPPreviewViewController?, (any Error)?) -> Void)? = nil)
```

```objc
- (void) stopRecordingWithHandler:(void (^)(RPPreviewViewController *previewViewController, NSError *error)) handler;
```

## Discussion

When recording stops with no associated error, present the resulting preview view controller using [`present(_:animated:completion:)`](../../UIKit/uiviewcontroller/present%28_,animated,completion%29.md). The user will see the built-in preview view controller with options to trim, cut, and share the recording. On iPad, you must present the preview view controller as a popover.

Listing 1. Presenting the preview view controller on iPad

```swift
sharedRecorder.stopRecording { previewViewController, error in
    guard let _ = error else {
        print("\(error?.localizedDescription ?? "Error")")
        return
    }
    if let previewViewController = previewViewController {
        if UIDevice.current.userInterfaceIdiom == .pad {
            previewViewController.modalPresentationStyle = .popover
            previewViewController.popoverPresentationController?.sourceRect = .zero
            previewViewController.popoverPresentationController?.sourceView = self.view
        }
        
        self.previewViewController = previewViewController
        previewViewController.previewControllerDelegate = self

        // Present the view controller.
        self.present(previewViewController, animated: true, completion: nil)
    }
}
```

## Parameters

- `handler`: A block that is called when the request completes.

  - **`previewViewController`**: An instance of the `RPPreviewViewController` class.
  - **`error`**: If an error occurred, this parameter holds an object that explains the error. Otherwise, the value of this parameter is `nil`. See [`RPRecordingErrorCode`](../rprecordingerrorcode.md) for a list of error codes to ReplayKit.

## See Also

### Controlling App Recording
- [func startRecording(handler: (((any Error)?) -> Void)?)](./startrecording%28handler%29.md)
  Starts recording the app display.
- [func stopRecording(withOutput: URL, completionHandler: (((any Error)?) -> Void)?)](./stoprecording%28withoutput,completionhandler%29.md)
  Stops the current recording and writes the movie to the specified output URL.
- [func startCapture(handler: ((CMSampleBuffer, RPSampleBufferType, (any Error)?) -> Void)?, completionHandler: (((any Error)?) -> Void)?)](./startcapture%28handler,completionhandler%29.md)
  Starts screen and audio capture.
- [enum RPSampleBufferType](../rpsamplebuffertype.md)
  The type of media clip sample being buffered.
- [func stopCapture(handler: (((any Error)?) -> Void)?)](./stopcapture%28handler%29.md)
  Stops screen capture
- [func discardRecording(handler: () -> Void)](./discardrecording%28handler%29.md)
  Discards the current recording.
- [func startRecording(withMicrophoneEnabled: Bool, handler: (((any Error)?) -> Void)?)](./startrecording%28withmicrophoneenabled,handler%29.md)
  Starts recording the app’s audio and video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/stoprecording(handler:))*