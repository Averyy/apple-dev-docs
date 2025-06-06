# preprocessed(from:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Preprocesses a sequence of examples.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func preprocessed<InputSequence>(from input: InputSequence, eventHandler: EventHandler? = nil) async throws -> [PreprocessedFeatureSequence<Preprocessor.Output>] where InputSequence : Sequence, Preprocessor.Input == InputSequence.Element.Feature, InputSequence.Element : TemporalSequence
```

#### Return Value

The preprocessed examples.

## Parameters

- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingtemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted(toPreprocessed: [PreprocessedFeatureSequence<Preprocessor.Output>], eventHandler: EventHandler?) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingtemporalestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [PreprocessingTemporalEstimator.Input](preprocessingtemporalestimator/input.md)
  The input type.
- [PreprocessingTemporalEstimator.Intermediate](preprocessingtemporalestimator/intermediate.md)
  The intermediate type.
- [PreprocessingTemporalEstimator.Output](preprocessingtemporalestimator/output.md)
  The output type.
- [PreprocessingTemporalEstimator.Transformer](preprocessingtemporalestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtemporalestimator/preprocessed(from:eventhandler:))*