# Transcript.ResponseFormat

**Framework**: Foundation Models  
**Kind**: struct

A response format that the model must conform its output to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ResponseFormat
```

## Topics

### Creating a response format
- [init(schema: GenerationSchema)](transcript/responseformat/init(schema:).md)
  Creates a response format with a schema.
- [init<Content>(type: Content.Type)](transcript/responseformat/init(type:).md)
  Creates a response format with type you specify.
### Inspecting the name
- [var name: String](transcript/responseformat/name.md)
  A name associated with the response format.
### Accessing the kind of format
- [let kind: Transcript.ResponseFormat.Kind](transcript/responseformat/kind-swift.property.md)
- [Transcript.ResponseFormat.Kind](transcript/responseformat/kind-swift.enum.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/responseformat)*