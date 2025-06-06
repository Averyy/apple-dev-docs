# UpdatableEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> UpdatableEstimatorToSupervisedAdaptor<Self, Annotation>](onehotencoder/adaptedassupervised(annotationtype:)-2keoa.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> UpdatableEstimatorToTemporalAdaptor<Self>](onehotencoder/adaptedastemporal-4ki99.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other>>
](onehotencoder/appending(_:)-3659i.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](onehotencoder/appending(_:)-46tol.md)
  Composes this updatable estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](onehotencoder/appending(_:)-47ta1.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](onehotencoder/appending(_:)-74r5v.md)
  Composes this updatable estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](onehotencoder/appending(_:)-8z8uj.md)
  Composes this updatable estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](onehotencoder/appending(_:)-90lxm.md)
  Composes this updatable estimator with another updatable estimator.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> OneHotEncoder<Category>.Transformer](onehotencoder/decodewithoptimizer(from:).md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(OneHotEncoder<Category>.Transformer, to: inout any EstimatorEncoder) throws](onehotencoder/encodewithoptimizer(_:to:).md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> OneHotEncoder<Category>.Transformer](onehotencoder/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](onehotencoder/update(_:with:).md)
- [func update(inout OneHotEncoder<Category>.Transformer, with: some Sequence<Optional<Category>>, eventHandler: EventHandler?) throws](onehotencoder/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/onehotencoder/updatableestimator-implementations)*