# Transcript.Reasoning

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A reasoning entry from the model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Reasoning
```

## Topics

### Creating a reasoning instance
- [init(id: String, metadata: [String : any ConvertibleToGeneratedContent], segments: [Transcript.Segment], signature: Data?)](./reasoning/init%28id,metadata,segments,signature%29.md)
  Creates a reasoning entry that contains the segments you provide.
### Inspecting the reasoning
- [var description: String](./reasoning/description.md)
  A textual representation of the reasoning entry.
- [var metadata: [String : GeneratedContent]](./reasoning/metadata.md)
  Metadata produced by the model while generating this reasoning entry.
- [var segments: [Transcript.Segment]](./reasoning/segments.md)
  Ordered reasoning segments.
- [var signature: Data?](./reasoning/signature.md)
  Opaque producer-supplied signature for this reasoning entry.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Transcript entries
- [Transcript.Entry](./entry.md)
  An entry in a transcript.
- [Transcript.Instructions](./instructions.md)
  Instructions you provide to the model that define its behavior.
- [Transcript.Prompt](./prompt.md)
  A prompt from the user to the model.
- [Transcript.Response](./response.md)
  A response from the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/reasoning)*