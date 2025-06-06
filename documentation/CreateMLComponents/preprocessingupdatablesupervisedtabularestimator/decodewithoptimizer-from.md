# decodeWithOptimizer(from:)

**Framework**: Create ML Components  
**Kind**: method

Reads the encoded transformer and optimizer with a decoder.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func decodeWithOptimizer(from decoder: inout any EstimatorDecoder) throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer
```

#### Return Value

The decoded transformer.

## Parameters

- `decoder`: A decoder.

## See Also

- [func encode(PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatablesupervisedtabularestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/decode(from:).md)
  Decodes a previously fitted transformer.
- [func encodeWithOptimizer(PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatablesupervisedtabularestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtabularestimator/decodewithoptimizer(from:))*