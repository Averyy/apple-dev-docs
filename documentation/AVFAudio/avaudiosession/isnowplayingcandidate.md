# isNowPlayingCandidate

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var isNowPlayingCandidate: Bool { get }
```

```objc
@property (readonly) BOOL isNowPlayingCandidate;
```

#### Discussion

Only a single audio session for an app can be a Now Playing candidate. Designating multiple audio sessions for the same app as Now Playing candidates results in none of them being eligible.

## See Also

### Configuring the spatial experience
- [var intendedSpatialExperience: any AVAudioSessionSpatialExperience](./intendedspatialexperience-1bpnq.md)
  The spatial audio experience your app intends to provide the user.
- [func setIntendedSpatialExperience(any AVAudioSessionSpatialExperience) throws](./setintendedspatialexperience%28_%29.md)
  Sets the spatial audio experience your app intends to provide the user.
- [protocol AVAudioSessionSpatialExperience](../avaudiosessionspatialexperience-swift.protocol.md)
- [AVAudioSession.SoundStageSize](./soundstagesize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [AVAudioSession.AnchoringStrategy](./anchoringstrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.
- [func setIsNowPlayingCandidate(Bool) throws](./setisnowplayingcandidate%28_%29.md)
  Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [intendedSpatialExperience](./intendedspatialexperience-qlty.md)
  The spatial audio experience your app intends to provide the user.
- [- setIntendedSpatialExperience:options:error:](./setintendedspatialexperience_options_error_.md)
  Sets the spatial audio experience your app intends to provide the user.
- [AVAudioSessionSpatialExperience](../avaudiosessionspatialexperience-c.enum.md)
- [intendedSpatialExperienceOptions](./intendedspatialexperienceoptions.md)
  A dictionary of options that customize the spatial experience.
- [AVAudioSessionSpatialExperienceOption](../avaudiosessionspatialexperienceoption.md)
  A key that configures one characteristic of a spatial experience, such as its sound stage size or anchoring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/isnowplayingcandidate)*