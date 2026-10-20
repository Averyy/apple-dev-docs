# Subject

**Framework**: Evaluations  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of subject the system under test produces.

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
associatedtype Subject : EvaluationSubject
```

## See Also

### Testing an intelligent feature
- [func subject(from: Self.Sample) async throws -> Self.Subject](./subject%28from%29.md)
  Produces the subject of evaluation from a given sample.
- [protocol EvaluationSubject](../evaluationsubject.md)
  A type that represents the output the system under test produces.
- [struct ModelSubject](../modelsubject.md)
  The subject type for language model evaluations.
- [var name: String](./name.md)
  The evaluation’s name in results. Defaults to the type name; override for a custom one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/subject)*