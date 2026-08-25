# ModelSampleProtocol

**Framework**: Evaluations  
**Kind**: protocol

A type that defines language model evaluation samples with prompt, instructions, and expectations.

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
protocol ModelSampleProtocol : SampleProtocol where Self.ExpectedValue : Decodable, Self.ExpectedValue : Encodable, Self.ExpectedValue : Sendable
```

#### Overview

Extends [`SampleProtocol`](sampleprotocol.md) with prompt, instructions, and evaluation expectations. Use [`ModelSample`](modelsample.md) for the common case; create custom conformances when you need additional properties.

```swift
let sample = ModelSample(
    prompt: "What's the weather?",
    expected: "Sunny",
    expectations: TrajectoryExpectation(ordered: [
        ToolExpectation("get_weather")
    ])
)
```

## Topics

### Associated Types
- [associatedtype Expectation : Decodable, Encodable, Sendable](modelsampleprotocol/expectation.md)
  The type of evaluation expectations.
### Instance Properties
- [var input: ModelSampleInput](modelsampleprotocol/input.md)
  The bundled language model input, including prompt, instructions, and schema.
- [var output: ModelSampleOutput<Self.ExpectedValue, Self.Expectation>](modelsampleprotocol/output.md)
  The expected output value and evaluation expectations.

## Relationships

### Inherits From
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [SampleProtocol](sampleprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Conforming Types
- [ModelSample](modelsample.md)

## See Also

- [protocol SampleProtocol](sampleprotocol.md)
  A type that defines evaluation samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsampleprotocol)*