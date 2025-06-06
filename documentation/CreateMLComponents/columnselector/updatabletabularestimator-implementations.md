# UpdatableTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> UpdatableTabularEstimatorToSupervisedAdaptor<Self, Annotation>](columnselector/adaptedassupervised(annotationcolumnid:)-4sir4.md)
  Exposes this updatable tabular estimator as a supervised tabular estimator.
- [func appending<Other>(Other) -> some UpdatableTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>>
](columnselector/appending(_:)-129t1.md)
  Composes this updatable tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](columnselector/appending(_:)-65u4v.md)
  Composes this updatable tabular estimator with an updatable supervised tabular estimator.
- [func appending<Other>(Other) -> some UpdatableTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>>
](columnselector/appending(_:)-99609.md)
  Composes this updatable tabular estimator with another updatable tabular estimator.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> ColumnSelector<Estimator, UnwrappedInput>.Transformer](columnselector/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(ColumnSelector<Estimator, UnwrappedInput>.Transformer, to: inout any EstimatorEncoder) throws](columnselector/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> ColumnSelectorTransformer<Estimator.Transformer, UnwrappedInput>](columnselector/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout Self.Transformer, with: DataFrame) async throws](columnselector/update(_:with:).md)
- [func update(inout ColumnSelector<Estimator, UnwrappedInput>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](columnselector/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselector/updatabletabularestimator-implementations)*