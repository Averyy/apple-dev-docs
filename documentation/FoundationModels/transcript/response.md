# Transcript.Response

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A response from the model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct Response
```

## Topics

### Creating a response
- [init(id: String, assetIDs: [String], segments: [Transcript.Segment])](./response/init%28id,assetids,segments%29.md)
  Creates a response that contains the segments you provide.
- [init(id: String, metadata: [String : any ConvertibleToGeneratedContent], segments: [Transcript.Segment])](./response/init%28id,metadata,segments%29.md)
  Creates a response that contains the metadata and segments you provide.
### Inspecting a response
- [var segments: [Transcript.Segment]](./response/segments.md)
  Ordered response segments.
- [var assetIDs: [String]](./response/assetids.md)
  Version-aware identifiers for all assets used to generate this response.
- [var metadata: [String : GeneratedContent]](./response/metadata.md)
  Metadata associated with generating the response.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
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
- [Transcript.Reasoning](./reasoning.md)
  A reasoning entry from the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/response)*