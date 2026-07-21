# EvaluatorError

**Framework**: Evaluations  
**Kind**: enum

A typed reason why an evaluator failed while scoring a produced subject.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum EvaluatorError
```

#### Overview

Recorded in the detailed DataFrame’s EvaluatorErrors column (as an array, since multiple evaluators can fail for one sample). Distinct from [`SubjectInferenceError`](subjectinferenceerror.md) so each failure mode can grow its own cases independently.

## Topics

### Enumeration Cases
- [case failed(evaluator: (any EvaluatorProtocol)?, evaluatorType: String, reason: String)](evaluatorerror/failed(evaluator:evaluatortype:reason:).md)
  The evaluator threw.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum EvaluationError](evaluationerror.md)
  Errors thrown during an evaluation run.
- [enum SubjectInferenceError](subjectinferenceerror.md)
  A typed reason why `subject(from:)` failed to produce a subject for a sample.
- [enum EvaluationResultsError](evaluationresultserror.md)
  Errors the framework throws when parsing evaluation results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluatorerror)*