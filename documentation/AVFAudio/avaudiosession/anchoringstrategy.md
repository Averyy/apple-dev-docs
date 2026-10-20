# AVAudioSession.AnchoringStrategy

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that specify how to set the origin of audio in a head-tracked spatial experience.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum AnchoringStrategy
```

## Topics

### Anchoring strategies
- [AVAudioSession.AnchoringStrategy.automatic](./anchoringstrategy/automatic.md)
  The system determines the anchoring strategy.
- [AVAudioSession.AnchoringStrategy.front](./anchoringstrategy/front.md)
  The audio session anchors to a person’s concept of front.
- [AVAudioSession.AnchoringStrategy.scene(identifier:)](./anchoringstrategy/scene%28identifier%29.md)
  The audio session anchors to a scene.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the spatial experience
- [var intendedSpatialExperience: any AVAudioSessionSpatialExperience](./intendedspatialexperience-1bpnq.md)
  The spatial audio experience your app intends to provide the user.
- [func setIntendedSpatialExperience(any AVAudioSessionSpatialExperience) throws](./setintendedspatialexperience%28_%29.md)
  Sets the spatial audio experience your app intends to provide the user.
- [protocol AVAudioSessionSpatialExperience](../avaudiosessionspatialexperience-swift.protocol.md)
- [AVAudioSession.SoundStageSize](./soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [var isNowPlayingCandidate: Bool](./isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](./setisnowplayingcandidate%28_%29.md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/anchoringstrategy)*