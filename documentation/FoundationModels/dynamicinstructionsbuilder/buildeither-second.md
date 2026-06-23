# buildEither(second:)

**Framework**: Foundation Models  
**Kind**: method

Creates a builder with the second component.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
static func buildEither<TrueContent, FalseContent>(second content: FalseContent) -> ConditionalDynamicInstructions<TrueContent, FalseContent> where TrueContent : DynamicInstructions, FalseContent : DynamicInstructions
```

## See Also

- [static func buildBlock() -> EmptyDynamicInstructions](dynamicinstructionsbuilder/buildblock.md)
  Creates a builder with an empty block.
- [static buildBlock(_:)](dynamicinstructionsbuilder/buildblock(_:).md)
  Creates a builder with a block.
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> ConditionalDynamicInstructions<TrueContent, FalseContent>](dynamicinstructionsbuilder/buildeither(first:).md)
  Creates a builder with the first component.
- [static buildExpression(_:)](dynamicinstructionsbuilder/buildexpression(_:).md)
  Creates a builder with a list of tools expression.
- [static func buildOptional<Content>(Content?) -> Content?](dynamicinstructionsbuilder/buildoptional(_:).md)
  Creates a builder with an optional component.
- [static func buildLimitedAvailability(some DynamicInstructions) -> AnyDynamicInstructions](dynamicinstructionsbuilder/buildlimitedavailability(_:).md)
  Creates a builder with limited availability dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsbuilder/buildeither(second:))*