# SpatialAudioExperience

**Framework**: Audio Toolbox  
**Kind**: protocol

Configure an audio stream for spatial computing.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
protocol SpatialAudioExperience : Decodable, Encodable, Hashable, Sendable
```

## Mentions

- [Anchoring sound to a window or volume](spatializing-sound-from-a-uiscene.md)

#### Overview

All audio playback APIs support 3D spatial rendering using SpatialAudioExperience. For example, with [`AVAudioPlayer`](https://developer.apple.com/documentation/AVFAudio/AVAudioPlayer):

```swift
// Create a player.
let myPlayer = try AVAudioPlayer(contentsOf: myAudioFileURL)

// Configure an audio player with a head-tracked spatial audio experience
// so that it's audible from a distinct location in space.
myPlayer.intendedSpatialExperience = .headTracked

// Play sound with the configured spatial audio experience.
player.play()
```

> **Note**: - [`SpatialAudioExperiences.AnchoringStrategy`](spatialaudioexperiences/anchoringstrategy.md)
- [`SpatialAudioExperiences.SoundStageSize`](spatialaudioexperiences/soundstagesize.md)

## Topics

### Type Properties
- [static var automatic: AutomaticSpatialAudio](spatialaudioexperience/automatic.md)
  An automatic spatial experience.
- [static var bypassed: BypassedSpatialAudio](spatialaudioexperience/bypassed.md)
  A bypassed spatial audio experience.
- [static var fixed: FixedSpatialAudio](spatialaudioexperience/fixed.md)
  A fixed spatial audio experience with an automatic sound stage size.
- [static var headTracked: HeadTrackedSpatialAudio](spatialaudioexperience/headtracked.md)
  A head-tracked spatial audio experience with an automatic anchoring strategy and automatic sound stage size.
### Type Methods
- [static func fixed(soundStageSize: SpatialAudioExperiences.SoundStageSize) -> Self](spatialaudioexperience/fixed(soundstagesize:).md)
  Create a fixed spatial audio experience with a specific sound stage size.
- [static func headTracked(SpatialAudioExperiences.AnchoringStrategy, soundStageSize: SpatialAudioExperiences.SoundStageSize) -> Self](spatialaudioexperience/headtracked(_:soundstagesize:).md)
  Create a head-tracked spatial audio experience with a specific anchoring strategy and sound stage size.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [AutomaticSpatialAudio](automaticspatialaudio.md)
- [BypassedSpatialAudio](bypassedspatialaudio.md)
- [FixedSpatialAudio](fixedspatialaudio.md)
- [HeadTrackedSpatialAudio](headtrackedspatialaudio.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/spatialaudioexperience)*