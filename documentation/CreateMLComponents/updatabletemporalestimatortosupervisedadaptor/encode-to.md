# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method

Does nothing since this estimator uses a pre-defined transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func encode(_ transformer: UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## See Also

- [func decode(from: inout any EstimatorDecoder) throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletemporalestimatortosupervisedadaptor/decode(from:).md)
  Returns the pre-defined transformer.
- [func encodeWithOptimizer(UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](updatabletemporalestimatortosupervisedadaptor/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletemporalestimatortosupervisedadaptor/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimatortosupervisedadaptor/encode(_:to:))*