# UpdatableEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> OneHotEncoder<Category>.Transformer](onehotencoder/decodewithoptimizer(from:).md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(OneHotEncoder<Category>.Transformer, to: inout any EstimatorEncoder) throws](onehotencoder/encodewithoptimizer(_:to:).md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> OneHotEncoder<Category>.Transformer](onehotencoder/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout OneHotEncoder<Category>.Transformer, with: some Sequence<Optional<Category>>, eventHandler: EventHandler?) throws](onehotencoder/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/onehotencoder/updatableestimator-implementations)*