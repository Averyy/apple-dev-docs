# generate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A video composition may generate HDR metadata and attach it to the rendered frame.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let generate: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy
```

```c
extern AVVideoCompositionPerFrameHDRDisplayMetadataPolicy const AVVideoCompositionPerFrameHDRDisplayMetadataPolicyGenerate;
```

#### Discussion

HDR metadata generation is influenced by the color space of the rendered frame, device, and HDR metadata format platform support. Any previously attached HDR metadata of the same metadata format is overwritten.

## See Also

### Policies
- [static let propagate: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](./propagate.md)
  A policy that passes HDR metadata through, if present on the composed frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct/generate)*