# volume

**Framework**: AVFoundation  
**Kind**: property

The audio playback volume for the player.

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
var volume: Float { get set }
```

#### Discussion

A value of `0.0` indicates silence; a value of `1.0` (the default) indicates full audio volume for the player instance.

This property is used to control the player audio volume relative to the system volume. There is no programmatic way to control the system volume in iOS, but you can use the MediaPlayer framework’s [`MPVolumeView`](https://developer.apple.com/documentation/MediaPlayer/MPVolumeView) class to present a standard user interface for controlling system volume.

## See Also

- [var isMuted: Bool](avplayer/ismuted.md)
  A Boolean value that indicates whether the audio output of the player is muted.
- [var allowedAudioSpatializationFormats: AVAudioSpatializationFormats](avplayeritem/allowedaudiospatializationformats.md)
  The source audio channel layouts the player item supports for spatialization.
- [var isAudioSpatializationAllowed: Bool](avplayeritem/isaudiospatializationallowed.md)
  A Boolean value that indicates whether the player item allows spatialized audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/volume)*