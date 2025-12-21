# InstructionsBuilder

**Framework**: Foundation Models  
**Kind**: struct

A type that represents an instructions builder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@resultBuilder
struct InstructionsBuilder
```

## Topics

### Building instructions
- [static func buildArray([some InstructionsRepresentable]) -> Instructions](instructionsbuilder/buildarray(_:).md)
  Creates a builder with the an array of prompts.
- [static func buildBlock<each I>(repeat each I) -> Instructions](instructionsbuilder/buildblock(_:).md)
  Creates a builder with the a block.
- [static func buildEither(first: some InstructionsRepresentable) -> Instructions](instructionsbuilder/buildeither(first:).md)
  Creates a builder with the first component.
- [static func buildEither(second: some InstructionsRepresentable) -> Instructions](instructionsbuilder/buildeither(second:).md)
  Creates a builder with the second component.
- [static buildExpression(_:)](instructionsbuilder/buildexpression(_:).md)
  Creates a builder with a prompt expression.
- [static func buildLimitedAvailability(some InstructionsRepresentable) -> Instructions](instructionsbuilder/buildlimitedavailability(_:).md)
  Creates a builder with a limited availability prompt.
- [static func buildOptional(Instructions?) -> Instructions](instructionsbuilder/buildoptional(_:).md)
  Creates a builder with an optional component.

## See Also

- [init(_:)](instructions/init(_:).md)
- [protocol InstructionsRepresentable](instructionsrepresentable.md)
  A type that can be represented as instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/instructionsbuilder)*