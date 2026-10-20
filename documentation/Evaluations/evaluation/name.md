# name

**Framework**: Evaluations  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The evaluation’s name in results. Defaults to the type name; override for a custom one.

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
var name: String { get }
```

## Default Implementations

### Evaluation Implementations
- [var name: String](./name-9jrme.md)
  The default name, taken from the type name.

## See Also

### Testing an intelligent feature
- [associatedtype Subject : EvaluationSubject](./subject.md)
  The type of subject the system under test produces.
- [func subject(from: Self.Sample) async throws -> Self.Subject](./subject%28from%29.md)
  Produces the subject of evaluation from a given sample.
- [protocol EvaluationSubject](../evaluationsubject.md)
  A type that represents the output the system under test produces.
- [struct ModelSubject](../modelsubject.md)
  The subject type for language model evaluations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/name)*