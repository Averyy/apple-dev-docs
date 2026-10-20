# SpatialAudioExperiences.SoundStageSize

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

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
- [SpatialAudioExperiences.SoundStageSize.automatic](./soundstagesize/automatic.md)
  A system-defined sound stage size.
- [SpatialAudioExperiences.SoundStageSize.large](./soundstagesize/large.md)
  Spreads an audio stream’s channels around the user according to the coordinates described in its channel layout.
- [SpatialAudioExperiences.SoundStageSize.medium](./soundstagesize/medium.md)
  Pulls an audio stream’s channels closer to the channel layout’s front.
- [SpatialAudioExperiences.SoundStageSize.small](./soundstagesize/small.md)
  Places all of an audio stream’s channels near the layout’s front.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/spatialaudioexperiences/soundstagesize)*