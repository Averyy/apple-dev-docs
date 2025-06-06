# AVAudioSession.SoundStageSize

**Framework**: AVFAudio  
**Kind**: enum

Constants that specify the perceived size of sounds the audio session plays.

**Availability**:
- visionOS ?+

## Declaration

```swift
enum SoundStageSize
```

## Topics

### Sound stage sizes
- [AVAudioSession.SoundStageSize.automatic](avaudiosession/soundstagesize/automatic.md)
  The system sets the sound stage size.
- [AVAudioSession.SoundStageSize.small](avaudiosession/soundstagesize/small.md)
  A small sound stage.
- [AVAudioSession.SoundStageSize.medium](avaudiosession/soundstagesize/medium.md)
  A medium sound stage.
- [AVAudioSession.SoundStageSize.large](avaudiosession/soundstagesize/large.md)
  A large sound stage.
### Initializers
- [init?(rawValue: Int)](avaudiosession/soundstagesize/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func setIntendedSpatialExperience(any AVAudioSessionSpatialExperience) throws](avaudiosession/setintendedspatialexperience(_:).md)
  Sets the spatial audio experience your app intends to provide the user.
- [var intendedSpatialExperience: any AVAudioSessionSpatialExperience](avaudiosession/intendedspatialexperience-1qwbe.md)
  The spatial audio experience your app intends to provide the user.
- [protocol AVAudioSessionSpatialExperience](../AVFoundation/AVAudioSessionSpatialExperience.md)
  A protocol that defines types of spatial audio experiences that the system supports.
- [AVAudioSession.HeadTrackedSpatialExperience](avaudiosession/headtrackedspatialexperience.md)
  An experience where the sound a size dictated by its sound stage and location dictated by its anchoring strategy.
- [AVAudioSession.FixedSpatialExperience](avaudiosession/fixedspatialexperience.md)
  An experience where the sound has a size dictated by its sound stage and is head-locked relative to the user.
- [AVAudioSession.BypassedSpatialExperience](avaudiosession/bypassedspatialexperience.md)
  An experience that bypasses system-provided audio spatialization.
- [AVAudioSession.AnchoringStrategy](avaudiosession/anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.
- [var isNowPlayingCandidate: Bool](avaudiosession/isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](avaudiosession/setisnowplayingcandidate(_:).md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/soundstagesize)*