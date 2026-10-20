# metadata

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

Metadata produced by the model while generating this reasoning entry.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var metadata: [String : GeneratedContent]
```

## See Also

### Inspecting the reasoning
- [var description: String](./description.md)
  A textual representation of the reasoning entry.
- [var segments: [Transcript.Segment]](./segments.md)
  Ordered reasoning segments.
- [var signature: Data?](./signature.md)
  Opaque producer-supplied signature for this reasoning entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/reasoning/metadata)*