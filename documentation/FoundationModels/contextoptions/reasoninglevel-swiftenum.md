# ContextOptions.ReasoningLevel

**Framework**: Foundation Models  
**Kind**: enum

Controls the amount of reasoning that the model is allowed to output before producing a response.

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
- [ContextOptions.ReasoningLevel.deep](contextoptions/reasoninglevel-swift.enum/deep.md)
  A level that indicates deep reasoning that’s good for more analysis over a request.
- [ContextOptions.ReasoningLevel.light](contextoptions/reasoninglevel-swift.enum/light.md)
  A level that indicates light reasoning that’s good for quick responses.
- [ContextOptions.ReasoningLevel.moderate](contextoptions/reasoninglevel-swift.enum/moderate.md)
  A level that indicates a moderate amount of reasoning.
- [ContextOptions.ReasoningLevel.custom(_:)](contextoptions/reasoninglevel-swift.enum/custom(_:).md)
  A custom level that indicates a level not supported by the other cases.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var reasoningLevel: ContextOptions.ReasoningLevel?](contextoptions/reasoninglevel-swift.property.md)
  Controls the amount of reasoning that the model is allowed to output before producing a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/contextoptions/reasoninglevel-swift.enum)*