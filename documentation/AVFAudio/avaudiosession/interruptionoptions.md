# AVAudioSession.InterruptionOptions

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

Constants that indicate the state of an audio session after an interruption.

**Availability**:
- iOS 6.0+ - Deprecated in 27.0
- iPadOS 6.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAudioSessionResumptionRecommendationNotification instead

## Declaration

```swift
struct InterruptionOptions
```

```c
enum AVAudioSessionInterruptionOptions : NSUInteger;
```

## Mentions

- [Handling audio interruptions](../handling-audio-interruptions.md)

## Topics

### Creating an interruption option
- [init(rawValue: UInt)](./interruptionoptions/init%28rawvalue%29.md)
  Creates a new instance with the raw value you specify.
### Getting standard interruption options
- [static var shouldResume: AVAudioSession.InterruptionOptions](./interruptionoptions/shouldresume.md)
  An option that indicates the interruption by another audio session has ended and the app can resume its audio session.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### User info values
- [AVAudioSession.InterruptionType](./interruptiontype.md)
  Constants that describe the type of an audio interruption.
- [AVAudioSession.InterruptionReason](./interruptionreason.md)
  Constants that define the reasons for an audio session interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionoptions)*