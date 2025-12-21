# UpdatableEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> NumericImputer<Element>.Transformer](numericimputer/decodewithoptimizer(from:).md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(NumericImputer<Element>.Transformer, to: inout any EstimatorEncoder) throws](numericimputer/encodewithoptimizer(_:to:).md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> NumericImputer<Element>.Transformer](numericimputer/maketransformer.md)
  Creates a default-initialized impute transformer suitable for incremental fitting.
- [func update(inout ImputeTransformer<Element>, with: some Sequence<Optional<Element>>, eventHandler: EventHandler?) throws](numericimputer/update(_:with:eventhandler:).md)
  Updates an impute transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/numericimputer/updatableestimator-implementations)*