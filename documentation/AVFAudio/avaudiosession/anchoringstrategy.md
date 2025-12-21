# AVAudioSession.AnchoringStrategy

**Framework**: AVFAudio  
**Kind**: enum

Constants that specify how to set the origin of audio in a head-tracked spatial experience.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum AnchoringStrategy
```

## Topics

### Anchoring strategies
- [AVAudioSession.AnchoringStrategy.automatic](avaudiosession/anchoringstrategy/automatic.md)
  The system determines the anchoring strategy.
- [AVAudioSession.AnchoringStrategy.front](avaudiosession/anchoringstrategy/front.md)
  The audio session anchors to a person’s concept of front.
- [AVAudioSession.AnchoringStrategy.scene(identifier:)](avaudiosession/anchoringstrategy/scene(identifier:).md)
  The audio session anchors to a scene.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func fixed(soundStageSize: AVAudioSession.SoundStageSize) -> Self](avaudiosessionspatialexperience-swift.protocol/fixed(soundstagesize:).md)
- [static func headTracked(soundStageSize: AVAudioSession.SoundStageSize, anchoringStrategy: AVAudioSession.AnchoringStrategy) -> Self](avaudiosessionspatialexperience-swift.protocol/headtracked(soundstagesize:anchoringstrategy:).md)
- [static var bypassed: AVAudioSession.BypassedSpatialExperience](avaudiosessionspatialexperience-swift.protocol/bypassed.md)
- [AVAudioSession.SoundStageSize](avaudiosession/soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/anchoringstrategy)*