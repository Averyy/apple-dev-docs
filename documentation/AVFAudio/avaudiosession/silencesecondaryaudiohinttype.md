# AVAudioSession.SilenceSecondaryAudioHintType

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate whether optional secondary audio muting should begin or end.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum SilenceSecondaryAudioHintType
```

```c
enum AVAudioSessionSilenceSecondaryAudioHintType : NSUInteger;
```

## Topics

### Creating a hint type
- [init?(rawValue: UInt)](./silencesecondaryaudiohinttype/init%28rawvalue%29.md)
### Identifying hint types
- [AVAudioSession.SilenceSecondaryAudioHintType.begin](./silencesecondaryaudiohinttype/begin.md)
  A value that indicates that another application’s primary audio has started.
- [AVAudioSession.SilenceSecondaryAudioHintType.end](./silencesecondaryaudiohinttype/end.md)
  A value that indicates that another application’s primary audio has stopped.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/silencesecondaryaudiohinttype)*