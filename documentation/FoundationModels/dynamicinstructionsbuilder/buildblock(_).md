# buildBlock(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Creates a builder with a block.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<T>(_ content: T) -> T where T : DynamicInstructions
```

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<each Content>(_ contents: repeat each Content) -> TupleDynamicInstructions<repeat each Content> where repeat each Content : DynamicInstructions
```

## See Also

### Building dynamic instructions
- [static func buildBlock() -> EmptyDynamicInstructions](./buildblock%28%29.md)
  Creates a builder with an empty block.
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> ConditionalDynamicInstructions<TrueContent, FalseContent>](./buildeither%28first%29.md)
  Creates a builder with the first component.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> ConditionalDynamicInstructions<TrueContent, FalseContent>](./buildeither%28second%29.md)
  Creates a builder with the second component.
- [static buildExpression(_:)](./buildexpression%28_%29.md)
  Creates a builder with a list of tools expression.
- [static func buildOptional<Content>(Content?) -> Content?](./buildoptional%28_%29.md)
  Creates a builder with an optional component.
- [static func buildLimitedAvailability(some DynamicInstructions) -> AnyDynamicInstructions](./buildlimitedavailability%28_%29.md)
  Creates a builder with limited availability dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsbuilder/buildblock(_:))*