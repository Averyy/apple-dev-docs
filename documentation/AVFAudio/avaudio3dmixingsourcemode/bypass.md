# AVAudio3DMixingSourceMode.bypass

**Framework**: AVFAudio  
**Kind**: case

A mode that does no spatial rendering.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case bypass
```

#### Discussion

If input and output audio channel layouts are equivalent, the framework copies all input channels directly to corresponding output channels. If the input and output audio channel layouts differ, the framework mixes according to the [`kAudioFormatProperty_MatrixMixMap`](https://developer.apple.com/documentation/AudioToolbox/kAudioFormatProperty_MatrixMixMap) property of the layouts. It applies no occlusion, obstruction, or reverb in this mode.

## See Also

- [AVAudio3DMixingSourceMode.spatializeIfMono](avaudio3dmixingsourcemode/spatializeifmono.md)
  A mono input bus that renders as a point source at the location of the source node.
- [AVAudio3DMixingSourceMode.pointSource](avaudio3dmixingsourcemode/pointsource.md)
  All channels of the bus render as a single source at the location of the source node.
- [AVAudio3DMixingSourceMode.ambienceBed](avaudio3dmixingsourcemode/ambiencebed.md)
  The input channels spread around the listener as far-field sources that anchor to global space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingsourcemode/bypass)*