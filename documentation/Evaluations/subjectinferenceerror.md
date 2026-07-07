# SubjectInferenceError

**Framework**: Evaluations  
**Kind**: enum

A typed reason why `subject(from:)` failed to produce a subject for a sample.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum SubjectInferenceError
```

#### Overview

Recorded in the detailed DataFrame’s SubjectInferenceError column for any row whose subject could not be produced. Distinct from [`EvaluatorError`](evaluatorerror.md) so each failure mode can grow its own cases independently — a subject-inference failure has no notion of an evaluator.

## Topics

### Enumeration Cases
- [SubjectInferenceError.failed(reason:)](subjectinferenceerror/failed(reason:).md)
  The subject producer threw. `reason` is the thrown error’s `localizedDescription`.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum EvaluationError](evaluationerror.md)
  Errors thrown during an evaluation run.
- [enum EvaluatorError](evaluatorerror.md)
  A typed reason why an evaluator failed while scoring a produced subject.
- [enum EvaluationResultsError](evaluationresultserror.md)
  Errors the framework throws when parsing evaluation results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/subjectinferenceerror)*