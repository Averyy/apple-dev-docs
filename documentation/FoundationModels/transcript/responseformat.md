# Transcript.ResponseFormat

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A response format that the model must conform its output to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct ResponseFormat
```

## Topics

### Creating a response format
- [init(schema: GenerationSchema)](./responseformat/init%28schema%29.md)
  Creates a response format with a schema.
- [init<Content>(type: Content.Type)](./responseformat/init%28type%29.md)
  Creates a response format with type you specify.
### Inspecting the name
- [var name: String](./responseformat/name.md)
  A name associated with the response format.
### Accessing the kind of format
- [let kind: Transcript.ResponseFormat.Kind](./responseformat/kind-swift.property.md)
  The way the response format constrains the model’s output.
- [Transcript.ResponseFormat.Kind](./responseformat/kind-swift.enum.md)
  A representation of the different ways a response format can constrain model output.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/responseformat)*