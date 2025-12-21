# PreprocessingUpdatableSupervisedTabularEstimator.Annotation

**Framework**: Create ML Components  
**Kind**: typealias

The annotation type.

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
typealias Annotation = Estimator.Annotation
```

## See Also

- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/fitted(to:validateon:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func fitted(toPreprocessed: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/fitted(topreprocessed:validateon:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func makeTransformer() -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](preprocessingupdatablesupervisedtabularestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a data frame.
- [func update(inout PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedtabularestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new data frame of examples.
- [func update(inout PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: DataFrame, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedtabularestimator/update(_:withpreprocessed:eventhandler:).md)
  Updates a transformer with a new data frame of preprocessed features.
- [PreprocessingUpdatableSupervisedTabularEstimator.Input](preprocessingupdatablesupervisedtabularestimator/input.md)
  The input type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Intermediate](preprocessingupdatablesupervisedtabularestimator/intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Output](preprocessingupdatablesupervisedtabularestimator/output.md)
  The output type.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtabularestimator/annotation)*