# EvaluationResultsError

**Framework**: Evaluations  
**Kind**: enum

Errors the framework throws when parsing evaluation results.

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
enum EvaluationResultsError
```

#### Overview

```swift
do {
    throw EvaluationResultsError.fileNotFound(URL(fileURLWithPath: "/tmp/results.json"))
} catch EvaluationResultsError.fileNotFound(let url) {
    print("File not found: \(url)")
}
```

## Topics

### Enumeration Cases
- [EvaluationResultsError.emptyJSONFile](evaluationresultserror/emptyjsonfile.md)
  The JSON file exists but contains no data.
- [EvaluationResultsError.fileNotFound(_:)](evaluationresultserror/filenotfound(_:).md)
  The specified file URL is not findable on disk.
- [EvaluationResultsError.invalidJSONFormat](evaluationresultserror/invalidjsonformat.md)
  The JSON data doesn’t match the expected evaluation result format.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum EvaluationError](evaluationerror.md)
  Errors thrown during an evaluation run.
- [enum EvaluatorError](evaluatorerror.md)
  A value that describes why an evaluator failed while scoring a produced subject.
- [enum SubjectInferenceError](subjectinferenceerror.md)
  A value that describes a failure to produce a subject for a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresultserror)*