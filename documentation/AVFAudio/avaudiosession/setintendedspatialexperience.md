# setIntendedSpatialExperience(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets the spatial audio experience your app intends to provide the user.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@nonobjc
func setIntendedSpatialExperience(_ spatialExperience: any AVAudioSessionSpatialExperience) throws
```

#### Discussion

- spatialExperience: The spatial audio experience to set.

## See Also

- [var intendedSpatialExperience: any AVAudioSessionSpatialExperience](avaudiosession/intendedspatialexperience-1bpnq.md)
  The spatial audio experience your app intends to provide the user.
- [protocol AVAudioSessionSpatialExperience](avaudiosessionspatialexperience-swift.protocol.md)
- [AVAudioSession.SoundStageSize](avaudiosession/soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [AVAudioSession.AnchoringStrategy](avaudiosession/anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.
- [var isNowPlayingCandidate: Bool](avaudiosession/isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](avaudiosession/setisnowplayingcandidate(_:).md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setintendedspatialexperience(_:))*