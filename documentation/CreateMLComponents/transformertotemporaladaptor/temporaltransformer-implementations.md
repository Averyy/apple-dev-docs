# TemporalTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](transformertotemporaladaptor/adaptedasestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](transformertotemporaladaptor/adaptedasupdatableestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TransformerToTemporalAdaptor<Other>>](transformertotemporaladaptor/appending(_:)-1nqed.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TemporalAdaptor<Other>>](transformertotemporaladaptor/appending(_:)-20ar5.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, EstimatorToTemporalAdaptor<Other>>](transformertotemporaladaptor/appending(_:)-28l29.md)
  Composes this temporal transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, UpdatableSupervisedEstimatorToTemporalAdaptor<Other>>](transformertotemporaladaptor/appending(_:)-292cs.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, Other>](transformertotemporaladaptor/appending(_:)-3l3ye.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, SupervisedEstimatorToTemporalAdaptor<Other>>](transformertotemporaladaptor/appending(_:)-4kibv.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, Other>](transformertotemporaladaptor/appending(_:)-6eb5o.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, Other>](transformertotemporaladaptor/appending(_:)-8a1vg.md)
  Composes this temporal transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, Other>](transformertotemporaladaptor/appending(_:)-8buvq.md)
  Composes this temporal transformer with a temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, Other>](transformertotemporaladaptor/appending(_:)-8kcu9.md)
  Composes this temporal transformer with another temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, UpdatableEstimatorToTemporalAdaptor<Other>>](transformertotemporaladaptor/appending(_:)-972cl.md)
  Composes this temporal transformer with an updatable estimator.
- [func applied<S, TS, Annotation>(to: S, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<Self.OutputSequence, Annotation>]](transformertotemporaladaptor/applied(to:eventhandler:)-15lwb.md)
  Performs the transformation on a sequence of annotated input sequences.
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](transformertotemporaladaptor/applied(to:eventhandler:)-7l7td.md)
  Performs the transformation on a sequence of input sequences.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](transformertotemporaladaptor/callasfunction(_:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](transformertotemporaladaptor/callasfunction(to:eventhandler:).md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](transformertotemporaladaptor/export(to:).md)
  Exports this temporal transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](transformertotemporaladaptor/export(to:metadata:).md)
  Exports this temporal transformer as a CoreML model with user-supplied metadata.
- [func prediction<S, Label>(from: S) async throws -> Self.OutputSequence](transformertotemporaladaptor/prediction(from:).md)
  Performs a prediction on a single input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertotemporaladaptor/temporaltransformer-implementations)*