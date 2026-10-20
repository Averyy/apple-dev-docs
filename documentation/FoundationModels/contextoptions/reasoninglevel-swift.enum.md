# ContextOptions.ReasoningLevel

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

A level of reasoning the model is allowed to output before producing a response.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum ReasoningLevel
```

## Topics

### Reasoning level cases
- [ContextOptions.ReasoningLevel.deep](./reasoninglevel-swift.enum/deep.md)
  A level that indicates deep reasoning that’s good for more analysis over a request.
- [ContextOptions.ReasoningLevel.light](./reasoninglevel-swift.enum/light.md)
  A level that indicates light reasoning that’s good for quick responses.
- [ContextOptions.ReasoningLevel.moderate](./reasoninglevel-swift.enum/moderate.md)
  A level that indicates a moderate amount of reasoning.
- [ContextOptions.ReasoningLevel.custom(_:)](./reasoninglevel-swift.enum/custom%28_%29.md)
  A custom level not represented by the other cases.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the reasoning level
- [var reasoningLevel: ContextOptions.ReasoningLevel?](./reasoninglevel-swift.property.md)
  A value that controls the amount of reasoning the model is allowed to output before producing a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/contextoptions/reasoninglevel-swift.enum)*