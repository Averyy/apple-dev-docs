# TemporalTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](composedtemporaltransformer/adaptedasestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](composedtemporaltransformer/adaptedasupdatableestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, Other>](composedtemporaltransformer/appending(_:)-1p1n0.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, UpdatableSupervisedEstimatorToTemporalAdaptor<Other>>](composedtemporaltransformer/appending(_:)-2ein3.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TemporalAdaptor<Other>>](composedtemporaltransformer/appending(_:)-317mg.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, Other>](composedtemporaltransformer/appending(_:)-4h937.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, Other>](composedtemporaltransformer/appending(_:)-4jnae.md)
  Composes this temporal transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, EstimatorToTemporalAdaptor<Other>>](composedtemporaltransformer/appending(_:)-5ksvv.md)
  Composes this temporal transformer with an estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TransformerToTemporalAdaptor<Other>>](composedtemporaltransformer/appending(_:)-5s6tf.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, Other>](composedtemporaltransformer/appending(_:)-8hfi2.md)
  Composes this temporal transformer with another temporal transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, Other>](composedtemporaltransformer/appending(_:)-8r1fu.md)
  Composes this temporal transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, SupervisedEstimatorToTemporalAdaptor<Other>>](composedtemporaltransformer/appending(_:)-97p5i.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, UpdatableEstimatorToTemporalAdaptor<Other>>](composedtemporaltransformer/appending(_:)-9fupa.md)
  Composes this temporal transformer with an updatable estimator.
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](composedtemporaltransformer/applied(to:eventhandler:)-6ju6s.md)
  Performs the transformation on a sequence of input sequences.
- [func applied<S, TS, Annotation>(to: S, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<Self.OutputSequence, Annotation>]](composedtemporaltransformer/applied(to:eventhandler:)-9uj3w.md)
  Performs the transformation on a sequence of annotated input sequences.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](composedtemporaltransformer/callasfunction(_:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](composedtemporaltransformer/callasfunction(to:eventhandler:).md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](composedtemporaltransformer/export(to:).md)
  Exports this temporal transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](composedtemporaltransformer/export(to:metadata:).md)
  Exports this temporal transformer as a CoreML model with user-supplied metadata.
- [func prediction<S, Label>(from: S) async throws -> Self.OutputSequence](composedtemporaltransformer/prediction(from:).md)
  Performs a prediction on a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtemporaltransformer/temporaltransformer-implementations)*