# EvaluationError.missingTranscript(evaluatorType:)

**Framework**: Evaluations  
**Kind**: case

An evaluator received a subject without the required transcript.

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
case missingTranscript(evaluatorType: String)
```

#### Discussion

This occurs when using [`ToolCallEvaluator`](toolcallevaluator.md) with a [`ModelSubject`](modelsubject.md) that has a `nil` transcript. Pass `session.transcript.structuredTranscript` when creating the `ModelSubject`.

## Parameters

- `evaluatorType`: The concrete type name of the evaluator that requires a transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationerror/missingtranscript(evaluatortype:))*