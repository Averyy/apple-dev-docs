# buildExpression(_:)

**Framework**: Foundation Models  
**Kind**: method

Creates a builder with a prompt expression.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func buildExpression(_ expression: Instructions) -> Instructions
```

## See Also

- [static func buildArray([some InstructionsRepresentable]) -> Instructions](instructionsbuilder/buildarray(_:).md)
  Creates a builder with the an array of prompts.
- [static func buildBlock<each I>(repeat each I) -> Instructions](instructionsbuilder/buildblock(_:).md)
  Creates a builder with the a block.
- [static func buildEither(first: some InstructionsRepresentable) -> Instructions](instructionsbuilder/buildeither(first:).md)
  Creates a builder with the first component.
- [static func buildEither(second: some InstructionsRepresentable) -> Instructions](instructionsbuilder/buildeither(second:).md)
  Creates a builder with the second component.
- [static func buildLimitedAvailability(some InstructionsRepresentable) -> Instructions](instructionsbuilder/buildlimitedavailability(_:).md)
  Creates a builder with a limited availability prompt.
- [static func buildOptional(Instructions?) -> Instructions](instructionsbuilder/buildoptional(_:).md)
  Creates a builder with an optional component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/instructionsbuilder/buildexpression(_:))*