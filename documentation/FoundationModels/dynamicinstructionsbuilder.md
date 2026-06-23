# DynamicInstructionsBuilder

**Framework**: Foundation Models  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@resultBuilder
struct DynamicInstructionsBuilder
```

## Topics

### Building dynamic instructions
- [static func buildBlock() -> EmptyDynamicInstructions](dynamicinstructionsbuilder/buildblock.md)
  Creates a builder with an empty block.
- [static buildBlock(_:)](dynamicinstructionsbuilder/buildblock(_:).md)
  Creates a builder with a block.
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> ConditionalDynamicInstructions<TrueContent, FalseContent>](dynamicinstructionsbuilder/buildeither(first:).md)
  Creates a builder with the first component.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> ConditionalDynamicInstructions<TrueContent, FalseContent>](dynamicinstructionsbuilder/buildeither(second:).md)
  Creates a builder with the second component.
- [static buildExpression(_:)](dynamicinstructionsbuilder/buildexpression(_:).md)
  Creates a builder with a list of tools expression.
- [static func buildOptional<Content>(Content?) -> Content?](dynamicinstructionsbuilder/buildoptional(_:).md)
  Creates a builder with an optional component.
- [static func buildLimitedAvailability(some DynamicInstructions) -> AnyDynamicInstructions](dynamicinstructionsbuilder/buildlimitedavailability(_:).md)
  Creates a builder with limited availability dynamic instructions.

## See Also

- [struct EmptyDynamicInstructions](emptydynamicinstructions.md)
  An empty dynamic instructions type..
- [struct ConditionalDynamicInstructions](conditionaldynamicinstructions.md)
  A dynamic instructions type that conditionally selects between two conditions.
- [struct AnyDynamicInstructions](anydynamicinstructions.md)
  A dynamic instructions type that’s type-erased.
- [struct TupleDynamicInstructions](tupledynamicinstructions.md)
  A dynamic instructions type that represents a tuple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsbuilder)*