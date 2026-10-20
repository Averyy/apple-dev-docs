# AVAudioSession.SoundStageSize

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the perceived size of sounds the audio session plays.

**Availability**:
- visionOS

## Declaration

```swift
enum SoundStageSize
```

```c
enum AVAudioSessionSoundStageSize : NSInteger;
```

## Topics

### Creating a sound stage size
- [init?(rawValue: Int)](./soundstagesize/init%28rawvalue%29.md)
### Choosing a sound stage size
- [AVAudioSession.SoundStageSize.automatic](./soundstagesize/automatic.md)
  The system sets the sound stage size.
- [AVAudioSession.SoundStageSize.small](./soundstagesize/small.md)
  A small sound stage.
- [AVAudioSession.SoundStageSize.medium](./soundstagesize/medium.md)
  A medium sound stage.
- [AVAudioSession.SoundStageSize.large](./soundstagesize/large.md)
  A large sound stage.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the spatial experience
- [var intendedSpatialExperience: any AVAudioSessionSpatialExperience](./intendedspatialexperience-1bpnq.md)
  The spatial audio experience your app intends to provide the user.
- [func setIntendedSpatialExperience(any AVAudioSessionSpatialExperience) throws](./setintendedspatialexperience%28_%29.md)
  Sets the spatial audio experience your app intends to provide the user.
- [protocol AVAudioSessionSpatialExperience](../avaudiosessionspatialexperience-swift.protocol.md)
- [AVAudioSession.AnchoringStrategy](./anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.
- [var isNowPlayingCandidate: Bool](./isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](./setisnowplayingcandidate%28_%29.md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/soundstagesize)*