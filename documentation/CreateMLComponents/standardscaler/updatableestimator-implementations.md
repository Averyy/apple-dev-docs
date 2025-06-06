# UpdatableEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> UpdatableEstimatorToSupervisedAdaptor<Self, Annotation>](standardscaler/adaptedassupervised(annotationtype:)-906as.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> UpdatableEstimatorToTemporalAdaptor<Self>](standardscaler/adaptedastemporal-5oojr.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](standardscaler/appending(_:)-19rwc.md)
  Composes this updatable estimator with another updatable estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](standardscaler/appending(_:)-2v4bi.md)
  Composes this updatable estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](standardscaler/appending(_:)-2vxol.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](standardscaler/appending(_:)-4f6lm.md)
  Composes this updatable estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other>>
](standardscaler/appending(_:)-5z8jp.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](standardscaler/appending(_:)-8zs0q.md)
  Composes this updatable estimator with a temporal transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> StandardScaler<Element>.Transformer](standardscaler/decodewithoptimizer(from:).md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(StandardScaler<Element>.Transformer, to: inout any EstimatorEncoder) throws](standardscaler/encodewithoptimizer(_:to:).md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> StandardScaler<Element>.Transformer](standardscaler/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](standardscaler/update(_:with:).md)
- [func update(inout StandardScaler<Element>.Transformer, with: some Sequence<Element>, eventHandler: EventHandler?)](standardscaler/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/standardscaler/updatableestimator-implementations)*