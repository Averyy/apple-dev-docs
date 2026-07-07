# Subject

**Framework**: Evaluations  
**Kind**: associatedtype  
**Required**: Yes

The type of the subject produced by the system under test.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
associatedtype Subject : EvaluationSubject
```

## See Also

- [func subject(from: Self.Sample) async throws -> Self.Subject](evaluation/subject(from:).md)
  Produces the subject of evaluation from a given sample.
- [protocol EvaluationSubject](evaluationsubject.md)
  A type that represents the output produced by the system under test.
- [struct ModelSubject](modelsubject.md)
  The subject type for language model evaluations.
- [var name: String](evaluation/name.md)
  The default name, derived from the type name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/subject)*