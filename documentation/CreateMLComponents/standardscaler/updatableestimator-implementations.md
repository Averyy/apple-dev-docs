# UpdatableEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> StandardScaler<Element>.Transformer](standardscaler/decodewithoptimizer(from:).md)
  Reads the encoded transformer with a decoder.
- [func encodeWithOptimizer(StandardScaler<Element>.Transformer, to: inout any EstimatorEncoder) throws](standardscaler/encodewithoptimizer(_:to:).md)
  Encodes the transformer to an encoder.
- [func makeTransformer() -> StandardScaler<Element>.Transformer](standardscaler/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout StandardScaler<Element>.Transformer, with: some Sequence<Element>, eventHandler: EventHandler?)](standardscaler/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/standardscaler/updatableestimator-implementations)*