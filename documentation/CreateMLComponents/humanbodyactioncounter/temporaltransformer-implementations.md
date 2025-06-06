# TemporalTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](humanbodyactioncounter/adaptedasestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](humanbodyactioncounter/adaptedasupdatableestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, Other>](humanbodyactioncounter/appending(_:)-1nmn.md)
  Composes this temporal transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, Other>](humanbodyactioncounter/appending(_:)-1u6h.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, Other>](humanbodyactioncounter/appending(_:)-3vg2u.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, UpdatableEstimatorToTemporalAdaptor<Other>>](humanbodyactioncounter/appending(_:)-49j0f.md)
  Composes this temporal transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, UpdatableSupervisedEstimatorToTemporalAdaptor<Other>>](humanbodyactioncounter/appending(_:)-49qfq.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, SupervisedEstimatorToTemporalAdaptor<Other>>](humanbodyactioncounter/appending(_:)-5nfgo.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TemporalAdaptor<Other>>](humanbodyactioncounter/appending(_:)-5tr9x.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TransformerToTemporalAdaptor<Other>>](humanbodyactioncounter/appending(_:)-6y6ap.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, EstimatorToTemporalAdaptor<Other>>](humanbodyactioncounter/appending(_:)-73e92.md)
  Composes this temporal transformer with an estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, Other>](humanbodyactioncounter/appending(_:)-86pf7.md)
  Composes this temporal transformer with another temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, Other>](humanbodyactioncounter/appending(_:)-lxaf.md)
  Composes this temporal transformer with an updatable temporal estimator.
- [func applied<S, TS, Annotation>(to: S, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<Self.OutputSequence, Annotation>]](humanbodyactioncounter/applied(to:eventhandler:)-3bm2t.md)
  Performs the transformation on a sequence of annotated input sequences.
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](humanbodyactioncounter/applied(to:eventhandler:)-4k94q.md)
  Performs the transformation on a sequence of input sequences.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](humanbodyactioncounter/callasfunction(_:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](humanbodyactioncounter/callasfunction(to:eventhandler:).md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](humanbodyactioncounter/export(to:).md)
  Exports this temporal transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](humanbodyactioncounter/export(to:metadata:).md)
  Exports this temporal transformer as a CoreML model with user-supplied metadata.
- [func prediction<S, Label>(from: S) async throws -> Self.OutputSequence](humanbodyactioncounter/prediction(from:).md)
  Performs a prediction on a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactioncounter/temporaltransformer-implementations)*