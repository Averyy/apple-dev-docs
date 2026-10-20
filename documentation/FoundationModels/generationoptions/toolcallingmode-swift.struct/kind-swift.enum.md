# GenerationOptions.ToolCallingMode.Kind

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

A representation of the different ways a model can use tools.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum Kind
```

## Topics

### Tool calling mode cases
- [GenerationOptions.ToolCallingMode.Kind.allowed](./kind-swift.enum/allowed.md)
  The model may call tools.
- [GenerationOptions.ToolCallingMode.Kind.disallowed](./kind-swift.enum/disallowed.md)
  The model can’t call any tools.
- [GenerationOptions.ToolCallingMode.Kind.required](./kind-swift.enum/required.md)
  The model must call one or more tools.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing the content
- [var kind: GenerationOptions.ToolCallingMode.Kind](./kind-swift.property.md)
  The tool-calling behavior this mode represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/toolcallingmode-swift.struct/kind-swift.enum)*