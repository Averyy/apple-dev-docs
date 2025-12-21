# PreprocessingUpdatableTemporalEstimator

**Framework**: Create ML Components  
**Kind**: struct

An updatable temporal estimator that composes a preprocessing transformer and an updatable temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator> where Preprocessor : TemporalTransformer, Estimator : UpdatableTemporalEstimator, Preprocessor.Output == Estimator.Transformer.Input
```

## Topics

### Creating an estimator
- [init(Preprocessor, Estimator)](preprocessingupdatabletemporalestimator/init(_:_:).md)
  Creates a composed temporal estimator from a preprocessing transformer and a temporal estimator.
### Getting the properties
- [var estimator: Estimator](preprocessingupdatabletemporalestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingupdatabletemporalestimator/preprocessor.md)
  The preprocessing transformer.
### Encoding and decoding
- [func encodeWithOptimizer(PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatabletemporalestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletemporalestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
### Preprocesing and fitting
- [func preprocessed<InputSequence>(from: InputSequence, eventHandler: EventHandler?) async throws -> [PreprocessedFeatureSequence<Preprocessor.Output>]](preprocessingupdatabletemporalestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted(toPreprocessed: [PreprocessedFeatureSequence<Preprocessor.Output>], eventHandler: EventHandler?) async throws -> PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletemporalestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [func update<InputSequence>(inout PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: InputSequence, eventHandler: EventHandler?) async throws](preprocessingupdatabletemporalestimator/update(_:withpreprocessed:eventhandler:).md)
  Updates a transformer with a new sequence of preprocessed features.
- [func update<InputSequence>(inout PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](preprocessingupdatabletemporalestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func makeTransformer() -> PreprocessingUpdatableTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletemporalestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [PreprocessingUpdatableTemporalEstimator.Input](preprocessingupdatabletemporalestimator/input.md)
  The input type.
- [PreprocessingUpdatableTemporalEstimator.Intermediate](preprocessingupdatabletemporalestimator/intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableTemporalEstimator.Output](preprocessingupdatabletemporalestimator/output.md)
  The output type.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalEstimator](temporalestimator.md)
- [UpdatableTemporalEstimator](updatabletemporalestimator.md)

## See Also

- [struct PreprocessingEstimator](preprocessingestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingTemporalEstimator](preprocessingtemporalestimator.md)
  A temporal estimator that composes a preprocessing transformer and a temporal estimator.
- [struct PreprocessingSupervisedEstimator](preprocessingsupervisedestimator.md)
  A supervised estimator that composes a preprocessing transformer and a supervised estimator.
- [struct PreprocessingSupervisedTemporalEstimator](preprocessingsupervisedtemporalestimator.md)
  A supervised temporal estimator that composes a preprocessing transformer and a supervised temporal estimator.
- [struct PreprocessingUpdatableEstimator](preprocessingupdatableestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.
- [struct PreprocessingUpdatableSupervisedEstimator](preprocessingupdatablesupervisedestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableSupervisedTemporalEstimator](preprocessingupdatablesupervisedtemporalestimator.md)
  An updatable supervised temporal estimator that composes a preprocessing transformer and an updatable supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletemporalestimator)*