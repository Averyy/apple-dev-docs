# EvaluationError.missingTranscript(evaluatorType:)

**Framework**: Evaluations  
**Kind**: case

An evaluator received a subject without the required transcript.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case missingTranscript(evaluatorType: String)
```

#### Discussion

This occurs when using [`ToolCallEvaluator`](toolcallevaluator.md) with a [`ModelSubject`](modelsubject.md) that has a `nil` transcript. Pass `session.transcript.structuredTranscript` when creating the `ModelSubject`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationerror/missingtranscript(evaluatortype:))*