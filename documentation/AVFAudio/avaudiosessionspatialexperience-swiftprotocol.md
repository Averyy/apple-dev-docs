# AVAudioSessionSpatialExperience

**Framework**: AVFAudio  
**Kind**: protocol

**Availability**:
- visionOS 1.0+

## Declaration

```swift
protocol AVAudioSessionSpatialExperience
```

## Topics

### Experiences
- [static func fixed(soundStageSize: AVAudioSession.SoundStageSize) -> Self](avaudiosessionspatialexperience-swift.protocol/fixed(soundstagesize:).md)
- [static func headTracked(soundStageSize: AVAudioSession.SoundStageSize, anchoringStrategy: AVAudioSession.AnchoringStrategy) -> Self](avaudiosessionspatialexperience-swift.protocol/headtracked(soundstagesize:anchoringstrategy:).md)
- [static var bypassed: AVAudioSession.BypassedSpatialExperience](avaudiosessionspatialexperience-swift.protocol/bypassed.md)
- [AVAudioSession.SoundStageSize](avaudiosession/soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [AVAudioSession.AnchoringStrategy](avaudiosession/anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.

## Relationships

### Conforming Types
- [AVAudioSession.BypassedSpatialExperience](avaudiosession/bypassedspatialexperience.md)
- [AVAudioSession.FixedSpatialExperience](avaudiosession/fixedspatialexperience.md)
- [AVAudioSession.HeadTrackedSpatialExperience](avaudiosession/headtrackedspatialexperience.md)

## See Also

- [var intendedSpatialExperience: any AVAudioSessionSpatialExperience](avaudiosession/intendedspatialexperience-1bpnq.md)
  The spatial audio experience your app intends to provide the user.
- [func setIntendedSpatialExperience(any AVAudioSessionSpatialExperience) throws](avaudiosession/setintendedspatialexperience(_:).md)
  Sets the spatial audio experience your app intends to provide the user.
- [var isNowPlayingCandidate: Bool](avaudiosession/isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](avaudiosession/setisnowplayingcandidate(_:).md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionspatialexperience-swift.protocol)*