# HeadTrackedSpatialAudio

**Framework**: Audio Toolbox  
**Kind**: struct

A spatial experience that takes user motion into account.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct HeadTrackedSpatialAudio
```

## Mentions

- [Anchoring sound to a window or volume](spatializing-sound-from-a-uiscene.md)

#### Overview

Sounds with a head-tracked experience come from a distinct location in space as defined by their anchoring strategy.

```swift
// Configure an audio player with a scene-anchored spatial audio experience.
myPlayer.intendedSpatialExperience = .headTracked(.scene(identifier: mySceneID))
```

For multi-channel experiences, you might also consider specifying the experience’s sound stage size if a system-specified size is not desirable.

```swift
// Configure an audio player with a front-anchored spatial audio experience
// and a large sound stage size.
myPlayer.intendedSpatialExperience = .headTracked(.front, soundStageSize: .large)
```

## Topics

### Instance Properties
- [var anchoringStrategy: SpatialAudioExperiences.AnchoringStrategy](headtrackedspatialaudio/anchoringstrategy.md)
  The experience’s anchoring strategy.
- [var soundStageSize: SpatialAudioExperiences.SoundStageSize](headtrackedspatialaudio/soundstagesize.md)
  The experience’s sound stage size.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpatialAudioExperience](spatialaudioexperience.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/headtrackedspatialaudio)*