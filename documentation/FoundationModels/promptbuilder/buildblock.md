# buildBlock(_:)

**Framework**: Foundation Models  
**Kind**: method

Creates a builder with the a block.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func buildBlock<each P>(_ components: repeat each P) -> Prompt where repeat each P : PromptRepresentable
```

## See Also

- [static func buildArray([some PromptRepresentable]) -> Prompt](promptbuilder/buildarray(_:).md)
  Creates a builder with the an array of prompts.
- [static func buildEither(first: some PromptRepresentable) -> Prompt](promptbuilder/buildeither(first:).md)
  Creates a builder with the first component.
- [static func buildEither(second: some PromptRepresentable) -> Prompt](promptbuilder/buildeither(second:).md)
  Creates a builder with the second component.
- [static buildExpression(_:)](promptbuilder/buildexpression(_:).md)
  Creates a builder with a prompt expression.
- [static func buildLimitedAvailability(some PromptRepresentable) -> Prompt](promptbuilder/buildlimitedavailability(_:).md)
  Creates a builder with a limited availability prompt.
- [static func buildOptional(Prompt?) -> Prompt](promptbuilder/buildoptional(_:).md)
  Creates a builder with an optional component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/promptbuilder/buildblock(_:))*