# AVAudio3DMixingSourceMode.ambienceBed

**Framework**: AVFAudio  
**Kind**: case

The input channels spread around the listener as far-field sources that anchor to global space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case ambienceBed
```

#### Discussion

The rendering depends on listener orientation, but not on listener position. The audio channel layout of the bus specifies the directions of the input channels. The direction of the source node controls the rotation of the bed in the global space.

## See Also

- [AVAudio3DMixingSourceMode.spatializeIfMono](avaudio3dmixingsourcemode/spatializeifmono.md)
  A mono input bus that renders as a point source at the location of the source node.
- [AVAudio3DMixingSourceMode.bypass](avaudio3dmixingsourcemode/bypass.md)
  A mode that does no spatial rendering.
- [AVAudio3DMixingSourceMode.pointSource](avaudio3dmixingsourcemode/pointsource.md)
  All channels of the bus render as a single source at the location of the source node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingsourcemode/ambiencebed)*