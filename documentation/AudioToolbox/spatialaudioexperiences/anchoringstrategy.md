# SpatialAudioExperiences.AnchoringStrategy

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

The center of a head-tracked spatial experience.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum AnchoringStrategy
```

## Overview

For mono sounds, this defines the sound’s single location. For multi-channel sounds this defines the position of the channel layout’s front with all channels placed around the user relative to that front.

## Topics

### Enumeration Cases
- [SpatialAudioExperiences.AnchoringStrategy.automatic](./anchoringstrategy/automatic.md)
  A system-defined anchoring strategy.
- [SpatialAudioExperiences.AnchoringStrategy.front](./anchoringstrategy/front.md)
  Anchor to the front of the user’s space.
- [SpatialAudioExperiences.AnchoringStrategy.scene(identifier:)](./anchoringstrategy/scene%28identifier%29.md)
  Anchor to the visual center of a particular UIScene.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/spatialaudioexperiences/anchoringstrategy)*