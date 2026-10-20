# AVAudioSessionInterruptionFlags_ShouldResume

**Framework**: AVFAudio  
**Kind**: var  
**Role**: Global Variable

Indicates that your audio session is active and ready for use.

**Availability**:
- iOS 4.0+ - Deprecated in 6.0 (renamed: AVAudioSessionInterruptionOptions)
- iPadOS 4.0+ - Deprecated in 6.0 (renamed: AVAudioSessionInterruptionOptions)
- Mac Catalyst 4.0+ - Deprecated in 6.0 (renamed: AVAudioSessionInterruptionOptions)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: AVAudioSessionInterruptionOptions)

> **Deprecated**: Use [`AVAudioSession.InterruptionOptions`](./avaudiosession/interruptionoptions.md) instead.

## Declaration

```swift
var AVAudioSessionInterruptionFlags_ShouldResume: Int { get }
```

```c
AVAudioSessionInterruptionFlags_ShouldResume
```

#### Discussion

Your app can resume the interrupted audio operation. See [Handling audio interruptions](./handling-audio-interruptions.md) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessioninterruptionflags_shouldresume)*