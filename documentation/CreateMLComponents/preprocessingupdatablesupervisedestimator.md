# PreprocessingUpdatableSupervisedEstimator

**Framework**: Create ML Components  
**Kind**: struct

An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.

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
struct PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator> where Preprocessor : Transformer, Estimator : UpdatableSupervisedEstimator, Preprocessor.Output == Estimator.Transformer.Input
```

## Topics

### Creating the estimator
- [init(Preprocessor, Estimator)](preprocessingupdatablesupervisedestimator/init(_:_:).md)
  Creates a composed supervised estimator from a preprocessing transformer and a supervised estimator.
### Getting the properties
- [var estimator: Estimator](preprocessingupdatablesupervisedestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingupdatablesupervisedestimator/preprocessor.md)
  The preprocessing transformer.
### Encoding and decoding
- [func encode(PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatablesupervisedestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedestimator/decode(from:).md)
  Decodes a previously fitted transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatablesupervisedestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
### Preprocesing and fitting
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
- [PreprocessingUpdatableSupervisedEstimator.Output](preprocessingupdatablesupervisedestimator/output.md)
  The output type.
- [PreprocessingUpdatableSupervisedEstimator.Transformer](preprocessingupdatablesupervisedestimator/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedEstimator Implementations](preprocessingupdatablesupervisedestimator/supervisedestimator-implementations.md)
- [UpdatableSupervisedEstimator Implementations](preprocessingupdatablesupervisedestimator/updatablesupervisedestimator-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SupervisedEstimator](supervisedestimator.md)
- [UpdatableSupervisedEstimator](updatablesupervisedestimator.md)

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
- [struct PreprocessingUpdatableTemporalEstimator](preprocessingupdatabletemporalestimator.md)
  An updatable temporal estimator that composes a preprocessing transformer and an updatable temporal estimator.
- [struct PreprocessingUpdatableSupervisedTemporalEstimator](preprocessingupdatablesupervisedtemporalestimator.md)
  An updatable supervised temporal estimator that composes a preprocessing transformer and an updatable supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedestimator)*