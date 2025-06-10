# PromptBuilder

**Framework**: Foundation Models  
**Kind**: struct

A type that represents a prompt builder.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@resultBuilder
struct PromptBuilder
```

## Topics

### Building a prompt
- [static func buildArray([some PromptRepresentable]) -> Prompt](promptbuilder/buildarray(_:).md)
  Creates a builder with the an array of prompts.
- [static func buildBlock<each P>(repeat each P) -> Prompt](promptbuilder/buildblock(_:).md)
  Creates a builder with the a block.
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

## See Also

- [init(_:)](prompt/init(_:).md)
- [protocol PromptRepresentable](promptrepresentable.md)
  A protocol that represents a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/promptbuilder)*