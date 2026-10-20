# AVAudioRecorderDelegate

**Framework**: AVFAudio  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol AVAudioRecorderDelegate <NSObject>
```

## Topics

### Responding to recording completion
- [func audioRecorderDidFinishRecording(AVAudioRecorder, successfully: Bool)](./avaudiorecorderdelegate/audiorecorderdidfinishrecording%28_,successfully%29.md)
  Tells the delegate when recording stops or finishes due to reaching its time limit.
### Responding to audio encoding errors
- [func audioRecorderEncodeErrorDidOccur(AVAudioRecorder, error: (any Error)?)](./avaudiorecorderdelegate/audiorecorderencodeerrordidoccur%28_,error%29.md)
  Tells the delegate that the audio recorder encountered an encoding error during recording.
### Responding to audio interruptions
- [func audioRecorderBeginInterruption(AVAudioRecorder)](./avaudiorecorderdelegate/audiorecorderbegininterruption%28_%29.md)
  Tells the delegate that the system interrupted the audio recording.
- [func audioRecorderEndInterruption(AVAudioRecorder)](./avaudiorecorderdelegate/audiorecorderendinterruption%28_%29.md)
  Tells the delegate that the audio session interruption ended.
- [func audioRecorderEndInterruption(AVAudioRecorder, withOptions: Int)](./avaudiorecorderdelegate/audiorecorderendinterruption%28_,withoptions%29.md)
  Tells the delegate that the audio session interruption ended with options.
- [func audioRecorderEndInterruption(AVAudioRecorder, withFlags: Int)](./avaudiorecorderdelegate/audiorecorderendinterruption%28_,withflags%29.md)
  Tells the delegate that the audio session interruption ended with flags.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responding to recorder events
- [var delegate: (any AVAudioRecorderDelegate)?](./avaudiorecorder/delegate.md)
  The delegate object for the audio recorder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorderdelegate)*