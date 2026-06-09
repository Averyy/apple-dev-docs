# signature

**Framework**: Foundation Models  
**Kind**: property

Opaque producer-supplied signature for this reasoning entry.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var signature: Data?
```

#### Discussion

When this is non-nil, `segments` may represent a partial summary or be empty; full reasoning text may not be available.

## See Also

- [var description: String](transcript/reasoning/description.md)
- [var metadata: [String : any Codable & Sendable & Equatable]](transcript/reasoning/metadata.md)
  Metadata produced by the model while generating this reasoning entry.
- [var segments: [Transcript.Segment]](transcript/reasoning/segments.md)
  Ordered reasoning segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/reasoning/signature)*