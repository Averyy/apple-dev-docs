# isAudioSpatializationAllowed

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player item allows spatialized audio playback.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0

> **Deprecated**: Use [`allowedAudioSpatializationFormats`](./allowedaudiospatializationformats.md) instead.

## Declaration

```swift
var isAudioSpatializationAllowed: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isAudioSpatializationAllowed) BOOL audioSpatializationAllowed;
```

## See Also

### Configuring audio behavior
- [var volume: Float](../avplayer/volume.md)
  The audio playback volume for the player.
- [var isMuted: Bool](../avplayer/ismuted.md)
  A Boolean value that indicates whether the audio output of the player is muted.
- [var allowedAudioSpatializationFormats: AVAudioSpatializationFormats](./allowedaudiospatializationformats.md)
  The source audio channel layouts the player item supports for spatialization.
- [var audioOutputSuppressedDueToNonMixableAudioRoute: Bool](../avplayer/audiooutputsuppressedduetononmixableaudioroute.md)
  Whether the player’s audio output is suppressed due to being on a non-mixable audio route.
- [var intendedSpatialAudioExperience: any SpatialAudioExperience](../avplayer/intendedspatialaudioexperience-1bd87.md)
  The player’s intended Spatial Audio experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/isaudiospatializationallowed)*