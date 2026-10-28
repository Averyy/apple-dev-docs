# SubjectInferenceError

**Framework**: Evaluations  
**Kind**: enum  
**Role**: Enumeration

A value that describes a failure to produce a subject for a sample.

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
enum SubjectInferenceError
```

## Overview

The evaluation runner records these values in the `"SubjectInferenceError"` column of [`detailed`](./evaluationresult/detailed.md). The evaluation runner omits this column entirely on a clean run where the run produces every subject successfully, so check for the column’s presence before reading it.

```swift
let result = try await evaluation.run()
if result.detailed.containsColumn("SubjectInferenceError") {
    let column = result.detailed["SubjectInferenceError", SubjectInferenceError.self]
    for (index, failure) in column.enumerated() {
        if let failure {
            print("Sample \(index) failed: \(failure.localizedDescription)")
        }
    }
}
```

Rows with a `SubjectInferenceError` value also have a `nil` `Response`, so failed samples are identifiable structurally. This is useful for filtering and re-running them. This error is distinct from [`EvaluatorError`](./evaluatorerror.md), which covers failures that occur after subject production succeeds.

## Topics

### Enumeration Cases
- [SubjectInferenceError.failed(reason:)](./subjectinferenceerror/failed%28reason%29.md)
  The subject method threw an error.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [enum EvaluationError](./evaluationerror.md)
  Errors thrown during an evaluation run.
- [enum EvaluatorError](./evaluatorerror.md)
  A value that describes why an evaluator failed while scoring a produced subject.
- [enum EvaluationResultsError](./evaluationresultserror.md)
  Errors the framework throws when parsing evaluation results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/subjectinferenceerror)*