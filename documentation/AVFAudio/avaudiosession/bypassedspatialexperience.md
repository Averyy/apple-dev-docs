# AVAudioSession.BypassedSpatialExperience

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

An experience that bypasses system-provided audio spatialization.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct BypassedSpatialExperience
```

## Relationships

### Conforms To
- [AVAudioSessionSpatialExperience](../avaudiosessionspatialexperience-swift.protocol.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Choosing an experience
- [static func fixed(soundStageSize: AVAudioSession.SoundStageSize) -> Self](../avaudiosessionspatialexperience-swift.protocol/fixed%28soundstagesize%29.md)
- [AVAudioSession.FixedSpatialExperience](./fixedspatialexperience.md)
  An experience where the sound has a size dictated by its sound stage and is head-locked relative to the user.
- [static func headTracked(soundStageSize: AVAudioSession.SoundStageSize, anchoringStrategy: AVAudioSession.AnchoringStrategy) -> Self](../avaudiosessionspatialexperience-swift.protocol/headtracked%28soundstagesize,anchoringstrategy%29.md)
- [AVAudioSession.HeadTrackedSpatialExperience](./headtrackedspatialexperience.md)
  An experience where the sound a size dictated by its sound stage and location dictated by its anchoring strategy.
- [static var bypassed: AVAudioSession.BypassedSpatialExperience](../avaudiosessionspatialexperience-swift.protocol/bypassed.md)
- [AVAudioSession.SoundStageSize](./soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [AVAudioSession.AnchoringStrategy](./anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/bypassedspatialexperience)*