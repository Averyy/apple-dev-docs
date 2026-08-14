# Transcript.Instructions

**Framework**: Foundation Models  
**Kind**: struct

Instructions you provide to the model that define its behavior.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Instructions
```

#### Overview

Instructions are typically provided to define the role and behavior of the model. The model is typically trained to obey instructions over any commands it receives in prompts. This is a security mechanism to help mitigate prompt injection attacks.

## Topics

### Creating instructions
- [init(id: String, segments: [Transcript.Segment], toolDefinitions: [Transcript.ToolDefinition])](transcript/instructions/init(id:segments:tooldefinitions:).md)
  Creates instructions that describe how you want the model to behave, in natural language.
### Inspecting instructions
- [var segments: [Transcript.Segment]](transcript/instructions/segments.md)
  The content of the instructions, in natural language.
- [var toolDefinitions: [Transcript.ToolDefinition]](transcript/instructions/tooldefinitions.md)
  A list of tools made available to the model.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Transcript.Entry](transcript/entry.md)
  An entry in a transcript.
- [Transcript.Prompt](transcript/prompt.md)
  A prompt from the user to the model.
- [Transcript.Response](transcript/response.md)
  A response from the model.
- [Transcript.Reasoning](transcript/reasoning.md)
  A reasoning entry from the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/instructions)*