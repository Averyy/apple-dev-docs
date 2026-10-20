# PromptBuilder

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A type that represents a prompt builder.

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
struct PromptBuilder
```

## Topics

### Building a prompt
- [static func buildArray([some PromptRepresentable]) -> Prompt](./promptbuilder/buildarray%28_%29.md)
  Creates a builder with an array of prompts.
- [static func buildBlock<each P>(repeat each P) -> Prompt](./promptbuilder/buildblock%28_%29.md)
  Creates a builder with a block.
- [static func buildEither(first: some PromptRepresentable) -> Prompt](./promptbuilder/buildeither%28first%29.md)
  Creates a builder with the first component.
- [static func buildEither(second: some PromptRepresentable) -> Prompt](./promptbuilder/buildeither%28second%29.md)
  Creates a builder with the second component.
- [static buildExpression(_:)](./promptbuilder/buildexpression%28_%29.md)
  Creates a builder with a prompt expression.
- [static func buildLimitedAvailability(some PromptRepresentable) -> Prompt](./promptbuilder/buildlimitedavailability%28_%29.md)
  Creates a builder with a limited availability prompt.
- [static func buildOptional(Prompt?) -> Prompt](./promptbuilder/buildoptional%28_%29.md)
  Creates a builder with an optional component.

## See Also

### Creating a prompt
- [init(_:)](./prompt/init%28_%29.md)
  Creates a prompt from the content of a builder closure.
- [protocol PromptRepresentable](./promptrepresentable.md)
  A type whose value can represent a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/promptbuilder)*