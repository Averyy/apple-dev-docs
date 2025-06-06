# TemporalTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](lineartimeseriesforecaster/model/adaptedasestimator-75kc1.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](lineartimeseriesforecaster/model/adaptedasupdatableestimator-75r88.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, Other>](lineartimeseriesforecaster/model/appending(_:)-1q42d.md)
  Composes this temporal transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, UpdatableEstimatorToTemporalAdaptor<Other>>](lineartimeseriesforecaster/model/appending(_:)-2lzk4.md)
  Composes this temporal transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, Other>](lineartimeseriesforecaster/model/appending(_:)-4en90.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TemporalAdaptor<Other>>](lineartimeseriesforecaster/model/appending(_:)-59p70.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, UpdatableSupervisedEstimatorToTemporalAdaptor<Other>>](lineartimeseriesforecaster/model/appending(_:)-6qdku.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TransformerToTemporalAdaptor<Other>>](lineartimeseriesforecaster/model/appending(_:)-8m7ok.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, Other>](lineartimeseriesforecaster/model/appending(_:)-92sik.md)
  Composes this temporal transformer with another temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, Other>](lineartimeseriesforecaster/model/appending(_:)-9qr5r.md)
  Composes this temporal transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, SupervisedEstimatorToTemporalAdaptor<Other>>](lineartimeseriesforecaster/model/appending(_:)-9w3yq.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, EstimatorToTemporalAdaptor<Other>>](lineartimeseriesforecaster/model/appending(_:)-pu73.md)
  Composes this temporal transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, Other>](lineartimeseriesforecaster/model/appending(_:)-s40i.md)
  Composes this transformer with a supervised temporal estimator.
- [func applied(to: some TemporalSequence<MLShapedArray<Scalar>>, eventHandler: EventHandler?) async throws -> AnyTemporalSequence<MLShapedArray<Scalar>>](lineartimeseriesforecaster/model/applied(to:eventhandler:)-3h2wx.md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](lineartimeseriesforecaster/model/callasfunction(_:eventhandler:)-4sfy3.md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](lineartimeseriesforecaster/model/callasfunction(to:eventhandler:).md)
  Performs the transformation on a sequence of inputs.
- [func prediction<S, Label>(from: S) async throws -> Self.OutputSequence](lineartimeseriesforecaster/model/prediction(from:)-sjeo.md)
  Performs a prediction on a single input.
### Type Aliases
- [LinearTimeSeriesForecaster.Model.OutputSequence](lineartimeseriesforecaster/model/outputsequence.md)
  The output async sequence type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model/temporaltransformer-implementations)*