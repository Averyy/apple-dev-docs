# AVAudioSession.InterruptionOptions

**Framework**: AVFAudio  
**Kind**: struct

Constants that indicate the state of an audio session after an interruption.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct InterruptionOptions
```

## Mentions

- [Handling audio interruptions](handling-audio-interruptions.md)

## Topics

### Creating an Interruption Option
- [init(rawValue: UInt)](avaudiosession/interruptionoptions/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.
### Getting Standard Interruption Options
- [static var shouldResume: AVAudioSession.InterruptionOptions](avaudiosession/interruptionoptions/shouldresume.md)
  An option that indicates the interruption by another audio session has ended and the app can resume its audio session.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [AVAudioSession.InterruptionType](avaudiosession/interruptiontype.md)
  Constants that describe the type of an audio interruption.
- [AVAudioSession.InterruptionReason](avaudiosession/interruptionreason.md)
  Constants that define the reasons for an audio session interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionoptions)*