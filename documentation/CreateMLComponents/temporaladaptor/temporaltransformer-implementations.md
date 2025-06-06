# TemporalTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](temporaladaptor/adaptedasestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](temporaladaptor/adaptedasupdatableestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TemporalAdaptor<Other>>](temporaladaptor/appending(_:)-1d3rm.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, Other>](temporaladaptor/appending(_:)-2ocdj.md)
  Composes this temporal transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, SupervisedEstimatorToTemporalAdaptor<Other>>](temporaladaptor/appending(_:)-3ouhi.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, UpdatableSupervisedEstimatorToTemporalAdaptor<Other>>](temporaladaptor/appending(_:)-3umk1.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, Other>](temporaladaptor/appending(_:)-3wmpt.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, UpdatableEstimatorToTemporalAdaptor<Other>>](temporaladaptor/appending(_:)-5jvwd.md)
  Composes this temporal transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, Other>](temporaladaptor/appending(_:)-5llyq.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, EstimatorToTemporalAdaptor<Other>>](temporaladaptor/appending(_:)-5s0ps.md)
  Composes this temporal transformer with an estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TransformerToTemporalAdaptor<Other>>](temporaladaptor/appending(_:)-6wbti.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, Other>](temporaladaptor/appending(_:)-7nj7k.md)
  Composes this temporal transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, Other>](temporaladaptor/appending(_:)-9g4bj.md)
  Composes this temporal transformer with another temporal transformer.
- [func applied<S, TS, Annotation>(to: S, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<Self.OutputSequence, Annotation>]](temporaladaptor/applied(to:eventhandler:)-2jzvj.md)
  Performs the transformation on a sequence of annotated input sequences.
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](temporaladaptor/applied(to:eventhandler:)-5l89e.md)
  Performs the transformation on a sequence of input sequences.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](temporaladaptor/callasfunction(_:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](temporaladaptor/callasfunction(to:eventhandler:).md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](temporaladaptor/export(to:).md)
  Exports this temporal transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](temporaladaptor/export(to:metadata:).md)
  Exports this temporal transformer as a CoreML model with user-supplied metadata.
- [func prediction<S, Label>(from: S) async throws -> Self.OutputSequence](temporaladaptor/prediction(from:).md)
  Performs a prediction on a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaladaptor/temporaltransformer-implementations)*