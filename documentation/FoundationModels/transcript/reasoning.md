# Transcript.Reasoning

**Framework**: Foundation Models  
**Kind**: struct

A reasoning entry from the model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Reasoning
```

## Topics

### Creating a reasoning instance
- [init(id: String, metadata: [String : any ConvertibleToGeneratedContent], segments: [Transcript.Segment], signature: Data?)](transcript/reasoning/init(id:metadata:segments:signature:).md)
### Inspecting the reasoning
- [var description: String](transcript/reasoning/description.md)
- [var metadata: [String : GeneratedContent]](transcript/reasoning/metadata.md)
  Metadata produced by the model while generating this reasoning entry.
- [var segments: [Transcript.Segment]](transcript/reasoning/segments.md)
  Ordered reasoning segments.
- [var signature: Data?](transcript/reasoning/signature.md)
  Opaque producer-supplied signature for this reasoning entry.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Transcript.Entry](transcript/entry.md)
  An entry in a transcript.
- [Transcript.Instructions](transcript/instructions.md)
  Instructions you provide to the model that define its behavior.
- [Transcript.Prompt](transcript/prompt.md)
  A prompt from the user to the model.
- [Transcript.Response](transcript/response.md)
  A response from the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/reasoning)*