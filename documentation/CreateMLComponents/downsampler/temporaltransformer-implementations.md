# TemporalTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](downsampler/adaptedasestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](downsampler/adaptedasupdatableestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, UpdatableEstimatorToTemporalAdaptor<Other>>](downsampler/appending(_:)-2nza2.md)
  Composes this temporal transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, SupervisedEstimatorToTemporalAdaptor<Other>>](downsampler/appending(_:)-3g84e.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, Other>](downsampler/appending(_:)-4d0jx.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TemporalAdaptor<Other>>](downsampler/appending(_:)-4vs5n.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, Other>](downsampler/appending(_:)-4x719.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, Other>](downsampler/appending(_:)-532g7.md)
  Composes this temporal transformer with another temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, UpdatableSupervisedEstimatorToTemporalAdaptor<Other>>](downsampler/appending(_:)-5keoj.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TransformerToTemporalAdaptor<Other>>](downsampler/appending(_:)-6tyqh.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, Other>](downsampler/appending(_:)-8cac2.md)
  Composes this temporal transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, EstimatorToTemporalAdaptor<Other>>](downsampler/appending(_:)-9g9hk.md)
  Composes this temporal transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, Other>](downsampler/appending(_:)-c3u1.md)
  Composes this temporal transformer with an updatable temporal estimator.
- [func applied<S, TS, Annotation>(to: S, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<Self.OutputSequence, Annotation>]](downsampler/applied(to:eventhandler:)-7v8zl.md)
  Performs the transformation on a sequence of annotated input sequences.
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](downsampler/applied(to:eventhandler:)-8z382.md)
  Performs the transformation on a sequence of input sequences.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](downsampler/callasfunction(_:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](downsampler/callasfunction(to:eventhandler:).md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](downsampler/export(to:).md)
  Exports this temporal transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](downsampler/export(to:metadata:).md)
  Exports this temporal transformer as a CoreML model with user-supplied metadata.
- [func prediction<S, Label>(from: S) async throws -> Self.OutputSequence](downsampler/prediction(from:).md)
  Performs a prediction on a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/downsampler/temporaltransformer-implementations)*