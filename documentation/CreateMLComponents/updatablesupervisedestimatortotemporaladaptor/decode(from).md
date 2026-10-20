# decode(from:)

**Framework**: Create ML Components  
**Kind**: method

Decodes the transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func decode(from decoder: inout any EstimatorDecoder) throws -> UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer
```

## See Also

- [func encode(UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](updatablesupervisedestimatortotemporaladaptor/encode(_:to:).md)
  Encodes a fitted transformer.
- [func encodeWithOptimizer(UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](updatablesupervisedestimatortotemporaladaptor/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer](updatablesupervisedestimatortotemporaladaptor/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedestimatortotemporaladaptor/decode(from:))*