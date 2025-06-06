# UpdatableEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> UpdatableEstimatorToSupervisedAdaptor<Self, Annotation>](ordinalencoder/adaptedassupervised(annotationtype:)-6u8j4.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> UpdatableEstimatorToTemporalAdaptor<Self>](ordinalencoder/adaptedastemporal-rkfq.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other>>
](ordinalencoder/appending(_:)-3660g.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](ordinalencoder/appending(_:)-3i3p4.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](ordinalencoder/appending(_:)-3w2ag.md)
  Composes this updatable estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](ordinalencoder/appending(_:)-7vgok.md)
  Composes this updatable estimator with another updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](ordinalencoder/appending(_:)-99wxu.md)
  Composes this updatable estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](ordinalencoder/appending(_:)-9ly0x.md)
  Composes this updatable estimator with a temporal transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> OrdinalEncoder<Category>.Transformer](ordinalencoder/decodewithoptimizer(from:).md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(OrdinalEncoder<Category>.Transformer, to: inout any EstimatorEncoder) throws](ordinalencoder/encodewithoptimizer(_:to:).md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> OrdinalEncoder<Category>.Transformer](ordinalencoder/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](ordinalencoder/update(_:with:).md)
- [func update(inout OrdinalEncoder<Category>.Transformer, with: some Sequence<Optional<Category>>, eventHandler: EventHandler?) throws](ordinalencoder/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/ordinalencoder/updatableestimator-implementations)*