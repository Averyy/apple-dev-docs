# AutomaticSpatialAudio

**Framework**: Audio Toolbox  
**Kind**: struct

A spatial audio experience determined by the system.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct AutomaticSpatialAudio
```

#### Overview

Sounds with an automatic spatial audio experience that belong to an [`AVAudioSession`](https://developer.apple.com/documentation/avfaudio/avaudiosession) inherit its doc://com.apple.documentation/documentation/avfaudio/avaudiosession/intendedspatialexperience-1qwbe.

```swift
// Configure an audio player with an automatic spatial audio experience.
myPlayer.intendedSpatialExperience = .automatic
```

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SpatialAudioExperience](spatialaudioexperience.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/automaticspatialaudio)*