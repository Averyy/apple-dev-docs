# AutomaticSpatialAudio

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

A spatial audio experience determined by the system.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct AutomaticSpatialAudio
```

#### Overview

Sounds with an automatic spatial audio experience that belong to an [`AVAudioSession`](../AVFAudio/avaudiosession.md) inherit its [`intendedSpatialExperience`](../AVFAudio/avaudiosession/intendedspatialexperience-qlty.md).

```swift
// Configure an audio player with an automatic spatial audio experience.
myPlayer.intendedSpatialExperience = .automatic
```

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SpatialAudioExperience](./spatialaudioexperience.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/automaticspatialaudio)*