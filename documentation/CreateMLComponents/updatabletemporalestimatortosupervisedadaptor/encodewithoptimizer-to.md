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
func encodeWithOptimizer(_ transformer: UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## Parameters

- `transformer`: A transformer this estimator creates.
- `encoder`: An encoder.

## See Also

- [func encode(UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](updatabletemporalestimatortosupervisedadaptor/encode(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletemporalestimatortosupervisedadaptor/decode(from:).md)
  Returns the pre-defined transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletemporalestimatortosupervisedadaptor/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimatortosupervisedadaptor/encodewithoptimizer(_:to:))*