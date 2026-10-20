# startRecording(withMicrophoneEnabled:handler:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Starts recording the app’s audio and video.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use microphoneEnabled property

## Declaration

```swift
func startRecording(withMicrophoneEnabled microphoneEnabled: Bool, handler: (((any Error)?) -> Void)? = nil)
```

```objc
- (void) startRecordingWithMicrophoneEnabled:(BOOL) microphoneEnabled handler:(void (^)(NSError *error)) handler;
```

#### Discussion

Call [`startRecording(withMicrophoneEnabled:handler:)`](./startrecording%28withmicrophoneenabled,handler%29.md) on an instance of the recorder to begin recording. When [`startRecording(withMicrophoneEnabled:handler:)`](./startrecording%28withmicrophoneenabled,handler%29.md) is first called, an alert window appears asking the user to confirm recording. This alert window is also presented if it has been longer than 8 minutes since the last time [`startRecording(withMicrophoneEnabled:handler:)`](./startrecording%28withmicrophoneenabled,handler%29.md) was called.

## Parameters

- `microphoneEnabled`: Set to [`true`](../../Swift/true.md) to activate the microphone during the recording. Defaults to [`false`](../../Swift/false.md).
- `handler`: A block that is called when the request completes.

  - **`error`**: If an error occurred, this parameter holds an object that explains the error. Otherwise, the value of this parameter is `nil`. See [`RPRecordingErrorCode`](../rprecordingerrorcode.md) for a list of error codes specific to ReplayKit.

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
- [func discardRecording(handler: () -> Void)](./discardrecording%28handler%29.md)
  Discards the current recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/startrecording(withmicrophoneenabled:handler:))*