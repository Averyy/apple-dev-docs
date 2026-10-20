# EvaluationContext

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

A context that provides the evaluation result within a test scope.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
struct EvaluationContext
```

## Mentions

- [Evaluating language model responses](./evaluating-language-model-responses.md)

#### Overview

Access the result through [`result`](./evaluationcontext/result.md) after the evaluation completes.

## Topics

### Instance Properties
- [let result: EvaluationResult](./evaluationcontext/result.md)
  The evaluation result.
### Type Properties
- [static var current: EvaluationContext](./evaluationcontext/current.md)
  The current evaluation context within the active test scope.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Swift Testing integration
- [struct EvaluationTrait](./evaluationtrait.md)
  A test trait that runs an evaluation and records the result as attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationcontext)*