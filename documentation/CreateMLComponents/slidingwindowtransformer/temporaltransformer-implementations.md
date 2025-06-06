# TemporalTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](slidingwindowtransformer/adaptedasestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](slidingwindowtransformer/adaptedasupdatableestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, SupervisedEstimatorToTemporalAdaptor<Other>>](slidingwindowtransformer/appending(_:)-1tbf9.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, UpdatableSupervisedEstimatorToTemporalAdaptor<Other>>](slidingwindowtransformer/appending(_:)-296ef.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, Other>](slidingwindowtransformer/appending(_:)-2vlsn.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TransformerToTemporalAdaptor<Other>>](slidingwindowtransformer/appending(_:)-65lzx.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, Other>](slidingwindowtransformer/appending(_:)-6vryi.md)
  Composes this temporal transformer with a temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, Other>](slidingwindowtransformer/appending(_:)-7vjb6.md)
  Composes this temporal transformer with another temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, Other>](slidingwindowtransformer/appending(_:)-7ykih.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, UpdatableEstimatorToTemporalAdaptor<Other>>](slidingwindowtransformer/appending(_:)-867t3.md)
  Composes this temporal transformer with an updatable estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TemporalAdaptor<Other>>](slidingwindowtransformer/appending(_:)-8bl20.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, EstimatorToTemporalAdaptor<Other>>](slidingwindowtransformer/appending(_:)-9pi1h.md)
  Composes this temporal transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, Other>](slidingwindowtransformer/appending(_:)-yjjf.md)
  Composes this temporal transformer with an updatable temporal estimator.
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](slidingwindowtransformer/applied(to:eventhandler:)-2iy21.md)
  Performs the transformation on a sequence of input sequences.
- [func applied<S, TS, Annotation>(to: S, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<Self.OutputSequence, Annotation>]](slidingwindowtransformer/applied(to:eventhandler:)-4qz21.md)
  Performs the transformation on a sequence of annotated input sequences.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](slidingwindowtransformer/callasfunction(_:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](slidingwindowtransformer/callasfunction(to:eventhandler:).md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](slidingwindowtransformer/export(to:).md)
  Exports this temporal transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](slidingwindowtransformer/export(to:metadata:).md)
  Exports this temporal transformer as a CoreML model with user-supplied metadata.
- [func prediction<S, Label>(from: S) async throws -> Self.OutputSequence](slidingwindowtransformer/prediction(from:).md)
  Performs a prediction on a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindowtransformer/temporaltransformer-implementations)*