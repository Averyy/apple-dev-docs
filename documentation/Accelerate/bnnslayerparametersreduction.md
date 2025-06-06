# BNNSLayerParametersReduction

**Framework**: Accelerate  
**Kind**: struct

A set of parameters that define a reduction layer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSLayerParametersReduction
```

## Topics

### Initializers
- [init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, w_desc: BNNSNDArrayDescriptor, reduce_func: BNNSReduceFunction, epsilon: Float)](bnnslayerparametersreduction/init(i_desc:o_desc:w_desc:reduce_func:epsilon:).md)
  Returns a structure containing the parameters of a reduction layer from the specified parameters.
- [init()](bnnslayerparametersreduction/init.md)
  Returns a structure containing the parameters of a reduction layer.
### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparametersreduction/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersreduction/o_desc.md)
  The descriptor of the output.
- [var w_desc: BNNSNDArrayDescriptor](bnnslayerparametersreduction/w_desc.md)
  The descriptor of the weights.
- [var reduce_func: BNNSReduceFunction](bnnslayerparametersreduction/reduce_func.md)
  The variable that specifies the reduction function.
- [var epsilon: Float](bnnslayerparametersreduction/epsilon.md)
  A value that the operation adds to each element when computing the sum of logarithms.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class ReductionLayer](bnns/reductionlayer.md)
  A layer object that wraps a reduction filter and manages its deinitialization.
- [static func applyReduction(BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/applyreduction(_:input:output:weights:filterparameters:).md)
  Applies the specified reduction function.
- [struct BNNSReduceFunction](bnnsreducefunction.md)
  Constants that describe reduction functions.
- [func BNNSFilterCreateLayerReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerreduction(_:_:).md)
  Returns a new reduction layer.
- [func BNNSDirectApplyReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsdirectapplyreduction(_:_:).md)
  Applies a reduction operation directly to an input tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersreduction)*