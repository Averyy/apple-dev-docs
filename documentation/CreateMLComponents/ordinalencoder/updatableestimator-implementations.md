# UpdatableEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> OrdinalEncoder<Category>.Transformer](ordinalencoder/decodewithoptimizer(from:).md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(OrdinalEncoder<Category>.Transformer, to: inout any EstimatorEncoder) throws](ordinalencoder/encodewithoptimizer(_:to:).md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> OrdinalEncoder<Category>.Transformer](ordinalencoder/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout OrdinalEncoder<Category>.Transformer, with: some Sequence<Optional<Category>>, eventHandler: EventHandler?) throws](ordinalencoder/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/ordinalencoder/updatableestimator-implementations)*