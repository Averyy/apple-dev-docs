# EvaluationContext

**Framework**: Evaluations  
**Kind**: struct

A context that provides the evaluation result within a test scope.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct EvaluationContext
```

## Mentions

- [Evaluating language model responses](evaluating-language-model-responses.md)

#### Overview

Access the result via [`result`](evaluationcontext/result.md) after the evaluation completes.

## Topics

### Instance Properties
- [let result: EvaluationResult](evaluationcontext/result.md)
  The evaluation result.
### Type Properties
- [static var current: EvaluationContext](evaluationcontext/current.md)
  The current evaluation context within the active test scope.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct EvaluationTrait](evaluationtrait.md)
  A test trait that runs an evaluation and records the result as attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationcontext)*