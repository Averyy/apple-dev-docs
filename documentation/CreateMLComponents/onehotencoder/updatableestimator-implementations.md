# UpdatableEstimator Implementations

**Framework**: Create ML Components  
**Role**: API Collection

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> OneHotEncoder<Category>.Transformer](./decodewithoptimizer%28from%29.md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(OneHotEncoder<Category>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> OneHotEncoder<Category>.Transformer](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout OneHotEncoder<Category>.Transformer, with: some Sequence<Optional<Category>>, eventHandler: EventHandler?) throws](./update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/onehotencoder/updatableestimator-implementations)*