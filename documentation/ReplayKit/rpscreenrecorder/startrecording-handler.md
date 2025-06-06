# startRecording(handler:)

**Framework**: ReplayKit  
**Kind**: method

Starts recording the app display.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func startRecording(handler: (((any Error)?) -> Void)? = nil)
```

#### Discussion

Call [`startRecording(handler:)`](rpscreenrecorder/startrecording(handler:).md) on an instance of the recorder to begin recording. When [`startRecording(handler:)`](rpscreenrecorder/startrecording(handler:).md) is first called, an alert window appears asking the user to confirm recording. This alert window is also presented if it has been longer than 8 minutes since the last time [`startRecording(handler:)`](rpscreenrecorder/startrecording(handler:).md) was called.

## Parameters

- `handler`: A block that is called when the request completes.

## See Also

- [func stopRecording(handler: ((RPPreviewViewController?, (any Error)?) -> Void)?)](rpscreenrecorder/stoprecording(handler:).md)
  Stops the current recording.
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

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/startrecording(handler:))*