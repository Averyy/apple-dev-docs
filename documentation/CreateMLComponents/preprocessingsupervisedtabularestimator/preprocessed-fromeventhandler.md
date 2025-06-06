# preprocessed(from:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Preprocesses a data frame of examples.

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
func preprocessed(from input: DataFrame, eventHandler: EventHandler? = nil) async throws -> DataFrame
```

#### Return Value

The preprocessed examples.

## Parameters

- `input`: A data frame of examples.
- `eventHandler`: An event handler.

## See Also

- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtabularestimator/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a data frame
- [func fitted(toPreprocessed: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtabularestimator/fitted(topreprocessed:validateon:eventhandler:).md)
  Fits a transformer to a data frame of preprocessed examples while validating.
- [PreprocessingSupervisedTabularEstimator.Annotation](preprocessingsupervisedtabularestimator/annotation.md)
  The annotation type.
- [PreprocessingSupervisedTabularEstimator.Input](preprocessingsupervisedtabularestimator/input.md)
  The input type.
- [PreprocessingSupervisedTabularEstimator.Intermediate](preprocessingsupervisedtabularestimator/intermediate.md)
  The intermediate type.
- [PreprocessingSupervisedTabularEstimator.Output](preprocessingsupervisedtabularestimator/output.md)
  The output type.
- [PreprocessingSupervisedTabularEstimator.Transformer](preprocessingsupervisedtabularestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtabularestimator/preprocessed(from:eventhandler:))*