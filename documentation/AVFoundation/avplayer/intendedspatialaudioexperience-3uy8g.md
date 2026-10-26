# intendedSpatialAudioExperience

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The AVPlayer’s intended spatial audio experience.

**Availability**:
- visionOS 26.0+

## Declaration

```objc
@property (nonatomic, copy) CASpatialAudioExperience * intendedSpatialAudioExperience;
```

#### Discussion

The default value of CAAutomaticSpatialAudio means the player uses its AVAudioSession’s intended spatial experience. If the anchoring strategy is impossible (e.g. it uses a destroyed UIScene’s identifier), the player follows a “front” anchoring strategy instead.

## See Also

### Configuring audio behavior
- [var volume: Float](./volume.md)
  The audio playback volume for the player.
- [var isMuted: Bool](./ismuted.md)
  A Boolean value that indicates whether the audio output of the player is muted.
- [var allowedAudioSpatializationFormats: AVAudioSpatializationFormats](../avplayeritem/allowedaudiospatializationformats.md)
  The source audio channel layouts the player item supports for spatialization.
- [var isAudioSpatializationAllowed: Bool](../avplayeritem/isaudiospatializationallowed.md)
  A Boolean value that indicates whether the player item allows spatialized audio playback.
- [var audioOutputSuppressedDueToNonMixableAudioRoute: Bool](./audiooutputsuppressedduetononmixableaudioroute.md)
  Whether the player’s audio output is suppressed due to being on a non-mixable audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/intendedspatialaudioexperience-3uy8g)*