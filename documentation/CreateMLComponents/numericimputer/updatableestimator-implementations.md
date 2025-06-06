# UpdatableEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> UpdatableEstimatorToSupervisedAdaptor<Self, Annotation>](numericimputer/adaptedassupervised(annotationtype:)-emyb.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> UpdatableEstimatorToTemporalAdaptor<Self>](numericimputer/adaptedastemporal-6czxr.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](numericimputer/appending(_:)-3brnq.md)
  Composes this updatable estimator with another updatable estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other>>
](numericimputer/appending(_:)-4pfep.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](numericimputer/appending(_:)-68w9d.md)
  Composes this updatable estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](numericimputer/appending(_:)-6h7hv.md)
  Composes this updatable estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](numericimputer/appending(_:)-8pyyq.md)
  Composes this updatable estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](numericimputer/appending(_:)-ddcq.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> NumericImputer<Element>.Transformer](numericimputer/decodewithoptimizer(from:).md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(NumericImputer<Element>.Transformer, to: inout any EstimatorEncoder) throws](numericimputer/encodewithoptimizer(_:to:).md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> NumericImputer<Element>.Transformer](numericimputer/maketransformer.md)
  Creates a default-initialized impute transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](numericimputer/update(_:with:).md)
- [func update(inout ImputeTransformer<Element>, with: some Sequence<Optional<Element>>, eventHandler: EventHandler?) throws](numericimputer/update(_:with:eventhandler:).md)
  Updates an impute transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/numericimputer/updatableestimator-implementations)*