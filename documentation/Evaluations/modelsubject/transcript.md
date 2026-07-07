# transcript

**Framework**: Evaluations  
**Kind**: property

The structured transcript from the model session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var transcript: StructuredTranscript?
```

#### Discussion

Required when using [`ToolCallEvaluator`](toolcallevaluator.md). If `nil` and a [`ToolCallEvaluator`](toolcallevaluator.md) is used, [`EvaluationError.missingTranscript(evaluatorType:)`](evaluationerror/missingtranscript(evaluatortype:).md) is thrown.

## See Also

- [var value: Value](modelsubject/value.md)
  The typed value produced by the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsubject/transcript)*