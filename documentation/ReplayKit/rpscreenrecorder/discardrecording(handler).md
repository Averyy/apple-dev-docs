# discardRecording(handler:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Discards the current recording.

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
func discardRecording(handler: @escaping () -> Void)
```

```objc
- (void) discardRecordingWithHandler:(void (^)()) handler;
```

## Discussion

[`discardRecording(handler:)`](./discardrecording%28handler%29.md) can only be called after the handler block in [`stopRecording(handler:)`](./stoprecording%28handler%29.md) has been called. Use the `handler` block to do any required cleanup, including setting any `RPPreviewScreenController` references to `nil`.

## Parameters

- `handler`: A block that is called when the request is completed.

## See Also

### Controlling App Recording
- [func startRecording(handler: (((any Error)?) -> Void)?)](./startrecording%28handler%29.md)
  Starts recording the app display.
- [func stopRecording(handler: ((RPPreviewViewController?, (any Error)?) -> Void)?)](./stoprecording%28handler%29.md)
  Stops the current recording.
- [func stopRecording(withOutput: URL, completionHandler: (((any Error)?) -> Void)?)](./stoprecording%28withoutput,completionhandler%29.md)
  Stops the current recording and writes the movie to the specified output URL.
- [func startCapture(handler: ((CMSampleBuffer, RPSampleBufferType, (any Error)?) -> Void)?, completionHandler: (((any Error)?) -> Void)?)](./startcapture%28handler,completionhandler%29.md)
  Starts screen and audio capture.
- [enum RPSampleBufferType](../rpsamplebuffertype.md)
  The type of media clip sample being buffered.
- [func stopCapture(handler: (((any Error)?) -> Void)?)](./stopcapture%28handler%29.md)
  Stops screen capture
- [func startRecording(withMicrophoneEnabled: Bool, handler: (((any Error)?) -> Void)?)](./startrecording%28withmicrophoneenabled,handler%29.md)
  Starts recording the app’s audio and video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/discardrecording(handler:))*