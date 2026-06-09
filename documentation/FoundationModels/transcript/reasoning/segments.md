# segments

**Framework**: Foundation Models  
**Kind**: property

Ordered reasoning segments.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var segments: [Transcript.Segment]
```

#### Discussion

May be empty or a partial/summary representation; full text may not be available when `signature` is non-nil.

## See Also

- [var description: String](transcript/reasoning/description.md)
- [var metadata: [String : any Codable & Sendable & Equatable]](transcript/reasoning/metadata.md)
  Metadata produced by the model while generating this reasoning entry.
- [var signature: Data?](transcript/reasoning/signature.md)
  Opaque producer-supplied signature for this reasoning entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/reasoning/segments)*