# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method

Encodes a fitted transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func encode(_ transformer: PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## See Also

- [func decode(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatableestimator/decode(from:).md)
  Decodes a previously fitted transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatableestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer.
- [func encodeWithOptimizer(PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatableestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatableestimator/encode(_:to:))*