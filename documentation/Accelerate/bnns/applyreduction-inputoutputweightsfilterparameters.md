# applyReduction(_:input:output:weights:filterParameters:)

**Framework**: Accelerate  
**Kind**: method

Applies the specified reduction function.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func applyReduction(_ reductionFunction: BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters? = nil) throws
```

## Parameters

- `reductionFunction`: The variable that specifies the reduction function.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `weights`: The descriptor of the weights.
- `filterParameters`: The filter runtime parameters.

## See Also

- [class ReductionLayer](bnns/reductionlayer.md)
  A layer object that wraps a reduction filter and manages its deinitialization.
- [struct BNNSReduceFunction](bnnsreducefunction.md)
  Constants that describe reduction functions.
- [struct BNNSLayerParametersReduction](bnnslayerparametersreduction.md)
  A set of parameters that define a reduction layer.
- [func BNNSFilterCreateLayerReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerreduction(_:_:).md)
  Returns a new reduction layer.
- [func BNNSDirectApplyReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsdirectapplyreduction(_:_:).md)
  Applies a reduction operation directly to an input tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/applyreduction(_:input:output:weights:filterparameters:))*