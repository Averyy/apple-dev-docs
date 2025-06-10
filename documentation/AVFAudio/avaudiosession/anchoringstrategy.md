# AVAudioSession.AnchoringStrategy

**Framework**: AVFAudio  
**Kind**: enum

Constants that specify how to set the origin of audio in a head-tracked spatial experience.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum AnchoringStrategy
```

## Topics

### Anchoring strategies
- [AVAudioSession.AnchoringStrategy.automatic](avaudiosession/anchoringstrategy/automatic.md)
  The system determines the anchoring strategy.
- [AVAudioSession.AnchoringStrategy.front](avaudiosession/anchoringstrategy/front.md)
  The audio session anchors to a person’s concept of front.
- [AVAudioSession.AnchoringStrategy.scene(identifier:)](avaudiosession/anchoringstrategy/scene(identifier:).md)
  The audio session anchors to a scene.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setIntendedSpatialExperience(any AVAudioSessionSpatialExperience) throws](avaudiosession/setintendedspatialexperience(_:).md)
  Sets the spatial audio experience your app intends to provide the user.
- [protocol AVAudioSessionSpatialExperience](../AVFoundation/AVAudioSessionSpatialExperience.md)
  A protocol that defines types of spatial audio experiences that the system supports.
- [AVAudioSession.HeadTrackedSpatialExperience](avaudiosession/headtrackedspatialexperience.md)
  An experience where the sound a size dictated by its sound stage and location dictated by its anchoring strategy.
- [AVAudioSession.FixedSpatialExperience](avaudiosession/fixedspatialexperience.md)
  An experience where the sound has a size dictated by its sound stage and is head-locked relative to the user.
- [AVAudioSession.BypassedSpatialExperience](avaudiosession/bypassedspatialexperience.md)
  An experience that bypasses system-provided audio spatialization.
- [AVAudioSession.SoundStageSize](avaudiosession/soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [var isNowPlayingCandidate: Bool](avaudiosession/isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](avaudiosession/setisnowplayingcandidate(_:).md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/anchoringstrategy)*