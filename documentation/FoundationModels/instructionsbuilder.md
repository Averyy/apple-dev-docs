# InstructionsBuilder

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A type that represents an instructions builder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
@resultBuilder
struct InstructionsBuilder
```

## Topics

### Building instructions
- [static func buildArray([some InstructionsRepresentable]) -> Instructions](./instructionsbuilder/buildarray%28_%29.md)
  Creates a builder with an array of instructions.
- [static func buildBlock<each I>(repeat each I) -> Instructions](./instructionsbuilder/buildblock%28_%29.md)
  Creates a builder with a block.
- [static func buildEither(first: some InstructionsRepresentable) -> Instructions](./instructionsbuilder/buildeither%28first%29.md)
  Creates a builder with the first component.
- [static func buildEither(second: some InstructionsRepresentable) -> Instructions](./instructionsbuilder/buildeither%28second%29.md)
  Creates a builder with the second component.
- [static buildExpression(_:)](./instructionsbuilder/buildexpression%28_%29.md)
  Creates a builder with an instructions expression.
- [static func buildLimitedAvailability(some InstructionsRepresentable) -> Instructions](./instructionsbuilder/buildlimitedavailability%28_%29.md)
  Creates a builder with limited availability instructions.
- [static func buildOptional(Instructions?) -> Instructions](./instructionsbuilder/buildoptional%28_%29.md)
  Creates a builder with an optional component.

## See Also

### Creating instructions
- [init(_:)](./instructions/init%28_%29.md)
  Creates instructions from the content of a builder closure.
- [protocol InstructionsRepresentable](./instructionsrepresentable.md)
  A type that can be represented as instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/instructionsbuilder)*