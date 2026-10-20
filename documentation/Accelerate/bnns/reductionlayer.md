# BNNS.ReductionLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A layer object that wraps a reduction filter and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
class ReductionLayer
```

## Topics

### Creating a Reduction Layer
- [convenience init?(function: BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?)](./reductionlayer/init%28function,input,output,weights,filterparameters%29.md)
  Returns a new reduction layer.
### Specifying a Reduction Function
- [BNNS.ReductionFunction](./reductionfunction.md)
  Constants that describe reduction functions.
### Applying a Reduction Layer
- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor, generatingWeightsGradient: BNNSNDArrayDescriptor?) throws](./reductionlayer/applybackward%28batchsize,input,output,outputgradient,generatinginputgradient,generatingweightsgradient%29.md)
  Applies the layer backward to generate input gradients.
### Directly Applying Reduction
- [static func applyReduction(BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](./applyreduction%28_,input,output,weights,filterparameters%29.md)
  Applies the specified reduction function.

## Relationships

### Inherits From
- [BNNS.UnaryLayer](./unarylayer.md)

## See Also

### Reduction layers
- [static func applyReduction(BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](./applyreduction%28_,input,output,weights,filterparameters%29.md)
  Applies the specified reduction function.
- [struct BNNSReduceFunction](../bnnsreducefunction.md)
  Constants that describe reduction functions.
- [struct BNNSLayerParametersReduction](../bnnslayerparametersreduction.md)
  A set of parameters that define a reduction layer.
- [func BNNSFilterCreateLayerReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatelayerreduction%28_,_%29.md)
  Returns a new reduction layer.
- [func BNNSDirectApplyReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnsdirectapplyreduction%28_,_%29.md)
  Applies a reduction operation directly to an input tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/reductionlayer)*