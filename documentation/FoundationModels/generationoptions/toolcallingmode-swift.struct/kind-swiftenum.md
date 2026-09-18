# GenerationOptions.ToolCallingMode.Kind

**Framework**: Foundation Models  
**Kind**: enum

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
- [GenerationOptions.ToolCallingMode.Kind.allowed](generationoptions/toolcallingmode-swift.struct/kind-swift.enum/allowed.md)
  The model may call tools.
- [GenerationOptions.ToolCallingMode.Kind.disallowed](generationoptions/toolcallingmode-swift.struct/kind-swift.enum/disallowed.md)
  The model can’t call any tools.
- [GenerationOptions.ToolCallingMode.Kind.required](generationoptions/toolcallingmode-swift.struct/kind-swift.enum/required.md)
  The model must call one or more tools.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var kind: GenerationOptions.ToolCallingMode.Kind](generationoptions/toolcallingmode-swift.struct/kind-swift.property.md)
  The tool-calling behavior this mode represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/toolcallingmode-swift.struct/kind-swift.enum)*