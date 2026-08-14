# SpatialAudioExperiences.AnchoringStrategy

**Framework**: Audio Toolbox  
**Kind**: enum

The center of a head-tracked spatial experience.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum AnchoringStrategy
```

#### Overview

For mono sounds, this defines the sound’s single location. For multi-channel sounds this defines the position of the channel layout’s front with all channels placed around the user relative to that front.

## Topics

### Enumeration Cases
- [SpatialAudioExperiences.AnchoringStrategy.automatic](spatialaudioexperiences/anchoringstrategy/automatic.md)
  A system-defined anchoring strategy.
- [SpatialAudioExperiences.AnchoringStrategy.front](spatialaudioexperiences/anchoringstrategy/front.md)
  Anchor to the front of the user’s space.
- [SpatialAudioExperiences.AnchoringStrategy.scene(identifier:)](spatialaudioexperiences/anchoringstrategy/scene(identifier:).md)
  Anchor to the visual center of a particular UIScene.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/spatialaudioexperiences/anchoringstrategy)*