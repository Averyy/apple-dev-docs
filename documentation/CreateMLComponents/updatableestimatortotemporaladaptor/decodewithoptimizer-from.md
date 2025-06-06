# decodeWithOptimizer(from:)

**Framework**: Create ML Components  
**Kind**: method

Reads the encoded transformer and optimizer with a decoder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func decodeWithOptimizer(from decoder: inout any EstimatorDecoder) throws -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer
```

#### Return Value

The decoded transformer.

## Parameters

- `decoder`: A decoder.

## See Also

- [func encode(UpdatableEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](updatableestimatortotemporaladaptor/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](updatableestimatortotemporaladaptor/decode(from:).md)
  Decodes the transformer.
- [func encodeWithOptimizer(UpdatableEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](updatableestimatortotemporaladaptor/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortotemporaladaptor/decodewithoptimizer(from:))*