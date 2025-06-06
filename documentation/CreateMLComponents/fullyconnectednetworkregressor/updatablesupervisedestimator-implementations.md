# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsTemporal() -> UpdatableSupervisedEstimatorToTemporalAdaptor<Self>](fullyconnectednetworkregressor/adaptedastemporal.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-3iwy6.md)
  Composes this updatable supervised estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-4jxv0.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-4vmz5.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-553f5.md)
  Composes this updatable supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-7u42x.md)
  Composes this updatable estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-8f5sd.md)
  Composes this updatable supervised estimator with an updatable supervised temporal estimator.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkRegressor<Scalar>.Transformer](fullyconnectednetworkregressor/decodewithoptimizer(from:).md)
  Decodes a previously fitted transformer with an optimizer.
- [func encodeWithOptimizer(FullyConnectedNetworkRegressor<Scalar>.Transformer, to: inout any EstimatorEncoder) throws](fullyconnectednetworkregressor/encodewithoptimizer(_:to:).md)
  Encodes a fitted transformer with an optimizer.
- [func makeTransformer() -> FullyConnectedNetworkRegressorModel<Scalar>](fullyconnectednetworkregressor/maketransformer.md)
  Creates a default-initialized fully connected network regressor model suitable for incremental fitting.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](fullyconnectednetworkregressor/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](fullyconnectednetworkregressor/update(_:with:).md)
- [func update<InputSequence>(inout FullyConnectedNetworkRegressorModel<Scalar>, with: InputSequence, eventHandler: EventHandler?) async throws](fullyconnectednetworkregressor/update(_:with:eventhandler:).md)
  Updates a fully connected network regressor model with a new sequence of examples.
- [func update<Input>(inout Self.Transformer, with: Input, eventHandler: EventHandler?) async throws](fullyconnectednetworkregressor/update(_:with:eventhandler:)-3rebk.md)
  Updates a transformer on an async sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](fullyconnectednetworkregressor/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressor/updatablesupervisedestimator-implementations)*