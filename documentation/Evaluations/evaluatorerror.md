# EvaluatorError

**Framework**: Evaluations  
**Kind**: enum

A value that describes why an evaluator failed while scoring a produced subject.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
enum EvaluatorError
```

#### Overview

The evaluation runner records these values in the `"EvaluatorErrors"` column of [`detailed`](evaluationresult/detailed.md) as an array. Multiple evaluators can fail for the same sample. The evaluation runner omits this column entirely when no evaluator fails, so check for the column’s presence before reading it.

```swift
let result = try await evaluation.run()
if result.detailed.containsColumn("EvaluatorErrors") {
    let column = result.detailed["EvaluatorErrors", [EvaluatorError].self]
    for (index, failures) in column.enumerated() {
        if let failures {
            for failure in failures {
                print("Sample \(index): \(failure.localizedDescription)")
            }
        }
    }
}
```

Rows with an `EvaluatorErrors` value always have a non-`nil` `Response`. Evaluators only run after subject production succeeds. Distinct from [`SubjectInferenceError`](subjectinferenceerror.md), which covers failures that occur before subject production.

## Topics

### Enumeration Cases
- [case failed(evaluator: (any EvaluatorProtocol)?, evaluatorType: String, reason: String)](evaluatorerror/failed(evaluator:evaluatortype:reason:).md)
  The evaluator threw an error while scoring the subject.

## Relationships

### Conforms To
- [Error](../swift/error.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum EvaluationError](evaluationerror.md)
  Errors thrown during an evaluation run.
- [enum SubjectInferenceError](subjectinferenceerror.md)
  A value that describes a failure to produce a subject for a sample.
- [enum EvaluationResultsError](evaluationresultserror.md)
  Errors the framework throws when parsing evaluation results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluatorerror)*