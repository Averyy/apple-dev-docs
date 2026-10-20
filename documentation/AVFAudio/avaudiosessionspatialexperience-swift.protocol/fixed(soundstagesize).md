# fixed(soundStageSize:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Type Method

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static func fixed(soundStageSize: AVAudioSession.SoundStageSize) -> Self
```

Available when `Self` is `AVAudioSession.FixedSpatialExperience`.

## See Also

### Choosing an experience
- [AVAudioSession.FixedSpatialExperience](../avaudiosession/fixedspatialexperience.md)
  An experience where the sound has a size dictated by its sound stage and is head-locked relative to the user.
- [static func headTracked(soundStageSize: AVAudioSession.SoundStageSize, anchoringStrategy: AVAudioSession.AnchoringStrategy) -> Self](./headtracked%28soundstagesize,anchoringstrategy%29.md)
- [AVAudioSession.HeadTrackedSpatialExperience](../avaudiosession/headtrackedspatialexperience.md)
  An experience where the sound a size dictated by its sound stage and location dictated by its anchoring strategy.
- [static var bypassed: AVAudioSession.BypassedSpatialExperience](./bypassed.md)
- [AVAudioSession.BypassedSpatialExperience](../avaudiosession/bypassedspatialexperience.md)
  An experience that bypasses system-provided audio spatialization.
- [AVAudioSession.SoundStageSize](../avaudiosession/soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [AVAudioSession.AnchoringStrategy](../avaudiosession/anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionspatialexperience-swift.protocol/fixed(soundstagesize:))*