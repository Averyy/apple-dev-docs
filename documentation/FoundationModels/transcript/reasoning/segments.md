# segments

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

Ordered reasoning segments.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var segments: [Transcript.Segment]
```

## Discussion

May be empty or a partial/summary representation; full text may not be available when `signature` is non-nil.

## See Also

### Inspecting the reasoning
- [var description: String](./description.md)
  A textual representation of the reasoning entry.
- [var metadata: [String : GeneratedContent]](./metadata.md)
  Metadata produced by the model while generating this reasoning entry.
- [var signature: Data?](./signature.md)
  Opaque producer-supplied signature for this reasoning entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/reasoning/segments)*