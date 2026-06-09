# metadata

**Framework**: Foundation Models  
**Kind**: property

Metadata produced by the model while generating this reasoning entry.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var metadata: [String : any Codable & Sendable & Equatable]
```

## See Also

- [var description: String](transcript/reasoning/description.md)
- [var segments: [Transcript.Segment]](transcript/reasoning/segments.md)
  Ordered reasoning segments.
- [var signature: Data?](transcript/reasoning/signature.md)
  Opaque producer-supplied signature for this reasoning entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/reasoning/metadata)*