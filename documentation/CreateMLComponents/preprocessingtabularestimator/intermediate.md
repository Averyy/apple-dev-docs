# PreprocessingTabularEstimator.Intermediate

**Framework**: Create ML Components  
**Kind**: typealias

The intermediate type.

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
typealias Intermediate = Preprocessor.Output
```

## See Also

- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](preprocessingtabularestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a data frame of examples.
- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> PreprocessingTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingtabularestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func fitted(toPreprocessed: DataFrame, eventHandler: EventHandler?) async throws -> PreprocessingTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingtabularestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a data frame of preprocessed features.
- [PreprocessingTabularEstimator.Input](preprocessingtabularestimator/input.md)
  The input type.
- [PreprocessingTabularEstimator.Output](preprocessingtabularestimator/output.md)
  The output type.
- [PreprocessingTabularEstimator.Transformer](preprocessingtabularestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtabularestimator/intermediate)*