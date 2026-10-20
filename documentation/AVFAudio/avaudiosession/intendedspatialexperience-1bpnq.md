# intendedSpatialExperience

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The spatial audio experience your app intends to provide the user.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@nonobjc
var intendedSpatialExperience: any AVAudioSessionSpatialExperience { get }
```

## See Also

### Configuring the spatial experience
- [func setIntendedSpatialExperience(any AVAudioSessionSpatialExperience) throws](./setintendedspatialexperience%28_%29.md)
  Sets the spatial audio experience your app intends to provide the user.
- [protocol AVAudioSessionSpatialExperience](../avaudiosessionspatialexperience-swift.protocol.md)
- [AVAudioSession.SoundStageSize](./soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [AVAudioSession.AnchoringStrategy](./anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.
- [var isNowPlayingCandidate: Bool](./isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](./setisnowplayingcandidate%28_%29.md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/intendedspatialexperience-1bpnq)*