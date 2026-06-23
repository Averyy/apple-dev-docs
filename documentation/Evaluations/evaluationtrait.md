# EvaluationTrait

**Framework**: Evaluations  
**Kind**: struct

A test trait that runs an evaluation and records the result as attachments.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct EvaluationTrait
```

## Mentions

- [Evaluating language model responses](evaluating-language-model-responses.md)
- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

#### Overview

The result is accessible via [`EvaluationContext`](evaluationcontext.md).

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TestScoping](../Testing/TestScoping.md)
- [TestTrait](../Testing/TestTrait.md)
- [Trait](../Testing/Trait.md)

## See Also

- [struct EvaluationContext](evaluationcontext.md)
  A context that provides the evaluation result within a test scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationtrait)*