# PreprocessingTemporalEstimator.Input

**Framework**: Create ML Components  
**Kind**: typealias

The input type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
typealias Input = Preprocessor.Input
```

## See Also

- [func preprocessed<InputSequence>(from: InputSequence, eventHandler: EventHandler?) async throws -> [PreprocessedFeatureSequence<Preprocessor.Output>]](preprocessingtemporalestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingtemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted(toPreprocessed: [PreprocessedFeatureSequence<Preprocessor.Output>], eventHandler: EventHandler?) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingtemporalestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [PreprocessingTemporalEstimator.Intermediate](preprocessingtemporalestimator/intermediate.md)
  The intermediate type.
- [PreprocessingTemporalEstimator.Output](preprocessingtemporalestimator/output.md)
  The output type.
- [PreprocessingTemporalEstimator.Transformer](preprocessingtemporalestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtemporalestimator/input)*