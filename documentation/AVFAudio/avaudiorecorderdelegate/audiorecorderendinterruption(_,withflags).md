# audioRecorderEndInterruption(_:withFlags:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the audio session interruption ended with flags.

**Availability**:
- iOS 4.0+ - Deprecated in 6.0
- iPadOS 4.0+ - Deprecated in 6.0
- Mac Catalyst 4.0+ - Deprecated in 6.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Observe audio session interruption notifications instead. See [Handling audio interruptions](../handling-audio-interruptions.md) for more information.

## Declaration

```swift
optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder, withFlags flags: Int)
```

```objc
- (void) audioRecorderEndInterruption:(AVAudioRecorder *) recorder withFlags:(NSUInteger) flags;
```

## Parameters

- `recorder`: The interrupted audio recorder.
- `flags`: The flags that indicate the state of the audio session.

## See Also

### Responding to audio interruptions
- [func audioRecorderBeginInterruption(AVAudioRecorder)](./audiorecorderbegininterruption%28_%29.md)
  Tells the delegate that the system interrupted the audio recording.
- [func audioRecorderEndInterruption(AVAudioRecorder)](./audiorecorderendinterruption%28_%29.md)
  Tells the delegate that the audio session interruption ended.
- [func audioRecorderEndInterruption(AVAudioRecorder, withOptions: Int)](./audiorecorderendinterruption%28_,withoptions%29.md)
  Tells the delegate that the audio session interruption ended with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorderdelegate/audiorecorderendinterruption(_:withflags:))*