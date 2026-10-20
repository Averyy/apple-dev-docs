# BNNSGraph.Builder

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure thats provides a closure you can use to define the arguments and operations of a BNNS Graph.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Builder
```

## Topics

### Protocols
- [BNNSGraph.Builder.OperationParameter](./builder/operationparameter.md)
  A protocol that allows functions to accept either tensors or collections.
- [BNNSGraph.Builder.SliceIndex](./builder/sliceindex.md)
  A protocol that the BNNS graph builder uses to specify slice indices.
### Structures
- [BNNSGraph.Builder.SliceRange](./builder/slicerange.md)
  A structure that represents a range.
- [BNNSGraph.Builder.Tensor](./builder/tensor.md)
  A structure that represents an abstract handle to a tensor that you use within a `BNNSGraph.makeContext` closure.
### Instance Methods
- [func argument<T>(name: String?, dataType: T.Type, shape: [Int], intent: BNNSGraph.Builder.Intent) -> BNNSGraph.Builder.Tensor<T>](./builder/argument%28name,datatype,shape,intent%29.md)
  Registers and returns an input or in-out tensor argument to the graph.
- [func concatenate<T>([BNNSGraph.Builder.Tensor<T>], axis: Int) -> BNNSGraph.Builder.Tensor<T>](./builder/concatenate%28_,axis%29.md)
  Adds a concatenation operation to the current graph.
- [func constant<T>(name: String?, value: T) -> BNNSGraph.Builder.Tensor<T>](./builder/constant%28name,value%29.md)
  Registers and returns a tensor that contains a constant scalar value.
- [func constant<T>(name: String?, values: some AccelerateBuffer, shape: [Int]?) -> BNNSGraph.Builder.Tensor<T>](./builder/constant%28name,values,shape%29.md)
  Registers and returns a tensor with the specified shape that contains constant data, such as weight or bias values.
- [func constant(values: Array<Array<Float>>, rowMajor: Bool) -> BNNSGraph.Builder.Tensor<Float>](./builder/constant%28values,rowmajor%29-6b7b8.md)
  Returns a rank 2 tensor from an array of arrays.
- [func constant(values: Array<Array<Float16>>, rowMajor: Bool) -> BNNSGraph.Builder.Tensor<Float16>](./builder/constant%28values,rowmajor%29-7b4v2.md)
### Type Aliases
- [BNNSGraph.Builder.PoolingPadding](./builder/poolingpadding.md)
  The padding that you use for pooling operations to specify zero-padding.
### Enumerations
- [BNNSGraph.Builder.Activation](./builder/activation.md)
  The activation function that a recurrent operation uses.
- [BNNSGraph.Builder.CeilingMode](./builder/ceilingmode.md)
  The pooling ceiling mode.
- [BNNSGraph.Builder.ConvolutionPadding](./builder/convolutionpadding.md)
  The padding that you use for convolution operations to specify zero-padding.
- [BNNSGraph.Builder.Direction](./builder/direction.md)
  The direction of a recurrent operation.
- [BNNSGraph.Builder.Intent](./builder/intent.md)
  Constants that describe argument intents.
- [BNNSGraph.Builder.Padding](./builder/padding.md)
  The padding that you use for pad operations.
- [BNNSGraph.Builder.PoolingFunction](./builder/poolingfunction.md)
  The pooling function
- [BNNSGraph.Builder.ScatterMode](./builder/scattermode.md)
  Constants that specify how scatter operations overwrite destination elements.
- [BNNSGraph.Builder.SortOrder](./builder/sortorder.md)
  The sort order for functions such as `argsort`.

## See Also

### Building graphs in Swift
- [static func makeContext(options: BNNSGraph.CompileOptions, (inout BNNSGraph.Builder) -> [any BNNSGraph.TensorDescriptor]) throws -> BNNSGraph.Context](./makecontext%28options,_%29.md)
  Returns a new context that wraps a graph object that the given closure defines.
- [BNNSGraph.Builder.Tensor](./builder/tensor.md)
  A structure that represents an abstract handle to a tensor that you use within a `BNNSGraph.makeContext` closure.
- [Supporting real-time ML inference on the CPU](../supporting-real-time-ml-inference-on-the-cpu.md)
  Add real-time digital signal processing to apps like Logic Pro X and GarageBand with the BNNS Graph API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder)*