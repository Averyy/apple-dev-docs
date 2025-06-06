# audioRecorderBeginInterruption(_:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate that the system interrupted the audio recording.

**Availability**:
- iOS 2.2+
- iPadOS 2.2+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func audioRecorderBeginInterruption(_ recorder: AVAudioRecorder)
```

## Parameters

- `recorder`: The interrupted audio recorder.

## See Also

- [func audioRecorderEndInterruption(AVAudioRecorder)](avaudiorecorderdelegate/audiorecorderendinterruption(_:).md)
  Tells the delegate that the audio session interruption ended.
- [func audioRecorderEndInterruption(AVAudioRecorder, withOptions: Int)](avaudiorecorderdelegate/audiorecorderendinterruption(_:withoptions:).md)
  Tells the delegate that the audio session interruption ended with options.
- [func audioRecorderEndInterruption(AVAudioRecorder, withFlags: Int)](avaudiorecorderdelegate/audiorecorderendinterruption(_:withflags:).md)
  Tells the delegate that the audio session interruption ended with flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorderdelegate/audiorecorderbegininterruption(_:))*