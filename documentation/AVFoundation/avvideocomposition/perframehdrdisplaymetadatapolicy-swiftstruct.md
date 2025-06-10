# AVVideoComposition.PerFrameHDRDisplayMetadataPolicy

**Framework**: AVFoundation  
**Kind**: struct

A type that defines the policy for handling of per frame HDR metadata.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct PerFrameHDRDisplayMetadataPolicy
```

#### Discussion

Use this type to specify what HDR display metadata to attach to the rendered frame.

## Topics

### Policies
- [static let propagate: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct/propagate.md)
  A policy that passes HDR metadata through, if present on the composed frame.
- [static let generate: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct/generate.md)
  A video composition may generate HDR metadata and attach it to the rendered frame.
### Initializers
- [init(rawValue: String)](avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct/init(rawvalue:).md)
  Creates a policy with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](avmutablevideocomposition/perframehdrdisplaymetadatapolicy.md)
  Configures the policy for display of HDR display metadata on the rendered frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct)*