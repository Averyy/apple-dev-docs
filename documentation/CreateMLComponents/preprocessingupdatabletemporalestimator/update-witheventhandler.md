# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Updates a transformer with a new sequence of examples.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func update<InputSequence>(_ transformer: inout PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer, with input: InputSequence, eventHandler: EventHandler? = nil) async throws where InputSequence : Sequence, Preprocessor.Input == InputSequence.Element.Feature, InputSequence.Element : TemporalSequence
```

## Parameters

- `transformer`: A transformer to update.
- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

- [func preprocessed<InputSequence>(from: InputSequence, eventHandler: EventHandler?) async throws -> [PreprocessedFeatureSequence<Preprocessor.Output>]](preprocessingupdatabletemporalestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted(toPreprocessed: [PreprocessedFeatureSequence<Preprocessor.Output>], eventHandler: EventHandler?) async throws -> PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletemporalestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [func update<InputSequence>(inout PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: InputSequence, eventHandler: EventHandler?) async throws](preprocessingupdatabletemporalestimator/update(_:withpreprocessed:eventhandler:).md)
  Updates a transformer with a new sequence of preprocessed features.
- [func makeTransformer() -> PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletemporalestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [PreprocessingUpdatableTemporalEstimator.Input](preprocessingupdatabletemporalestimator/input.md)
  The input type.
- [PreprocessingUpdatableTemporalEstimator.Intermediate](preprocessingupdatabletemporalestimator/intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableTemporalEstimator.Output](preprocessingupdatabletemporalestimator/output.md)
  The output type.
- [PreprocessingUpdatableTemporalEstimator.Transformer](preprocessingupdatabletemporalestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletemporalestimator/update(_:with:eventhandler:))*