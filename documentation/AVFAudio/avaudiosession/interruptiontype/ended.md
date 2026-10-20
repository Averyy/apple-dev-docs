# AVAudioSession.InterruptionType.ended

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

A type that indicates that the operating system ended interrupting the audio session.

**Availability**:
- iOS 6.0+ - Deprecated in 27.0
- iPadOS 6.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAudioSessionDidBecomeInactiveNotification and AVAudioSessionResumptionRecommendationNotification instead

## Declaration

```swift
case ended
```

```c
AVAudioSessionInterruptionTypeEnded
```

## Mentions

- [Handling audio interruptions](../../handling-audio-interruptions.md)

## See Also

### Identifying interruption types
- [AVAudioSession.InterruptionType.began](./began.md)
  A type that indicates that the operating system began interrupting the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptiontype/ended)*