# name

**Framework**: Evaluations  
**Kind**: property

The default name, taken from the type name.

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
var name: String { get }
```

## See Also

- [associatedtype Subject : EvaluationSubject](evaluation/subject.md)
  The type of subject the system under test produces.
- [func subject(from: Self.Sample) async throws -> Self.Subject](evaluation/subject(from:).md)
  Produces the subject of evaluation from a given sample.
- [protocol EvaluationSubject](evaluationsubject.md)
  A type that represents the output the system under test produces.
- [struct ModelSubject](modelsubject.md)
  The subject type for language model evaluations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/name)*