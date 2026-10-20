# propagate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A policy that passes HDR metadata through, if present on the composed frame.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let propagate: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy
```

```c
extern AVVideoCompositionPerFrameHDRDisplayMetadataPolicy const AVVideoCompositionPerFrameHDRDisplayMetadataPolicyPropagate;
```

## See Also

### Policies
- [static let generate: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](./generate.md)
  A video composition may generate HDR metadata and attach it to the rendered frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct/propagate)*