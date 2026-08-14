# SampleProtocol

**Framework**: Evaluations  
**Kind**: protocol

A type that defines evaluation samples.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol SampleProtocol : Decodable, Encodable, Sendable
```

#### Overview

```swift
struct MySample: SampleProtocol {
    var input: String
    var expected: String?
}
```

Conform to this protocol to define input samples for your evaluation datasets. Each sample has an input that’s displayed in the DataFrame “Input” column, and an optional expected value for comparison.

For language model evaluations, use [`ModelSampleProtocol`](modelsampleprotocol.md) which extends this protocol with language-model-specific properties: prompt, instructions, and expectations.

```swift
let samples = [
    ModelSample(prompt: "Classify: I love this!", expected: "positive"),
]
```

## Topics

### Associated Types
- [associatedtype ExpectedValue](sampleprotocol/expectedvalue.md)
  The type of the expected output value.
- [associatedtype Input : CustomStringConvertible](sampleprotocol/input-swift.associatedtype.md)
  The type of the input data.
### Instance Properties
- [var expected: Self.ExpectedValue?](sampleprotocol/expected.md)
  The expected output for comparison.
- [var input: Self.Input](sampleprotocol/input-swift.property.md)
  The input data for this sample, shown in the “Input” DataFrame column.

## Relationships

### Inherits From
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Inherited By
- [ModelSampleProtocol](modelsampleprotocol.md)
### Conforming Types
- [ModelSample](modelsample.md)

## See Also

- [protocol ModelSampleProtocol](modelsampleprotocol.md)
  A type that defines language model evaluation samples with prompt, instructions, and expectations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/sampleprotocol)*