# ArgumentMatcher

**Framework**: Evaluations  
**Kind**: enum

The values that define how to validate a tool-call argument.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum ArgumentMatcher
```

## Mentions

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

#### Overview

Use argument matchers to specify validation rules for tool-call arguments. You can require exact values, verify key presence, check ranges, match patterns, or use a language model for semantic matching.

For example:

```swift
let matchers: [ArgumentMatcher] = [
    .exact(argumentName: "city", value: "San Francisco"),
    .keyOnly(argumentName: "units"),
    .naturalLanguage(argumentName: "prompt", criteria: "A weather-related question")
]
```

| Validation Strategy | Rules |
| --- | --- |
| [`ArgumentMatcher.exact(argumentName:value:)`](argumentmatcher/exact(argumentname:value:).md) | Value must equal the expected value exactly. Use for identifiers, enum values, and precise inputs. |
| [`ArgumentMatcher.keyOnly(argumentName:)`](argumentmatcher/keyonly(argumentname:).md) | Argument must be present with any value. Use when you care that the model provides the parameter but any value is acceptable. |
| [`ArgumentMatcher.oneOf(argumentName:allowedValues:)`](argumentmatcher/oneof(argumentname:allowedvalues:).md) | Value must be one of the allowed options. Use for ambiguous prompts with multiple valid interpretations. |
| [`ArgumentMatcher.range(argumentName:minimum:maximum:)`](argumentmatcher/range(argumentname:minimum:maximum:).md) | Numeric value must fall within bounds (inclusive). Use for quantities where a range is acceptable. |
| [`ArgumentMatcher.pattern(argumentName:regex:)`](argumentmatcher/pattern(argumentname:regex:).md) | String must match a regular expression. Use for structured formats: emails, dates, IDs. |
| [`ArgumentMatcher.contains(argumentName:substring:)`](argumentmatcher/contains(argumentname:substring:).md) | String must contain a substring. Use when the argument references a concept but phrasing varies. |
| [`ArgumentMatcher.hasPrefix(argumentName:prefix:)`](argumentmatcher/hasprefix(argumentname:prefix:).md) | String must start with a prefix. Use for paths, URLs, or namespaced values. |
| [`ArgumentMatcher.hasSuffix(argumentName:suffix:)`](argumentmatcher/hassuffix(argumentname:suffix:).md) | String must end with a suffix. Use for file extensions or domain-specific endings. |
| [`ArgumentMatcher.naturalLanguage(argumentName:criteria:)`](argumentmatcher/naturallanguage(argumentname:criteria:).md) | A language model judges whether the value satisfies the criteria. Use when correctness is subjective or hard to express with string operations, for example, validating that a query argument is “a weather-related question”. |

## Topics

### Exact matching
- [case exact(argumentName: String, value: ArgumentValue)](argumentmatcher/exact(argumentname:value:).md)
  A value that indicates that the argument must be present with this exact key and value.
- [ArgumentMatcher.keyOnly(argumentName:)](argumentmatcher/keyonly(argumentname:).md)
  A value that indicates that the argument must be present with this key and no specific value.
### Set and range matching
- [case oneOf(argumentName: String, allowedValues: [ArgumentValue])](argumentmatcher/oneof(argumentname:allowedvalues:).md)
  A value that indicates the argument must be present with a value that matches one of the allowed values.
- [case range(argumentName: String, minimum: Double?, maximum: Double?)](argumentmatcher/range(argumentname:minimum:maximum:).md)
  A value that indicates that the argument must be present and its numeric value must be within the specified range.
### String matching
- [case pattern(argumentName: String, regex: String)](argumentmatcher/pattern(argumentname:regex:).md)
  A value that indicates that the argument must be present and its string value must match the specified regex pattern.
- [case contains(argumentName: String, substring: String)](argumentmatcher/contains(argumentname:substring:).md)
  A value that indicates that the argument must be present and its string value must contain the specified substring.
- [case hasPrefix(argumentName: String, prefix: String)](argumentmatcher/hasprefix(argumentname:prefix:).md)
  A value that indicates that the argument must be present and its string value must start with the specified prefix.
- [case hasSuffix(argumentName: String, suffix: String)](argumentmatcher/hassuffix(argumentname:suffix:).md)
  A value that indicates that the argument must be present and its string value must end with the specified suffix.
### Semantic matching
- [case naturalLanguage(argumentName: String, criteria: String)](argumentmatcher/naturallanguage(argumentname:criteria:).md)
  A value that indicates that the argument must be present and semantically match the given criteria.
### Supporting types
- [enum ArgumentValue](argumentvalue.md)
  A primitive value type for argument specifications that is @Generable.
- [enum StructuredValue](structuredvalue.md)
  A type-safe representation of JSON values.

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

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)
  Analyze your model’s tool calls against expected trajectories, argument values, and call ordering.
- [struct ToolCallEvaluator](toolcallevaluator.md)
  An evaluator that verifies agentic tool calls against an expected trajectory.
- [struct TrajectoryExpectation](trajectoryexpectation.md)
  The expected pattern of tool calls for an evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher)*