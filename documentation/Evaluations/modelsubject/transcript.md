# transcript

**Framework**: Evaluations  
**Kind**: property  
**Role**: Instance Property

The structured transcript from the model session.

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
var transcript: StructuredTranscript?
```

#### Discussion

This transcript is required when using [`ToolCallEvaluator`](../toolcallevaluator.md). If `nil`, [`ToolCallEvaluator`](../toolcallevaluator.md) throws [`EvaluationError.missingTranscript(evaluatorType:)`](../evaluationerror/missingtranscript%28evaluatortype%29.md).

## See Also

### Accessing the content
- [var value: Value](./value.md)
  The typed value the model produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsubject/transcript)*