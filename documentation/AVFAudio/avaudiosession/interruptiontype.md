# AVAudioSession.InterruptionType

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the type of an audio interruption.

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
enum InterruptionType
```

```c
enum AVAudioSessionInterruptionType : NSUInteger;
```

## Mentions

- [Handling audio interruptions](../handling-audio-interruptions.md)

## Topics

### Creating an interruption type
- [init?(rawValue: UInt)](./interruptiontype/init%28rawvalue%29.md)
### Identifying interruption types
- [AVAudioSession.InterruptionType.began](./interruptiontype/began.md)
  A type that indicates that the operating system began interrupting the audio session.
- [AVAudioSession.InterruptionType.ended](./interruptiontype/ended.md)
  A type that indicates that the operating system ended interrupting the audio session.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### User info values
- [AVAudioSession.InterruptionOptions](./interruptionoptions.md)
  Constants that indicate the state of an audio session after an interruption.
- [AVAudioSession.InterruptionReason](./interruptionreason.md)
  Constants that define the reasons for an audio session interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptiontype)*