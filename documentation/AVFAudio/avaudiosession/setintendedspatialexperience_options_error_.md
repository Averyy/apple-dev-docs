# setIntendedSpatialExperience:options:error:

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sets the spatial audio experience your app intends to provide the user.

**Availability**:
- visionOS 1.0+

## Declaration

```objc
- (BOOL) setIntendedSpatialExperience:(AVAudioSessionSpatialExperience) intendedSpatialExperience options:(NSDictionary<NSString *,id> *) options error:(NSError **) error;
```

## Parameters

- `intendedSpatialExperience`: The spatial audio experience to set.
- `options`: A dictionary of options that customize the experience.
- `error`: If an error occurs, an object that provides the details of the error.

## Topics

### Spatial experience options
- [AVAudioSessionSpatialExperienceOptionAnchoringStrategy](../avaudiosessionspatialexperienceoptionanchoringstrategy.md)
  An option that sets where the audio anchors in a head-tracked spatial experience.
- [AVAudioSessionSpatialExperienceOptionSceneIdentifier](../avaudiosessionspatialexperienceoptionsceneidentifier.md)
  An option that identifies the scene the audio anchors to.
- [AVAudioSessionSpatialExperienceOptionSoundStageSize](../avaudiosessionspatialexperienceoptionsoundstagesize.md)
  An option that sets how large the sound stage is in a spatial experience.
- [AVAudioSessionSpatialExperienceOption](../avaudiosessionspatialexperienceoption.md)
  A key that configures one characteristic of a spatial experience, such as its sound stage size or anchoring.

## See Also

### Configuring the spatial experience
- [intendedSpatialExperience](./intendedspatialexperience-qlty.md)
  The spatial audio experience your app intends to provide the user.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setintendedspatialexperience:options:error:)*