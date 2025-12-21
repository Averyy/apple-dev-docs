# PreprocessingSupervisedTabularEstimator.Annotation

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

- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](preprocessingsupervisedtabularestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a data frame of examples.
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtabularestimator/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a data frame
- [func fitted(toPreprocessed: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtabularestimator/fitted(topreprocessed:validateon:eventhandler:).md)
  Fits a transformer to a data frame of preprocessed examples while validating.
- [PreprocessingSupervisedTabularEstimator.Input](preprocessingsupervisedtabularestimator/input.md)
  The input type.
- [PreprocessingSupervisedTabularEstimator.Intermediate](preprocessingsupervisedtabularestimator/intermediate.md)
  The intermediate type.
- [PreprocessingSupervisedTabularEstimator.Output](preprocessingsupervisedtabularestimator/output.md)
  The output type.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtabularestimator/annotation)*