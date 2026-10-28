# BypassedSpatialAudio

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

An experience in which the system does not apply spatial processing to the audio stream.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct BypassedSpatialAudio
```

## Overview

Use this if implementing your own spatial audio rendering or designing an experience that should not have spatial audio.

```swift
// Configure an audio player with a bypassed spatial audio experience.
myPlayer.intendedSpatialExperience = .bypassed
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/bypassedspatialaudio)*