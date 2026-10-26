# intendedSpatialExperience

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The spatial audio experience your app intends to provide the user.

**Availability**:
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) AVAudioSessionSpatialExperience intendedSpatialExperience;
```

## See Also

### Configuring the spatial experience
- [- setIntendedSpatialExperience:options:error:](./setintendedspatialexperience_options_error_.md)
  Sets the spatial audio experience your app intends to provide the user.
- [AVAudioSessionSpatialExperience](../avaudiosessionspatialexperience-c.enum.md)
- [AVAudioSession.SoundStageSize](./soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [intendedSpatialExperienceOptions](./intendedspatialexperienceoptions.md)
  A dictionary of options that customize the spatial experience.
- [AVAudioSessionSpatialExperienceOption](../avaudiosessionspatialexperienceoption.md)
  A key that configures one characteristic of a spatial experience, such as its sound stage size or anchoring.
- [var isNowPlayingCandidate: Bool](./isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](./setisnowplayingcandidate%28_%29.md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/intendedspatialexperience-qlty)*