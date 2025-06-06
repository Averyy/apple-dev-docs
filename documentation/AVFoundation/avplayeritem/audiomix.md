# audioMix

**Framework**: AVFoundation  
**Kind**: property

The audio mix parameters to be applied during playback.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@NSCopying
@MainActor var audioMix: AVAudioMix? { get set }
```

#### Discussion

An audio mix can only be used with file-based media and is not supported for use with media served using HTTP Live Streaming.

## See Also

- [var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm](avplayeritem/audiotimepitchalgorithm.md)
  The processing algorithm used to manage audio pitch for scaled audio edits.
- [var allowedAudioSpatializationFormats: AVAudioSpatializationFormats](avplayeritem/allowedaudiospatializationformats.md)
  The source audio channel layouts the player item supports for spatialization.
- [struct AVAudioSpatializationFormats](avaudiospatializationformats.md)
  A structure that defines the spatialization formats that a player item supports.
- [var isAudioSpatializationAllowed: Bool](avplayeritem/isaudiospatializationallowed.md)
  A Boolean value that indicates whether the player item allows spatialized audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/audiomix)*