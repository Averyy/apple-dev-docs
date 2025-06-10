# AutomaticSpatialAudio

**Framework**: Audio Toolbox  
**Kind**: struct

A spatial audio experience determined by the system.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct AutomaticSpatialAudio
```

#### Overview

Sounds with an automatic spatial audio experience that belong to an [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) inherit its [`intendedSpatialExperience`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/intendedSpatialExperience-1qwbe).

```swift
// Configure an audio player with an automatic spatial audio experience.
myPlayer.intendedSpatialExperience = .automatic
```

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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/automaticspatialaudio)*