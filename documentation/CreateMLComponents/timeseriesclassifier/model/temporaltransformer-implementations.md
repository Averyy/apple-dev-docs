# TemporalTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](timeseriesclassifier/model/adaptedasestimator-9s3tv.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](timeseriesclassifier/model/adaptedasupdatableestimator-3ngfq.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, UpdatableEstimatorToTemporalAdaptor<Other>>](timeseriesclassifier/model/appending(_:)-11d0n.md)
  Composes this temporal transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, Other>](timeseriesclassifier/model/appending(_:)-1ggjp.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, Other>](timeseriesclassifier/model/appending(_:)-1om8.md)
  Composes this temporal transformer with another temporal transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, SupervisedEstimatorToTemporalAdaptor<Other>>](timeseriesclassifier/model/appending(_:)-28nnp.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, Other>](timeseriesclassifier/model/appending(_:)-2kcn0.md)
  Composes this temporal transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TransformerToTemporalAdaptor<Other>>](timeseriesclassifier/model/appending(_:)-6t06l.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, Other>](timeseriesclassifier/model/appending(_:)-81047.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, Other>](timeseriesclassifier/model/appending(_:)-8xxp4.md)
  Composes this temporal transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, EstimatorToTemporalAdaptor<Other>>](timeseriesclassifier/model/appending(_:)-8yxon.md)
  Composes this temporal transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, UpdatableSupervisedEstimatorToTemporalAdaptor<Other>>](timeseriesclassifier/model/appending(_:)-9yije.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TemporalAdaptor<Other>>](timeseriesclassifier/model/appending(_:)-sm3l.md)
  Composes this temporal transformer with a transformer.
- [func applied(to: some TemporalSequence<MLShapedArray<Scalar>>, eventHandler: EventHandler?) async throws -> AnyTemporalSequence<ClassificationDistribution<Label>>](timeseriesclassifier/model/applied(to:eventhandler:)-3hpop.md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](timeseriesclassifier/model/callasfunction(_:eventhandler:)-8gh1b.md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](timeseriesclassifier/model/callasfunction(to:eventhandler:).md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](timeseriesclassifier/model/export(to:)-8hnf.md)
  Exports this temporal transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](timeseriesclassifier/model/export(to:metadata:)-2hktb.md)
  Exports this temporal transformer as a CoreML model with user-supplied metadata.
### Type Aliases
- [TimeSeriesClassifier.Model.OutputSequence](timeseriesclassifier/model/outputsequence.md)
  The output async sequence type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/model/temporaltransformer-implementations)*