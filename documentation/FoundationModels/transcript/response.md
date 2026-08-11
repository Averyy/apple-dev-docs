# Transcript.Response

**Framework**: Foundation Models  
**Kind**: struct

A response from the model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Response
```

## Topics

### Creating a response
- [init(id: String, assetIDs: [String], segments: [Transcript.Segment])](transcript/response/init(id:assetids:segments:).md)
- [init(id: String, metadata: [String : any ConvertibleToGeneratedContent], segments: [Transcript.Segment])](transcript/response/init(id:metadata:segments:).md)
### Inspecting a response
- [var segments: [Transcript.Segment]](transcript/response/segments.md)
  Ordered prompt segments.
- [var assetIDs: [String]](transcript/response/assetids.md)
  Version aware identifiers for all assets used to generate this response.
- [var metadata: [String : GeneratedContent]](transcript/response/metadata.md)
  Metadata associated with generating the response.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
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
- [Transcript.Reasoning](transcript/reasoning.md)
  A reasoning entry from the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/response)*