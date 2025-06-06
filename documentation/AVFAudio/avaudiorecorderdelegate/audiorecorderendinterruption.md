# audioRecorderEndInterruption(_:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate that the audio session interruption ended.

**Availability**:
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder)
```

## Parameters

- `recorder`: The interrupted audio recorder.

## See Also

- [func audioRecorderBeginInterruption(AVAudioRecorder)](avaudiorecorderdelegate/audiorecorderbegininterruption(_:).md)
  Tells the delegate that the system interrupted the audio recording.
- [func audioRecorderEndInterruption(AVAudioRecorder, withOptions: Int)](avaudiorecorderdelegate/audiorecorderendinterruption(_:withoptions:).md)
  Tells the delegate that the audio session interruption ended with options.
- [func audioRecorderEndInterruption(AVAudioRecorder, withFlags: Int)](avaudiorecorderdelegate/audiorecorderendinterruption(_:withflags:).md)
  Tells the delegate that the audio session interruption ended with flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorderdelegate/audiorecorderendinterruption(_:))*