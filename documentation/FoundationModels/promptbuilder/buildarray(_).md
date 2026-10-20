# buildArray(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Creates a builder with an array of prompts.

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
static func buildArray(_ prompts: [some PromptRepresentable]) -> Prompt
```

## See Also

### Building a prompt
- [static func buildBlock<each P>(repeat each P) -> Prompt](./buildblock%28_%29.md)
  Creates a builder with a block.
- [static func buildEither(first: some PromptRepresentable) -> Prompt](./buildeither%28first%29.md)
  Creates a builder with the first component.
- [static func buildEither(second: some PromptRepresentable) -> Prompt](./buildeither%28second%29.md)
  Creates a builder with the second component.
- [static buildExpression(_:)](./buildexpression%28_%29.md)
  Creates a builder with a prompt expression.
- [static func buildLimitedAvailability(some PromptRepresentable) -> Prompt](./buildlimitedavailability%28_%29.md)
  Creates a builder with a limited availability prompt.
- [static func buildOptional(Prompt?) -> Prompt](./buildoptional%28_%29.md)
  Creates a builder with an optional component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/promptbuilder/buildarray(_:))*