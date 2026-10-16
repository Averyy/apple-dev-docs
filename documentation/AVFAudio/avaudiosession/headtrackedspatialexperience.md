# AVAudioSession.HeadTrackedSpatialExperience

**Framework**: AVFAudio  
**Kind**: struct

An experience where the sound a size dictated by its sound stage and location dictated by its anchoring strategy.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct HeadTrackedSpatialExperience
```

## Topics

### Inspecting the experience
- [var anchoringStrategy: AVAudioSession.AnchoringStrategy](avaudiosession/headtrackedspatialexperience/anchoringstrategy.md)
- [var soundStageSize: AVAudioSession.SoundStageSize](avaudiosession/headtrackedspatialexperience/soundstagesize.md)

## Relationships

### Conforms To
- [AVAudioSessionSpatialExperience](avaudiosessionspatialexperience-swift.protocol.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static func fixed(soundStageSize: AVAudioSession.SoundStageSize) -> Self](avaudiosessionspatialexperience-swift.protocol/fixed(soundstagesize:).md)
- [AVAudioSession.FixedSpatialExperience](avaudiosession/fixedspatialexperience.md)
  An experience where the sound has a size dictated by its sound stage and is head-locked relative to the user.
- [static func headTracked(soundStageSize: AVAudioSession.SoundStageSize, anchoringStrategy: AVAudioSession.AnchoringStrategy) -> Self](avaudiosessionspatialexperience-swift.protocol/headtracked(soundstagesize:anchoringstrategy:).md)
- [static var bypassed: AVAudioSession.BypassedSpatialExperience](avaudiosessionspatialexperience-swift.protocol/bypassed.md)
- [AVAudioSession.BypassedSpatialExperience](avaudiosession/bypassedspatialexperience.md)
  An experience that bypasses system-provided audio spatialization.
- [AVAudioSession.SoundStageSize](avaudiosession/soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [AVAudioSession.AnchoringStrategy](avaudiosession/anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/headtrackedspatialexperience)*