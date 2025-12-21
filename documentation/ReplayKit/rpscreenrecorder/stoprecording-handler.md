# stopRecording(handler:)

**Framework**: ReplayKit  
**Kind**: method

Stops the current recording.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func stopRecording(handler: ((RPPreviewViewController?, (any Error)?) -> Void)? = nil)
```

#### Discussion

When recording stops with no associated error, present the resulting preview view controller using [`present(_:animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/present(_:animated:completion:)). The user will see the built-in preview view controller with options to trim, cut, and share the recording. On iPad, you must present the preview view controller as a popover.

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

## See Also

- [func startRecording(handler: (((any Error)?) -> Void)?)](rpscreenrecorder/startrecording(handler:).md)
  Starts recording the app display.
- [func stopRecording(withOutput: URL, completionHandler: (((any Error)?) -> Void)?)](rpscreenrecorder/stoprecording(withoutput:completionhandler:).md)
  Stops the current recording and writes the movie to the specified output URL.
- [func startCapture(handler: ((CMSampleBuffer, RPSampleBufferType, (any Error)?) -> Void)?, completionHandler: (((any Error)?) -> Void)?)](rpscreenrecorder/startcapture(handler:completionhandler:).md)
  Starts screen and audio capture.
- [enum RPSampleBufferType](rpsamplebuffertype.md)
  The type of media clip sample being buffered.
- [func stopCapture(handler: (((any Error)?) -> Void)?)](rpscreenrecorder/stopcapture(handler:).md)
  Stops screen capture
- [func discardRecording(handler: () -> Void)](rpscreenrecorder/discardrecording(handler:).md)
  Discards the current recording.
- [func startRecording(withMicrophoneEnabled: Bool, handler: (((any Error)?) -> Void)?)](rpscreenrecorder/startrecording(withmicrophoneenabled:handler:).md)
  Starts recording the app’s audio and video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/stoprecording(handler:))*