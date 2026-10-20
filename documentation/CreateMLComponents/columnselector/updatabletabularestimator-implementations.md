# UpdatableTabularEstimator Implementations

**Framework**: Create ML Components  
**Role**: API Collection

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> ColumnSelector<Estimator, UnwrappedInput>.Transformer](./decodewithoptimizer%28from%29.md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(ColumnSelector<Estimator, UnwrappedInput>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> ColumnSelectorTransformer<Estimator.Transformer, UnwrappedInput>](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout ColumnSelector<Estimator, UnwrappedInput>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselector/updatabletabularestimator-implementations)*