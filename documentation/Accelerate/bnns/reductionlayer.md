# BNNS.ReductionLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a reduction filter and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
class ReductionLayer
```

## Topics

### Creating a Reduction Layer
- [convenience init?(function: BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?)](bnns/reductionlayer/init(function:input:output:weights:filterparameters:).md)
  Returns a new reduction layer.
### Specifying a Reduction Function
- [BNNS.ReductionFunction](bnns/reductionfunction.md)
  Constants that describe reduction functions.
### Applying a Reduction Layer
- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor, generatingWeightsGradient: BNNSNDArrayDescriptor?) throws](bnns/reductionlayer/applybackward(batchsize:input:output:outputgradient:generatinginputgradient:generatingweightsgradient:).md)
  Applies the layer backward to generate input gradients.
### Directly Applying Reduction
- [static func applyReduction(BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/applyreduction(_:input:output:weights:filterparameters:).md)
  Applies the specified reduction function.

## Relationships

### Inherits From
- [BNNS.UnaryLayer](bnns/unarylayer.md)

## See Also

- [static func applyReduction(BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/applyreduction(_:input:output:weights:filterparameters:).md)
  Applies the specified reduction function.
- [struct BNNSReduceFunction](bnnsreducefunction.md)
  Constants that describe reduction functions.
- [struct BNNSLayerParametersReduction](bnnslayerparametersreduction.md)
  A set of parameters that define a reduction layer.
- [func BNNSFilterCreateLayerReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerreduction(_:_:).md)
  Returns a new reduction layer.
- [func BNNSDirectApplyReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsdirectapplyreduction(_:_:).md)
  Applies a reduction operation directly to an input tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/reductionlayer)*