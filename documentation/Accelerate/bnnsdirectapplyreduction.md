# BNNSDirectApplyReduction(_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a reduction operation directly to an input tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func BNNSDirectApplyReduction(_ layer_params: UnsafePointer<BNNSLayerParametersReduction>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: Filter runtime parameters.

## See Also

- [class ReductionLayer](bnns/reductionlayer.md)
  A layer object that wraps a reduction filter and manages its deinitialization.
- [static func applyReduction(BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/applyreduction(_:input:output:weights:filterparameters:).md)
  Applies the specified reduction function.
- [struct BNNSReduceFunction](bnnsreducefunction.md)
  Constants that describe reduction functions.
- [struct BNNSLayerParametersReduction](bnnslayerparametersreduction.md)
  A set of parameters that define a reduction layer.
- [func BNNSFilterCreateLayerReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerreduction(_:_:).md)
  Returns a new reduction layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdirectapplyreduction(_:_:))*