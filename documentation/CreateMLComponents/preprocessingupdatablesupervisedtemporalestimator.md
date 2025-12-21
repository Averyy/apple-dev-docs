# PreprocessingUpdatableSupervisedTemporalEstimator

**Framework**: Create ML Components  
**Kind**: struct

An updatable supervised temporal estimator that composes a preprocessing transformer and an updatable supervised temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator> where Preprocessor : TemporalTransformer, Estimator : UpdatableSupervisedTemporalEstimator, Preprocessor.Output == Estimator.Transformer.Input
```

## Topics

### Creating an estimator
- [init(Preprocessor, Estimator)](preprocessingupdatablesupervisedtemporalestimator/init(_:_:).md)
  Creates a composed supervised temporal estimator from a preprocessing transformer and a supervised temporal estimator.
### Getting the properties
- [var estimator: Estimator](preprocessingupdatablesupervisedtemporalestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingupdatablesupervisedtemporalestimator/preprocessor.md)
  The preprocessing transformer.
### Encoding and decoding
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatablesupervisedtemporalestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
### Preprocesing and fitting
- [func preprocessed<InputSequence, FeatureSequence>(from: InputSequence, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>]](preprocessingupdatablesupervisedtemporalestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted(toPreprocessed: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [func fitted(toPreprocessed: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], validateOn: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/fitted(topreprocessed:validateon:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features while validating.
- [func makeTransformer() -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence, FeatureSequence>(inout PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedtemporalestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence, FeatureSequence>(inout PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: InputSequence, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedtemporalestimator/update(_:withpreprocessed:eventhandler:).md)
  Updates a transformer with a new sequence of preprocessed features.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Annotation](preprocessingupdatablesupervisedtemporalestimator/annotation.md)
  The annotation type.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Input](preprocessingupdatablesupervisedtemporalestimator/input.md)
  The input type.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Intermediate](preprocessingupdatablesupervisedtemporalestimator/intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Output](preprocessingupdatablesupervisedtemporalestimator/output.md)
  The output type.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SupervisedTemporalEstimator](supervisedtemporalestimator.md)
- [UpdatableSupervisedTemporalEstimator](updatablesupervisedtemporalestimator.md)

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
- [struct PreprocessingUpdatableSupervisedEstimator](preprocessingupdatablesupervisedestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtemporalestimator)*