# AVAudioSession.SilenceSecondaryAudioHintType

**Framework**: AVFAudio  
**Kind**: enum

Constants that indicate whether optional secondary audio muting should begin or end.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum SilenceSecondaryAudioHintType
```

## Topics

### Creating a hint type
- [init?(rawValue: UInt)](avaudiosession/silencesecondaryaudiohinttype/init(rawvalue:).md)
### Identifying hint types
- [AVAudioSession.SilenceSecondaryAudioHintType.begin](avaudiosession/silencesecondaryaudiohinttype/begin.md)
  A value that indicates that another application’s primary audio has started.
- [AVAudioSession.SilenceSecondaryAudioHintType.end](avaudiosession/silencesecondaryaudiohinttype/end.md)
  A value that indicates that another application’s primary audio has stopped.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/silencesecondaryaudiohinttype)*