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

## Declaration

```swift
enum EvaluationError
```

#### Overview

```swift
do {
    throw EvaluationError.metricsNotFound(names: ["Accuracy"])
} catch EvaluationError.metricsNotFound(let names) {
    print("Missing metrics: \(names)")
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

- [enum EvaluationResultsError](evaluationresultserror.md)
  Errors the framework throws when parsing evaluation results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationerror)*