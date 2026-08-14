# SpatialAudioExperiences.SoundStageSize

**Framework**: Audio Toolbox  
**Kind**: enum

Configure the distribution of audio channels in 3D space.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum SoundStageSize
```

#### Overview

For multi-channel sounds, the sound stage size describes how the channels are positioned relative to the coordinates described in the sound’s channel layout.

## Topics

### Enumeration Cases
- [SpatialAudioExperiences.SoundStageSize.automatic](spatialaudioexperiences/soundstagesize/automatic.md)
  A system-defined sound stage size.
- [SpatialAudioExperiences.SoundStageSize.large](spatialaudioexperiences/soundstagesize/large.md)
  Spreads an audio stream’s channels around the user according to the coordinates described in its channel layout.
- [SpatialAudioExperiences.SoundStageSize.medium](spatialaudioexperiences/soundstagesize/medium.md)
  Pulls an audio stream’s channels closer to the channel layout’s front.
- [SpatialAudioExperiences.SoundStageSize.small](spatialaudioexperiences/soundstagesize/small.md)
  Places all of an audio stream’s channels near the layout’s front.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/spatialaudioexperiences/soundstagesize)*