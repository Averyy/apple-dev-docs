# ToolExpectation

**Framework**: Evaluations  
**Kind**: struct

A specification for an expected tool call, or a group of expectations that can be satisfied in any order.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ToolExpectation
```

## Mentions

- [Evaluating language model responses](evaluating-language-model-responses.md)
- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

#### Overview

Most commonly, a `ToolExpectation` identifies a single tool by name and optionally validates its arguments:

```swift
ToolExpectation("getWeather", arguments: [
    .exact(argumentName: "location", value: "Paris, France")
])
```

For ordered sequences where multiple tools must all be called at the same position but their relative order doesn’t matter, use [`anyOrder(_:)`](toolexpectation/anyorder(_:).md):

```swift
ToolExpectation.anyOrder([
    ToolExpectation("fetchData"),
    ToolExpectation("fetchMetadata"),
])
```

## Topics

### Creating an expectation
- [init(String, arguments: [ArgumentMatcher])](toolexpectation/init(_:arguments:).md)
  Creates a new tool expectation.
### Creating any-order groups
- [static func anyOrder([ToolExpectation]) -> ToolExpectation](toolexpectation/anyorder(_:).md)
  Creates a group of expectations that must all be satisfied at the same sequential position, but can occur in any relative order.
### Accessing expectation details
- [var name: String](toolexpectation/name.md)
  The name of the tool that the evaluation expects the model to call.
- [var arguments: [ArgumentMatcher]](toolexpectation/arguments.md)
  The argument matchers to validate against the tool call.
- [var isAnyOrderGroup: Bool](toolexpectation/isanyordergroup.md)
  A Boolean value that indicates whether this expectation represents a group of expectations that can be satisfied in any order.
### Matching arguments
- [enum ArgumentMatcher](argumentmatcher.md)
  The values that define how to validate a tool-call argument.

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](../FoundationModels/ConvertibleFromGeneratedContent.md)
- [ConvertibleToGeneratedContent](../FoundationModels/ConvertibleToGeneratedContent.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Escapable](../Swift/Escapable.md)
- [Generable](../FoundationModels/Generable.md)
- [InstructionsRepresentable](../FoundationModels/InstructionsRepresentable.md)
- [PromptRepresentable](../FoundationModels/PromptRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(expected: String, arguments: [ArgumentMatcher])](trajectoryexpectation/init(expected:arguments:).md)
  Creates a trajectory expectation for a single expected tool call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolexpectation)*