# audioRecorderEndInterruption(_:withOptions:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate that the audio session interruption ended with options.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder, withOptions flags: Int)
```

## Parameters

- `recorder`: The interrupted audio recorder.
- `flags`: The options that indicate the state of the audio session.

## See Also

- [func audioRecorderBeginInterruption(AVAudioRecorder)](avaudiorecorderdelegate/audiorecorderbegininterruption(_:).md)
  Tells the delegate that the system interrupted the audio recording.
- [func audioRecorderEndInterruption(AVAudioRecorder)](avaudiorecorderdelegate/audiorecorderendinterruption(_:).md)
  Tells the delegate that the audio session interruption ended.
- [func audioRecorderEndInterruption(AVAudioRecorder, withFlags: Int)](avaudiorecorderdelegate/audiorecorderendinterruption(_:withflags:).md)
  Tells the delegate that the audio session interruption ended with flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorderdelegate/audiorecorderendinterruption(_:withoptions:))*