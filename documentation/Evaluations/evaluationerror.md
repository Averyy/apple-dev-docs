# EvaluationError

**Framework**: Evaluations  
**Kind**: enum  
**Role**: Enumeration

Errors thrown during an evaluation run.

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
- [EvaluationError.duplicateMetricName(name:)](./evaluationerror/duplicatemetricname%28name%29.md)
  Two evaluators — or a single evaluator returning multiple metrics — produced a metric with the same name for the same sample.
- [EvaluationError.missingTranscript(evaluatorType:)](./evaluationerror/missingtranscript%28evaluatortype%29.md)
  An evaluator received a subject without the required transcript.

## Relationships

### Conforms To
- [Error](../Swift/error.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [enum EvaluatorError](./evaluatorerror.md)
  A value that describes why an evaluator failed while scoring a produced subject.
- [enum SubjectInferenceError](./subjectinferenceerror.md)
  A value that describes a failure to produce a subject for a sample.
- [enum EvaluationResultsError](./evaluationresultserror.md)
  Errors the framework throws when parsing evaluation results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationerror)*