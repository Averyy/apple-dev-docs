# AVAudioSession.InterruptionOptions

**Framework**: AVFAudio  
**Kind**: struct

Constants that indicate the state of an audio session after an interruption.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [AVAudioSession.InterruptionType](avaudiosession/interruptiontype.md)
  Constants that describe the type of an audio interruption.
- [AVAudioSession.InterruptionReason](avaudiosession/interruptionreason.md)
  Constants that define the reasons for an audio session interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionoptions)*