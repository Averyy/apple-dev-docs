# PreprocessingUpdatableSupervisedEstimator.Output

**Framework**: Create ML Components  
**Kind**: typealias

The output type.

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
typealias Output = Estimator.Transformer.Output
```

## See Also

- [func preprocessed<S>(from: S, eventHandler: EventHandler?) async throws -> AnySequence<AnnotatedFeature<Preprocessor.Output, PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Annotation>>](preprocessingupdatablesupervisedestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a sequence of examples.
- [func fitted<S>(toPreprocessed: S, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [func fitted<InputSequence, Validation>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedestimator/fitted(to:validateon:eventhandler:).md)
  Fits a composed transformer to a sequence of examples.
- [func fitted<InputSequence, Validation>(toPreprocessed: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedestimator/fitted(topreprocessed:validateon:eventhandler:).md)
  Fits a composed transformer to a sequence of examples.
- [func makeTransformer() -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence>(inout PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: InputSequence, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedestimator/update(_:withpreprocessed:eventhandler:).md)
  Updates a transformer with a new sequence of preprocessed features.
- [PreprocessingUpdatableSupervisedEstimator.Annotation](preprocessingupdatablesupervisedestimator/annotation.md)
  The annotation type.
- [PreprocessingUpdatableSupervisedEstimator.Input](preprocessingupdatablesupervisedestimator/input.md)
  The input type.
- [PreprocessingUpdatableSupervisedEstimator.Intermediate](preprocessingupdatablesupervisedestimator/intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableSupervisedEstimator.Transformer](preprocessingupdatablesupervisedestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedestimator/output)*