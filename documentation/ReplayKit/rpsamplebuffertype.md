# RPSampleBufferType

**Framework**: ReplayKit  
**Kind**: enum  
**Role**: Enumeration

The type of media clip sample being buffered.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use SCStreamOutputType instead

## Declaration

```swift
enum RPSampleBufferType
```

```c
enum RPSampleBufferType : NSInteger;
```

## Topics

### Sample Buffer Types
- [RPSampleBufferType.audioApp](./rpsamplebuffertype/audioapp.md)
  The sample audio that originates from the app.
- [RPSampleBufferType.audioMic](./rpsamplebuffertype/audiomic.md)
  The sample audio that originates from the microphone.
- [RPSampleBufferType.video](./rpsamplebuffertype/video.md)
  The sample that contains a video clip.
### Initializers
- [init?(rawValue: Int)](./rpsamplebuffertype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controlling App Recording
- [func startRecording(handler: (((any Error)?) -> Void)?)](./rpscreenrecorder/startrecording%28handler%29.md)
  Starts recording the app display.
- [func stopRecording(handler: ((RPPreviewViewController?, (any Error)?) -> Void)?)](./rpscreenrecorder/stoprecording%28handler%29.md)
  Stops the current recording.
- [func stopRecording(withOutput: URL, completionHandler: (((any Error)?) -> Void)?)](./rpscreenrecorder/stoprecording%28withoutput,completionhandler%29.md)
  Stops the current recording and writes the movie to the specified output URL.
- [func startCapture(handler: ((CMSampleBuffer, RPSampleBufferType, (any Error)?) -> Void)?, completionHandler: (((any Error)?) -> Void)?)](./rpscreenrecorder/startcapture%28handler,completionhandler%29.md)
  Starts screen and audio capture.
- [func stopCapture(handler: (((any Error)?) -> Void)?)](./rpscreenrecorder/stopcapture%28handler%29.md)
  Stops screen capture
- [func discardRecording(handler: () -> Void)](./rpscreenrecorder/discardrecording%28handler%29.md)
  Discards the current recording.
- [func startRecording(withMicrophoneEnabled: Bool, handler: (((any Error)?) -> Void)?)](./rpscreenrecorder/startrecording%28withmicrophoneenabled,handler%29.md)
  Starts recording the app’s audio and video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype)*