# AVAudioSessionSpatialExperience

**Framework**: AVFAudio  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- visionOS 1.0+

## Declaration

```swift
protocol AVAudioSessionSpatialExperience
```

## Topics

### Choosing an experience
- [static func fixed(soundStageSize: AVAudioSession.SoundStageSize) -> Self](./avaudiosessionspatialexperience-swift.protocol/fixed%28soundstagesize%29.md)
- [AVAudioSession.FixedSpatialExperience](./avaudiosession/fixedspatialexperience.md)
  An experience where the sound has a size dictated by its sound stage and is head-locked relative to the user.
- [static func headTracked(soundStageSize: AVAudioSession.SoundStageSize, anchoringStrategy: AVAudioSession.AnchoringStrategy) -> Self](./avaudiosessionspatialexperience-swift.protocol/headtracked%28soundstagesize,anchoringstrategy%29.md)
- [AVAudioSession.HeadTrackedSpatialExperience](./avaudiosession/headtrackedspatialexperience.md)
  An experience where the sound a size dictated by its sound stage and location dictated by its anchoring strategy.
- [static var bypassed: AVAudioSession.BypassedSpatialExperience](./avaudiosessionspatialexperience-swift.protocol/bypassed.md)
- [AVAudioSession.BypassedSpatialExperience](./avaudiosession/bypassedspatialexperience.md)
  An experience that bypasses system-provided audio spatialization.
- [AVAudioSession.SoundStageSize](./avaudiosession/soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [AVAudioSession.AnchoringStrategy](./avaudiosession/anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.

## Relationships

### Conforming Types
- [AVAudioSession.BypassedSpatialExperience](./avaudiosession/bypassedspatialexperience.md)
- [AVAudioSession.FixedSpatialExperience](./avaudiosession/fixedspatialexperience.md)
- [AVAudioSession.HeadTrackedSpatialExperience](./avaudiosession/headtrackedspatialexperience.md)

## See Also

### Configuring the spatial experience
- [var intendedSpatialExperience: any AVAudioSessionSpatialExperience](./avaudiosession/intendedspatialexperience-1bpnq.md)
  The spatial audio experience your app intends to provide the user.
- [func setIntendedSpatialExperience(any AVAudioSessionSpatialExperience) throws](./avaudiosession/setintendedspatialexperience%28_%29.md)
  Sets the spatial audio experience your app intends to provide the user.
- [AVAudioSession.SoundStageSize](./avaudiosession/soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [AVAudioSession.AnchoringStrategy](./avaudiosession/anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.
- [var isNowPlayingCandidate: Bool](./avaudiosession/isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](./avaudiosession/setisnowplayingcandidate%28_%29.md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionspatialexperience-swift.protocol)*