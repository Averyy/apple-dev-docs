# EvaluationError

**Framework**: Evaluations  
**Kind**: enum

Errors thrown during an evaluation run.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum EvaluationError
```

#### Overview

```swift
do {
    let result = try await evaluation.run()
} catch EvaluationError.missingTranscript(let evaluatorType) {
    print("'\(evaluatorType)' requires a transcript")
}
```

## Topics

### Enumeration Cases
- [EvaluationError.metricsNotFound(names:)](evaluationerror/metricsnotfound(names:).md)
  One or more metric columns were not found in the evaluation results.
- [EvaluationError.missingTranscript(evaluatorType:)](evaluationerror/missingtranscript(evaluatortype:).md)
  An evaluator received a subject without the required transcript.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum EvaluatorError](evaluatorerror.md)
  A typed reason why an evaluator failed while scoring a produced subject.
- [enum SubjectInferenceError](subjectinferenceerror.md)
  A typed reason why `subject(from:)` failed to produce a subject for a sample.
- [enum EvaluationResultsError](evaluationresultserror.md)
  Errors the framework throws when parsing evaluation results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationerror)*