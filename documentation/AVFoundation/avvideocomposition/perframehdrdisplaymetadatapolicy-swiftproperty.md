# perFrameHDRDisplayMetadataPolicy

**Framework**: AVFoundation  
**Kind**: property

The policy for display of HDR display metadata on the rendered frame.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy { get }
```

#### Discussion

Allows the system to identify situations where it can generate HDR metadata and attach it to the rendered video frame.

The default value is [`propagate`](avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct/propagate.md), which indicates the system propagates any HDR metadata attached to the composed frame to the rendered video frames.

## See Also

- [AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct.md)
  A type that defines the policy for handling of per frame HDR metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.property)*