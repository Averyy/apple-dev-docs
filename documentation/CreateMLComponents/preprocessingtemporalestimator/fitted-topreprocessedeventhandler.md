# fitted(toPreprocessed:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a transformer to a sequence of preprocessed features.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func fitted(toPreprocessed preprocessed: [PreprocessedFeatureSequence<Preprocessor.Output>], eventHandler: EventHandler? = nil) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer
```

#### Return Value

The fitted transformer.

## Parameters

- `preprocessed`: A sequence of preprocessed featuress.
- `eventHandler`: An event handler.

## See Also

- [func preprocessed<InputSequence>(from: InputSequence, eventHandler: EventHandler?) async throws -> [PreprocessedFeatureSequence<Preprocessor.Output>]](preprocessingtemporalestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingtemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [PreprocessingTemporalEstimator.Input](preprocessingtemporalestimator/input.md)
  The input type.
- [PreprocessingTemporalEstimator.Intermediate](preprocessingtemporalestimator/intermediate.md)
  The intermediate type.
- [PreprocessingTemporalEstimator.Output](preprocessingtemporalestimator/output.md)
  The output type.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtemporalestimator/fitted(topreprocessed:eventhandler:))*