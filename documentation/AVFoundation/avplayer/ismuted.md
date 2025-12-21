# isMuted

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the audio output of the player is muted.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
var isMuted: Bool { get set }
```

## See Also

- [var volume: Float](avplayer/volume.md)
  The audio playback volume for the player.
- [var allowedAudioSpatializationFormats: AVAudioSpatializationFormats](avplayeritem/allowedaudiospatializationformats.md)
  The source audio channel layouts the player item supports for spatialization.
- [var isAudioSpatializationAllowed: Bool](avplayeritem/isaudiospatializationallowed.md)
  A Boolean value that indicates whether the player item allows spatialized audio playback.
- [var audioOutputSuppressedDueToNonMixableAudioRoute: Bool](avplayer/audiooutputsuppressedduetononmixableaudioroute.md)
  Whether the player’s audio output is suppressed due to being on a non-mixable audio route.
- [var intendedSpatialAudioExperience: any SpatialAudioExperience](avplayer/intendedspatialaudioexperience-1bd87.md)
  The player’s intended Spatial Audio experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/ismuted)*