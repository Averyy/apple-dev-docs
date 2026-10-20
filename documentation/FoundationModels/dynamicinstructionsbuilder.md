# DynamicInstructionsBuilder

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A result builder that combines tools and other content into dynamic instructions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@resultBuilder
struct DynamicInstructionsBuilder
```

## Topics

### Building dynamic instructions
- [static func buildBlock() -> EmptyDynamicInstructions](./dynamicinstructionsbuilder/buildblock%28%29.md)
  Creates a builder with an empty block.
- [static buildBlock(_:)](./dynamicinstructionsbuilder/buildblock%28_%29.md)
  Creates a builder with a block.
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> ConditionalDynamicInstructions<TrueContent, FalseContent>](./dynamicinstructionsbuilder/buildeither%28first%29.md)
  Creates a builder with the first component.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> ConditionalDynamicInstructions<TrueContent, FalseContent>](./dynamicinstructionsbuilder/buildeither%28second%29.md)
  Creates a builder with the second component.
- [static buildExpression(_:)](./dynamicinstructionsbuilder/buildexpression%28_%29.md)
  Creates a builder with a list of tools expression.
- [static func buildOptional<Content>(Content?) -> Content?](./dynamicinstructionsbuilder/buildoptional%28_%29.md)
  Creates a builder with an optional component.
- [static func buildLimitedAvailability(some DynamicInstructions) -> AnyDynamicInstructions](./dynamicinstructionsbuilder/buildlimitedavailability%28_%29.md)
  Creates a builder with limited availability dynamic instructions.

## See Also

### Building dynamic instructions
- [struct EmptyDynamicInstructions](./emptydynamicinstructions.md)
  An empty dynamic instructions type.
- [struct ConditionalDynamicInstructions](./conditionaldynamicinstructions.md)
  A dynamic instructions type that conditionally selects between two conditions.
- [struct AnyDynamicInstructions](./anydynamicinstructions.md)
  A dynamic instructions type that’s type-erased.
- [struct TupleDynamicInstructions](./tupledynamicinstructions.md)
  A dynamic instructions type that represents a tuple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsbuilder)*