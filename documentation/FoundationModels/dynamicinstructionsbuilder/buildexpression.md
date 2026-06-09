# buildExpression(_:)

**Framework**: Foundation Models  
**Kind**: method

Creates a builder with a list of tools expression.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func buildExpression(_ tools: [any Tool]) -> some DynamicInstructions
```

## See Also

- [static func buildBlock() -> EmptyDynamicInstructions](dynamicinstructionsbuilder/buildblock.md)
  Creates a builder with an empty block.
- [static buildBlock(_:)](dynamicinstructionsbuilder/buildblock(_:).md)
  Creates a builder with a block.
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> ConditionalDynamicInstructions<TrueContent, FalseContent>](dynamicinstructionsbuilder/buildeither(first:).md)
  Creates a builder with the first component.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> ConditionalDynamicInstructions<TrueContent, FalseContent>](dynamicinstructionsbuilder/buildeither(second:).md)
  Creates a builder with the second component.
- [static func buildOptional<Content>(Content?) -> Content?](dynamicinstructionsbuilder/buildoptional(_:).md)
  Creates a builder with an optional component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsbuilder/buildexpression(_:))*