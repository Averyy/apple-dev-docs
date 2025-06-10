# BNNSGraph.Builder

**Framework**: Accelerate  
**Kind**: struct

A structure thats provides a closure you can use to define the arguments and operations of a BNNS Graph.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct Builder
```

## Topics

### Protocols
- [BNNSGraph.Builder.OperationParameter](bnnsgraph/builder/operationparameter.md)
  A protocol that allows functions to accept either tensors or collections.
- [BNNSGraph.Builder.SliceIndex](bnnsgraph/builder/sliceindex.md)
  A protocol that the BNNS graph builder uses to specify slice indices.
### Structures
- [BNNSGraph.Builder.SliceRange](bnnsgraph/builder/slicerange.md)
  A structure that represents a range.
- [BNNSGraph.Builder.Tensor](bnnsgraph/builder/tensor.md)
  A structure that represents an abstract handle to a tensor that you use within a `BNNSGraph.makeContext` closure.
### Instance Methods
- [func argument<T>(name: String?, dataType: T.Type, shape: [Int], intent: BNNSGraph.Builder.Intent) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/argument(name:datatype:shape:intent:).md)
  Registers and returns an input or in-out tensor argument to the graph.
- [func concatenate<T>([BNNSGraph.Builder.Tensor<T>], axis: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/concatenate(_:axis:).md)
  Adds a concatenation operation to the current graph.
- [func constant<T>(name: String?, value: T) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/constant(name:value:).md)
  Registers and returns a tensor that contains a constant scalar value.
- [func constant<T>(name: String?, values: some AccelerateBuffer, shape: [Int]?) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/constant(name:values:shape:).md)
  Registers and returns a tensor with the specified shape that contains constant data, such as weight or bias values.
- [func constant(values: Array<Array<Float>>, rowMajor: Bool) -> BNNSGraph.Builder.Tensor<Float>](bnnsgraph/builder/constant(values:rowmajor:)-6b7b8.md)
  Returns a rank 2 tensor from an array of arrays.
- [func constant(values: Array<Array<Float16>>, rowMajor: Bool) -> BNNSGraph.Builder.Tensor<Float16>](bnnsgraph/builder/constant(values:rowmajor:)-7b4v2.md)
### Type Aliases
- [BNNSGraph.Builder.PoolingPadding](bnnsgraph/builder/poolingpadding.md)
  The padding that you use for pooling operations to specify zero-padding.
### Enumerations
- [BNNSGraph.Builder.Activation](bnnsgraph/builder/activation.md)
  The activation function that a recurrent operation uses.
- [BNNSGraph.Builder.CeilingMode](bnnsgraph/builder/ceilingmode.md)
  The pooling ceiling mode.
- [BNNSGraph.Builder.ConvolutionPadding](bnnsgraph/builder/convolutionpadding.md)
  The padding that you use for convolution operations to specify zero-padding.
- [BNNSGraph.Builder.Direction](bnnsgraph/builder/direction.md)
  The direction of a recurrent operation.
- [BNNSGraph.Builder.Intent](bnnsgraph/builder/intent.md)
  Constants that describe argument intents.
- [BNNSGraph.Builder.Padding](bnnsgraph/builder/padding.md)
  The padding that you use for pad operations.
- [BNNSGraph.Builder.PoolingFunction](bnnsgraph/builder/poolingfunction.md)
  The pooling function
- [BNNSGraph.Builder.ScatterMode](bnnsgraph/builder/scattermode.md)
  Constants that specify how scatter operations overwrite destination elements.
- [BNNSGraph.Builder.SortOrder](bnnsgraph/builder/sortorder.md)
  The sort order for functions such as `argsort`.

## See Also

- [static func makeContext(options: BNNSGraph.CompileOptions, (inout BNNSGraph.Builder) -> [any BNNSGraph.TensorDescriptor]) throws -> BNNSGraph.Context](bnnsgraph/makecontext(options:_:).md)
  Returns a new context that wraps a graph object that the given closure defines.
- [BNNSGraph.Builder.Tensor](bnnsgraph/builder/tensor.md)
  A structure that represents an abstract handle to a tensor that you use within a `BNNSGraph.makeContext` closure.
- [Supporting real-time ML inference on the CPU](supporting-real-time-ml-inference-on-the-cpu.md)
  Add real-time digital signal processing to apps like Logic Pro X and GarageBand with the BNNS Graph API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder)*