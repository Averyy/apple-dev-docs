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
- Xcode 27.0+ (Beta)

## Declaration

```swift
var transcript: StructuredTranscript?
```

#### Discussion

This transcript is required when using [`ToolCallEvaluator`](toolcallevaluator.md). If `nil`, [`ToolCallEvaluator`](toolcallevaluator.md) throws [`EvaluationError.missingTranscript(evaluatorType:)`](evaluationerror/missingtranscript(evaluatortype:).md).

## See Also

- [var value: Value](modelsubject/value.md)
  The typed value the model produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsubject/transcript)*