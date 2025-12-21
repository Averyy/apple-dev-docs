# intendedSpatialAudioExperience

**Framework**: AVFoundation  
**Kind**: property

The player’s intended Spatial Audio experience.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
var intendedSpatialAudioExperience: any SpatialAudioExperience { get set }
```

#### Discussion

If unspecified, the property value defaults to [`CAAutomaticSpatialAudio`](https://developer.apple.com/documentation/AudioToolbox/CAAutomaticSpatialAudio).

## See Also

- [var volume: Float](avplayer/volume.md)
  The audio playback volume for the player.
- [var isMuted: Bool](avplayer/ismuted.md)
  A Boolean value that indicates whether the audio output of the player is muted.
- [var allowedAudioSpatializationFormats: AVAudioSpatializationFormats](avplayeritem/allowedaudiospatializationformats.md)
  The source audio channel layouts the player item supports for spatialization.
- [var isAudioSpatializationAllowed: Bool](avplayeritem/isaudiospatializationallowed.md)
  A Boolean value that indicates whether the player item allows spatialized audio playback.
- [var audioOutputSuppressedDueToNonMixableAudioRoute: Bool](avplayer/audiooutputsuppressedduetononmixableaudioroute.md)
  Whether the player’s audio output is suppressed due to being on a non-mixable audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/intendedspatialaudioexperience-1bd87)*