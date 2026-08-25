# Evaluator

**Framework**: Evaluations  
**Kind**: struct

A closure-based evaluator.

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
struct Evaluator<Input> where Input : SampleProtocol, Input.ExpectedValue : Decodable, Input.ExpectedValue : Encodable, Input.ExpectedValue : Sendable
```

## Mentions

- [Designing specific, measurable criteria in an evaluation suite](designing-evaluation-criteria.md)

#### Overview

Use Evaluator to create inline evaluators without defining a custom type. The closure receives the input sample and the [`ModelSubject`](modelsubject.md), providing access to both .value and .transcript.

```swift
Evaluator { sample, subject in
    let metric = Metric("TitleMatch")
    guard let expected = sample.expected else { return metric.ignore() }
    return subject.value == expected ? metric.passing() : metric.failing()
}
```

## Topics

### Initializers
- [init(nonisolated(nonsending) (Input, ModelSubject<Input.ExpectedValue>) async throws -> Metric)](evaluator/init(_:).md)
  Creates an evaluator with the given evaluation closure.
### Instance Methods
- [func metrics(subject: ModelSubject<Input.ExpectedValue>, input: Input) async throws -> [Metric]](evaluator/metrics(subject:input:).md)
  Evaluates the input and returns an array of metrics.

## Relationships

### Conforms To
- [EvaluatorProtocol](evaluatorprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Designing specific, measurable criteria in an evaluation suite](designing-evaluation-criteria.md)
  Define quality for your feature by choosing measurable criteria, scoring approaches, and ground-truth strategies.
- [struct Metric](metric.md)
  A named metric that carries a result value.
- [struct MetricsAggregator](metricsaggregator.md)
  A utility for computing aggregate statistics from evaluation metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluator)*