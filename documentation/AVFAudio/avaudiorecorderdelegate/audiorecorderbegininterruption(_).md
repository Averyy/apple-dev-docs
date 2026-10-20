# audioRecorderBeginInterruption(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the system interrupted the audio recording.

**Availability**:
- iOS 2.2+ - Deprecated in 8.0
- iPadOS 2.2+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Observe audio session interruption notifications instead. See [Handling audio interruptions](../handling-audio-interruptions.md) for more information.

## Declaration

```swift
optional func audioRecorderBeginInterruption(_ recorder: AVAudioRecorder)
```

```objc
- (void) audioRecorderBeginInterruption:(AVAudioRecorder *) recorder;
```

## Parameters

- `recorder`: The interrupted audio recorder.

## See Also

### Responding to audio interruptions
- [func audioRecorderEndInterruption(AVAudioRecorder)](./audiorecorderendinterruption%28_%29.md)
  Tells the delegate that the audio session interruption ended.
- [func audioRecorderEndInterruption(AVAudioRecorder, withOptions: Int)](./audiorecorderendinterruption%28_,withoptions%29.md)
  Tells the delegate that the audio session interruption ended with options.
- [func audioRecorderEndInterruption(AVAudioRecorder, withFlags: Int)](./audiorecorderendinterruption%28_,withflags%29.md)
  Tells the delegate that the audio session interruption ended with flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorderdelegate/audiorecorderbegininterruption(_:))*