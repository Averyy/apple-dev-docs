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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var intendedSpatialExperience: any AVAudioSessionSpatialExperience](avaudiosession/intendedspatialexperience-1bpnq.md)
  The spatial audio experience your app intends to provide the user.
- [func setIntendedSpatialExperience(any AVAudioSessionSpatialExperience) throws](avaudiosession/setintendedspatialexperience(_:).md)
  Sets the spatial audio experience your app intends to provide the user.
- [protocol AVAudioSessionSpatialExperience](avaudiosessionspatialexperience-swift.protocol.md)
- [AVAudioSession.AnchoringStrategy](avaudiosession/anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.
- [var isNowPlayingCandidate: Bool](avaudiosession/isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](avaudiosession/setisnowplayingcandidate(_:).md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/soundstagesize)*