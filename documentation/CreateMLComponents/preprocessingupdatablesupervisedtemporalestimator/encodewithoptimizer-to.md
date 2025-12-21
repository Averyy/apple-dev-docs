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
func encodeWithOptimizer(_ transformer: PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer, to encoder: inout any EstimatorEncoder) throws
```

## Parameters

- `transformer`: A transformer this estimator creates.
- `encoder`: An encoder.

## See Also

- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtemporalestimator/encodewithoptimizer(_:to:))*