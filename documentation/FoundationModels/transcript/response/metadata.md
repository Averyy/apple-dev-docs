# metadata

**Framework**: Foundation Models  
**Kind**: property

Metadata associated with generating the response.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, visionOS 27.0)
var metadata: [String : GeneratedContent] { get }
```

## See Also

- [var segments: [Transcript.Segment]](transcript/response/segments.md)
  Ordered prompt segments.
- [var assetIDs: [String]](transcript/response/assetids.md)
  Version aware identifiers for all assets used to generate this response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/response/metadata)*