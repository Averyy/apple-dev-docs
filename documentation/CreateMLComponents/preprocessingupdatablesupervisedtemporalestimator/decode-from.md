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
func decode(from decoder: inout any EstimatorDecoder) throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer
```

## See Also

- [func encode(PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatablesupervisedtemporalestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatablesupervisedtemporalestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtemporalestimator/decode(from:))*