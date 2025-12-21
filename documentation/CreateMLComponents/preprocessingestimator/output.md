# PreprocessingEstimator.Output

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

- [func preprocessed<S>(from: S, eventHandler: EventHandler?) async throws -> [Preprocessor.Output]](preprocessingestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> PreprocessingEstimator<Preprocessor, Estimator>.Transformer](preprocessingestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a sequence of examples.
- [func fitted<S>(toPreprocessed: S, eventHandler: EventHandler?) async throws -> PreprocessingEstimator<Preprocessor, Estimator>.Transformer](preprocessingestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [PreprocessingEstimator.Input](preprocessingestimator/input.md)
  The input type.
- [PreprocessingEstimator.Intermediate](preprocessingestimator/intermediate.md)
  The intermediate type.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingestimator/output)*