# buildExpression(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Creates a builder with an instructions expression.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
@export(implementation)
static func buildExpression(_ expression: Instructions) -> Instructions
```

**Other overloads**:

```swift
@export(implementation)
static func buildExpression<I>(_ expression: I) -> I where I : InstructionsRepresentable
```

## See Also

### Building instructions
- [static func buildArray([some InstructionsRepresentable]) -> Instructions](./buildarray%28_%29.md)
  Creates a builder with an array of instructions.
- [static func buildBlock<each I>(repeat each I) -> Instructions](./buildblock%28_%29.md)
  Creates a builder with a block.
- [static func buildEither(first: some InstructionsRepresentable) -> Instructions](./buildeither%28first%29.md)
  Creates a builder with the first component.
- [static func buildEither(second: some InstructionsRepresentable) -> Instructions](./buildeither%28second%29.md)
  Creates a builder with the second component.
- [static func buildLimitedAvailability(some InstructionsRepresentable) -> Instructions](./buildlimitedavailability%28_%29.md)
  Creates a builder with limited availability instructions.
- [static func buildOptional(Instructions?) -> Instructions](./buildoptional%28_%29.md)
  Creates a builder with an optional component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/instructionsbuilder/buildexpression(_:))*