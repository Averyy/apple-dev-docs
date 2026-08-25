# subject(from:)

**Framework**: Evaluations  
**Kind**: method  
**Required**: Yes

Produces the subject of evaluation from a given sample.

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
nonisolated
(nonsending) func subject(from sample: Self.Sample) async throws -> Self.Subject
```

## Mentions

- [Evaluating language model responses](evaluating-language-model-responses.md)
- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

#### Return Value

The subject of evaluation.

#### Discussion

Implement this method to run your system under test and return the subject that evaluators will measure.

## Parameters

- `sample`: The input sample.

## See Also

- [associatedtype Subject : EvaluationSubject](evaluation/subject.md)
  The type of subject the system under test produces.
- [protocol EvaluationSubject](evaluationsubject.md)
  A type that represents the output the system under test produces.
- [struct ModelSubject](modelsubject.md)
  The subject type for language model evaluations.
- [var name: String](evaluation/name.md)
  The default name, taken from the type name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/subject(from:))*