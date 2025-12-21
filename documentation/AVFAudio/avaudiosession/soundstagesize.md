# AVAudioSession.SoundStageSize

**Framework**: AVFAudio  
**Kind**: enum

Constants that specify the perceived size of sounds the audio session plays.

**Availability**:
- visionOS ?+

## Declaration

```swift
enum SoundStageSize
```

## Topics

### Sound stage sizes
- [AVAudioSession.SoundStageSize.automatic](avaudiosession/soundstagesize/automatic.md)
  The system sets the sound stage size.
- [AVAudioSession.SoundStageSize.small](avaudiosession/soundstagesize/small.md)
  A small sound stage.
- [AVAudioSession.SoundStageSize.medium](avaudiosession/soundstagesize/medium.md)
  A medium sound stage.
- [AVAudioSession.SoundStageSize.large](avaudiosession/soundstagesize/large.md)
  A large sound stage.
### Initializers
- [init?(rawValue: Int)](avaudiosession/soundstagesize/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func fixed(soundStageSize: AVAudioSession.SoundStageSize) -> Self](avaudiosessionspatialexperience-swift.protocol/fixed(soundstagesize:).md)
- [static func headTracked(soundStageSize: AVAudioSession.SoundStageSize, anchoringStrategy: AVAudioSession.AnchoringStrategy) -> Self](avaudiosessionspatialexperience-swift.protocol/headtracked(soundstagesize:anchoringstrategy:).md)
- [static var bypassed: AVAudioSession.BypassedSpatialExperience](avaudiosessionspatialexperience-swift.protocol/bypassed.md)
- [AVAudioSession.AnchoringStrategy](avaudiosession/anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/soundstagesize)*