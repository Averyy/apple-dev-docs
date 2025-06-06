# AVAudioSession.IOType.notSpecified

**Framework**: AVFAudio  
**Kind**: case

The default audio session I/O type.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case notSpecified
```

#### Discussion

Use this I/O type if your app doesn’t use [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession), or doesn’t have any specific requirements for aggregating input and output audio in the same realtime I/O callback. If your app doesn’t use a capture session, it gets aggregated I/O when using the [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) category.

If your app uses a capture session, specifying this value allows the session to start recording without causing glitches in the already running output audio. It also allows the system to use power-saving optimizations.

## See Also

- [AVAudioSession.IOType.aggregated](avaudiosession/iotype/aggregated.md)
  An I/O type that indicates if audio input and output should be presented in the same realtime I/O callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/iotype/notspecified)*