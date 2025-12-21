# UpdatableTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> ColumnSelector<Estimator, UnwrappedInput>.Transformer](columnselector/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(ColumnSelector<Estimator, UnwrappedInput>.Transformer, to: inout any EstimatorEncoder) throws](columnselector/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> ColumnSelectorTransformer<Estimator.Transformer, UnwrappedInput>](columnselector/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout ColumnSelector<Estimator, UnwrappedInput>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](columnselector/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselector/updatabletabularestimator-implementations)*