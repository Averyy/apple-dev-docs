# AVAudio3DMixingSourceMode.spatializeIfMono

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

A mono input bus that renders as a point source at the location of the source node.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case spatializeIfMono
```

```c
AVAudio3DMixingSourceModeSpatializeIfMono
```

#### Discussion

The system bypasses an input bus with more than one channel. This is equivalent to [`AVAudio3DMixingSourceMode.pointSource`](./pointsource.md) for a mono bus and [`AVAudio3DMixingSourceMode.bypass`](./bypass.md) for a bus with more than one channel.

## See Also

### Choosing a source mode
- [AVAudio3DMixingSourceMode.bypass](./bypass.md)
  A mode that does no spatial rendering.
- [AVAudio3DMixingSourceMode.pointSource](./pointsource.md)
  All channels of the bus render as a single source at the location of the source node.
- [AVAudio3DMixingSourceMode.ambienceBed](./ambiencebed.md)
  The input channels spread around the listener as far-field sources that anchor to global space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingsourcemode/spatializeifmono)*