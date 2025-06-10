# AVAudioRecorderDelegate

**Framework**: AVFAudio  
**Kind**: protocol

A protocol that defines the methods to respond to audio recording events and encoding errors.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
protocol AVAudioRecorderDelegate : NSObjectProtocol, Sendable
```

## Topics

### Responding to Recording Completion
- [func audioRecorderDidFinishRecording(AVAudioRecorder, successfully: Bool)](avaudiorecorderdelegate/audiorecorderdidfinishrecording(_:successfully:).md)
  Tells the delegate when recording stops or finishes due to reaching its time limit.
### Responding to Audio Encoding Errors
- [func audioRecorderEncodeErrorDidOccur(AVAudioRecorder, error: (any Error)?)](avaudiorecorderdelegate/audiorecorderencodeerrordidoccur(_:error:).md)
  Tells the delegate that the audio recorder encountered an encoding error during recording.
### Responding to Audio Interruptions
- [func audioRecorderBeginInterruption(AVAudioRecorder)](avaudiorecorderdelegate/audiorecorderbegininterruption(_:).md)
  Tells the delegate that the system interrupted the audio recording.
- [func audioRecorderEndInterruption(AVAudioRecorder)](avaudiorecorderdelegate/audiorecorderendinterruption(_:).md)
  Tells the delegate that the audio session interruption ended.
- [func audioRecorderEndInterruption(AVAudioRecorder, withOptions: Int)](avaudiorecorderdelegate/audiorecorderendinterruption(_:withoptions:).md)
  Tells the delegate that the audio session interruption ended with options.
- [func audioRecorderEndInterruption(AVAudioRecorder, withFlags: Int)](avaudiorecorderdelegate/audiorecorderendinterruption(_:withflags:).md)
  Tells the delegate that the audio session interruption ended with flags.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var delegate: (any AVAudioRecorderDelegate)?](avaudiorecorder/delegate.md)
  The delegate object for the audio recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorderdelegate)*