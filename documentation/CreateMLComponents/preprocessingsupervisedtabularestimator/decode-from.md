# decode(from:)

**Framework**: Create ML Components  
**Kind**: method

Decodes a previously fitted transformer.

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
func decode(from decoder: inout any EstimatorDecoder) throws -> PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer
```

## See Also

- [func encode(PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingsupervisedtabularestimator/encode(_:to:).md)
  Encodes a fitted transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtabularestimator/decode(from:))*