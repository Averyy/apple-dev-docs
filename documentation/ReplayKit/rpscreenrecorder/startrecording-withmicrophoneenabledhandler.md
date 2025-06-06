# startRecording(withMicrophoneEnabled:handler:)

**Framework**: ReplayKit  
**Kind**: method

Starts recording the app’s audio and video.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func startRecording(withMicrophoneEnabled microphoneEnabled: Bool, handler: (((any Error)?) -> Void)? = nil)
```

#### Discussion

Call [`startRecording(withMicrophoneEnabled:handler:)`](rpscreenrecorder/startrecording(withmicrophoneenabled:handler:).md) on an instance of the recorder to begin recording. When [`startRecording(withMicrophoneEnabled:handler:)`](rpscreenrecorder/startrecording(withmicrophoneenabled:handler:).md) is first called, an alert window appears asking the user to confirm recording. This alert window is also presented if it has been longer than 8 minutes since the last time [`startRecording(withMicrophoneEnabled:handler:)`](rpscreenrecorder/startrecording(withmicrophoneenabled:handler:).md) was called.

## Parameters

- `microphoneEnabled`: Set to   to activate the microphone during the recording. Defaults to  .
- `handler`: A block that is called when the request completes.

## See Also

- [func startRecording(handler: (((any Error)?) -> Void)?)](rpscreenrecorder/startrecording(handler:).md)
  Starts recording the app display.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/startrecording(withmicrophoneenabled:handler:))*