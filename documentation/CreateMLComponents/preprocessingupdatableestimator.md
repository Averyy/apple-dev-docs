# PreprocessingUpdatableEstimator

**Framework**: Create ML Components  
**Kind**: struct

An updatable estimator that composes a preprocessing transformer and an updatable estimator.

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
struct PreprocessingUpdatableEstimator<Preprocessor, Estimator> where Preprocessor : Transformer, Estimator : UpdatableEstimator, Preprocessor.Output == Estimator.Transformer.Input
```

## Topics

### Creating an estimator
- [init(Preprocessor, Estimator)](preprocessingupdatableestimator/init(_:_:).md)
  Creates a composed updatable estimator from a preprocessing transformer and an estimator.
### Getting the properties
- [var estimator: Estimator](preprocessingupdatableestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingupdatableestimator/preprocessor.md)
  The preprocessing transformer.
### Encoding and decoding
- [func encode(PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatableestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatableestimator/decode(from:).md)
  Decodes a previously fitted transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatableestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer.
- [func encodeWithOptimizer(PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatableestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
### Preprocesing and fitting
- [func preprocessed<S>(from: S, eventHandler: EventHandler?) async throws -> [Preprocessor.Output]](preprocessingupdatableestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatableestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a sequence of examples.
- [func fitted<S>(toPreprocessed: S, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatableestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
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
### Default Implementations
- [Estimator Implementations](preprocessingupdatableestimator/estimator-implementations.md)
- [UpdatableEstimator Implementations](preprocessingupdatableestimator/updatableestimator-implementations.md)

## Relationships

### Conforms To
- [Estimator](estimator.md)
- [Sendable](../Swift/Sendable.md)
- [UpdatableEstimator](updatableestimator.md)

## See Also

- [struct PreprocessingEstimator](preprocessingestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingTemporalEstimator](preprocessingtemporalestimator.md)
  A temporal estimator that composes a preprocessing transformer and a temporal estimator.
- [struct PreprocessingSupervisedEstimator](preprocessingsupervisedestimator.md)
  A supervised estimator that composes a preprocessing transformer and a supervised estimator.
- [struct PreprocessingSupervisedTemporalEstimator](preprocessingsupervisedtemporalestimator.md)
  A supervised temporal estimator that composes a preprocessing transformer and a supervised temporal estimator.
- [struct PreprocessingUpdatableTemporalEstimator](preprocessingupdatabletemporalestimator.md)
  An updatable temporal estimator that composes a preprocessing transformer and an updatable temporal estimator.
- [struct PreprocessingUpdatableSupervisedEstimator](preprocessingupdatablesupervisedestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableSupervisedTemporalEstimator](preprocessingupdatablesupervisedtemporalestimator.md)
  An updatable supervised temporal estimator that composes a preprocessing transformer and an updatable supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatableestimator)*