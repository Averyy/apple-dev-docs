# FixedSpatialAudio

**Framework**: Audio Toolbox  
**Kind**: struct

A spatial experience that does not take user motion into account.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct FixedSpatialAudio
```

#### Overview

The lack of spatial tracking gives the impression of a “fixed” spatial experience locked to the user’s frame of reference.

```swift
// Configure an audio player with a fixed spatial audio experience.
myPlayer.intendedSpatialExperience = .fixed
```

For multi-channel experiences, you might also consider specifying the experience’s sound stage size if a system-specified size is not desirable.

```swift
// Configure an audio player with a fixed spatial audio experience
// that has a large sound stage size.
myPlayer.intendedSpatialExperience = .fixed(soundStageSize: .large)
```

## Topics

### Instance Properties
- [var soundStageSize: SpatialAudioExperiences.SoundStageSize](fixedspatialaudio/soundstagesize.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/fixedspatialaudio)*