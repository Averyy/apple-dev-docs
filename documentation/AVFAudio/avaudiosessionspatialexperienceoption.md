# AVAudioSessionSpatialExperienceOption

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

A key that configures one characteristic of a spatial experience, such as its sound stage size or anchoring.

**Availability**:
- visionOS

## Declaration

```c
typedef NSString * const AVAudioSessionSpatialExperienceOption;
```

## Topics

### Option keys
- [AVAudioSessionSpatialExperienceOptionAnchoringStrategy](./avaudiosessionspatialexperienceoptionanchoringstrategy.md)
  An option that sets where the audio anchors in a head-tracked spatial experience.
- [AVAudioSessionSpatialExperienceOptionSceneIdentifier](./avaudiosessionspatialexperienceoptionsceneidentifier.md)
  An option that identifies the scene the audio anchors to.
- [AVAudioSessionSpatialExperienceOptionSoundStageSize](./avaudiosessionspatialexperienceoptionsoundstagesize.md)
  An option that sets how large the sound stage is in a spatial experience.

## See Also

### Configuring the spatial experience
- [intendedSpatialExperience](./avaudiosession/intendedspatialexperience-qlty.md)
  The spatial audio experience your app intends to provide the user.
- [- setIntendedSpatialExperience:options:error:](./avaudiosession/setintendedspatialexperience_options_error_.md)
  Sets the spatial audio experience your app intends to provide the user.
- [AVAudioSessionSpatialExperience](./avaudiosessionspatialexperience-c.enum.md)
- [AVAudioSession.SoundStageSize](./avaudiosession/soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [intendedSpatialExperienceOptions](./avaudiosession/intendedspatialexperienceoptions.md)
  A dictionary of options that customize the spatial experience.
- [var isNowPlayingCandidate: Bool](./avaudiosession/isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [func setIsNowPlayingCandidate(Bool) throws](./avaudiosession/setisnowplayingcandidate%28_%29.md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionspatialexperienceoption)*