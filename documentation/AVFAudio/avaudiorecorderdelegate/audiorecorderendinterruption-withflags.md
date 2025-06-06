# audioRecorderEndInterruption(_:withFlags:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate that the audio session interruption ended with flags.

**Availability**:
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder, withFlags flags: Int)
```

## Parameters

- `recorder`: The interrupted audio recorder.
- `flags`: The flags that indicate the state of the audio session.

## See Also

- [func audioRecorderBeginInterruption(AVAudioRecorder)](avaudiorecorderdelegate/audiorecorderbegininterruption(_:).md)
  Tells the delegate that the system interrupted the audio recording.
- [func audioRecorderEndInterruption(AVAudioRecorder)](avaudiorecorderdelegate/audiorecorderendinterruption(_:).md)
  Tells the delegate that the audio session interruption ended.
- [func audioRecorderEndInterruption(AVAudioRecorder, withOptions: Int)](avaudiorecorderdelegate/audiorecorderendinterruption(_:withoptions:).md)
  Tells the delegate that the audio session interruption ended with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorderdelegate/audiorecorderendinterruption(_:withflags:))*