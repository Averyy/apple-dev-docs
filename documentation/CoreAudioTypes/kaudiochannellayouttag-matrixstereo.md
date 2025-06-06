# kAudioChannelLayoutTag_MatrixStereo

**Framework**: Core Audio Types  
**Kind**: var

A matrix-encoded stereo stream.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var kAudioChannelLayoutTag_MatrixStereo: AudioChannelLayoutTag { get }
```

#### Discussion

Your channels must be laid out in the following order:

- Left matrix total
- Right matrix total

## See Also

- [var kAudioChannelLayoutTag_UseChannelDescriptions: AudioChannelLayoutTag](kaudiochannellayouttag_usechanneldescriptions.md)
  An array of audio channel description structures that defines the layout mapping.
- [var kAudioChannelLayoutTag_UseChannelBitmap: AudioChannelLayoutTag](kaudiochannellayouttag_usechannelbitmap.md)
  A bitmap that defines the layout mapping.
- [var kAudioChannelLayoutTag_Mono: AudioChannelLayoutTag](kaudiochannellayouttag_mono.md)
  A standard monophonic stream.
- [var kAudioChannelLayoutTag_Stereo: AudioChannelLayoutTag](kaudiochannellayouttag_stereo.md)
  A standard stereophonic stream.
- [var kAudioChannelLayoutTag_StereoHeadphones: AudioChannelLayoutTag](kaudiochannellayouttag_stereoheadphones.md)
  A standard stereo stream; headphone playback implied.
- [var kAudioChannelLayoutTag_MidSide: AudioChannelLayoutTag](kaudiochannellayouttag_midside.md)
  A middle and side channel audio layout.
- [var kAudioChannelLayoutTag_XY: AudioChannelLayoutTag](kaudiochannellayouttag_xy.md)
  A coincident, angled microphone pair.
- [var kAudioChannelLayoutTag_Binaural: AudioChannelLayoutTag](kaudiochannellayouttag_binaural.md)
  A binaural stereo audio layout.
- [var kAudioChannelLayoutTag_Ambisonic_B_Format: AudioChannelLayoutTag](kaudiochannellayouttag_ambisonic_b_format.md)
  An ambisonic B-format audio layout.
- [var kAudioChannelLayoutTag_Quadraphonic: AudioChannelLayoutTag](kaudiochannellayouttag_quadraphonic.md)
  A quadraphonic audio layout.
- [var kAudioChannelLayoutTag_Pentagonal: AudioChannelLayoutTag](kaudiochannellayouttag_pentagonal.md)
  A pentalgonal audio layout.
- [var kAudioChannelLayoutTag_Hexagonal: AudioChannelLayoutTag](kaudiochannellayouttag_hexagonal.md)
  A hexagonal audio layout.
- [var kAudioChannelLayoutTag_Octagonal: AudioChannelLayoutTag](kaudiochannellayouttag_octagonal.md)
  An octagonal audio layout.
- [var kAudioChannelLayoutTag_Cube: AudioChannelLayoutTag](kaudiochannellayouttag_cube.md)
  A cubic audio layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/kaudiochannellayouttag_matrixstereo)*