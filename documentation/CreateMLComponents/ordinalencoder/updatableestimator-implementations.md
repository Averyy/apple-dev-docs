# UpdatableEstimator Implementations

**Framework**: Create ML Components  
**Role**: API Collection

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> OrdinalEncoder<Category>.Transformer](./decodewithoptimizer%28from%29.md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(OrdinalEncoder<Category>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> OrdinalEncoder<Category>.Transformer](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout OrdinalEncoder<Category>.Transformer, with: some Sequence<Optional<Category>>, eventHandler: EventHandler?) throws](./update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/ordinalencoder/updatableestimator-implementations)*