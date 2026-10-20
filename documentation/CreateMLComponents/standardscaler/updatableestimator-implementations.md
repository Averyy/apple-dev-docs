# UpdatableEstimator Implementations

**Framework**: Create ML Components  
**Role**: API Collection

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> StandardScaler<Element>.Transformer](./decodewithoptimizer%28from%29.md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(StandardScaler<Element>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> StandardScaler<Element>.Transformer](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout StandardScaler<Element>.Transformer, with: some Sequence<Element>, eventHandler: EventHandler?)](./update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/standardscaler/updatableestimator-implementations)*