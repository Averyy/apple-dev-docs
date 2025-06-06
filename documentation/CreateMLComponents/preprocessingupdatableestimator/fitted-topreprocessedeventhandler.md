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
- watchOS 11.0+

## Declaration

```swift
func fitted<S>(toPreprocessed preprocessed: S, eventHandler: EventHandler? = nil) async throws -> PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer where S : Sequence, Preprocessor.Output == S.Element, S.Element == Estimator.Transformer.Input
```

#### Return Value

The fitted transformer.

## Parameters

- `preprocessed`: A sequence of preprocessed features.
- `eventHandler`: An event handler.

## See Also

- [func preprocessed<S>(from: S, eventHandler: EventHandler?) async throws -> [Preprocessor.Output]](preprocessingupdatableestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatableestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a sequence of examples.
- [func makeTransformer() -> PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatableestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](preprocessingupdatableestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence>(inout PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: InputSequence, eventHandler: EventHandler?) async throws](preprocessingupdatableestimator/update(_:withpreprocessed:eventhandler:).md)
  Updates a transformer with a new sequence of preprocessed features.
- [PreprocessingUpdatableEstimator.Input](preprocessingupdatableestimator/input.md)
  The input type.
- [PreprocessingUpdatableEstimator.Intermediate](preprocessingupdatableestimator/intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableEstimator.Output](preprocessingupdatableestimator/output.md)
  The output type.
- [PreprocessingUpdatableEstimator.Transformer](preprocessingupdatableestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatableestimator/fitted(topreprocessed:eventhandler:))*