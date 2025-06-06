# decode(from:)

**Framework**: Create ML Components  
**Kind**: method

Decodes a previously fitted transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func decode(from decoder: inout any EstimatorDecoder) throws -> PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer
```

## See Also

- [func encode(PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatabletemporalestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func encodeWithOptimizer(PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatabletemporalestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletemporalestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletemporalestimator/decode(from:))*