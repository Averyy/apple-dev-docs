# EvaluationSubject

**Framework**: Evaluations  
**Kind**: protocol

A type that represents the output produced by the system under test.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol EvaluationSubject<Value>
```

#### Overview

Conform to this protocol to define custom subject types. The primary concrete conformance is [`ModelSubject`](modelsubject.md), which carries a value and an optional transcript for tool-call evaluation.

```swift
struct MySubject<Value: Codable>: EvaluationSubject {
    var value: Value
    var transcript: StructuredTranscript?
}
```

## Topics

### Associated Types
- [associatedtype Value : Decodable, Encodable](evaluationsubject/value-swift.associatedtype.md)
  The type of the value produced by the system under test.
### Instance Properties
- [var value: Self.Value](evaluationsubject/value-swift.property.md)
  The typed value produced by the system under test.

## Relationships

### Conforming Types
- [ModelSubject](modelsubject.md)

## See Also

- [associatedtype Subject : EvaluationSubject](evaluation/subject.md)
  The type of the subject produced by the system under test.
- [func subject(from: Self.Sample) async throws -> Self.Subject](evaluation/subject(from:).md)
  Produces the subject of evaluation from a given sample.
- [struct ModelSubject](modelsubject.md)
  The subject type for language model evaluations.
- [var name: String](evaluation/name.md)
  The default name, derived from the type name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationsubject)*