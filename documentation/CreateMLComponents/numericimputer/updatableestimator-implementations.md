# UpdatableEstimator Implementations

**Framework**: Create ML Components  
**Role**: API Collection

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> NumericImputer<Element>.Transformer](./decodewithoptimizer%28from%29.md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(NumericImputer<Element>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> NumericImputer<Element>.Transformer](./maketransformer%28%29.md)
  Creates a default-initialized impute transformer suitable for incremental fitting.
- [func update(inout ImputeTransformer<Element>, with: some Sequence<Optional<Element>>, eventHandler: EventHandler?) throws](./update%28_,with,eventhandler%29.md)
  Updates an impute transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/numericimputer/updatableestimator-implementations)*