# encodeWithOptimizer(_:to:)

**Framework**: Create ML Components  
**Kind**: method

Encodes the transformer and optimizer to an encoder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func encodeWithOptimizer(_ transformer: UpdatableEstimatorToTemporalAdaptor<Base>.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## Parameters

- `transformer`: A transformer created by this estimator.
- `encoder`: An encoder.

## See Also

- [func encode(UpdatableEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](updatableestimatortotemporaladaptor/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](updatableestimatortotemporaladaptor/decode(from:).md)
  Decodes the transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](updatableestimatortotemporaladaptor/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortotemporaladaptor/encodewithoptimizer(_:to:))*