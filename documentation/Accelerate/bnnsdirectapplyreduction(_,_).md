# BNNSDirectApplyReduction(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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

```c
int BNNSDirectApplyReduction(const BNNSLayerParametersReduction *layer_params, const BNNSFilterParameters *filter_params);
```

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: Filter runtime parameters.

## See Also

### Reduction layers
- [class ReductionLayer](./bnns/reductionlayer.md)
  A layer object that wraps a reduction filter and manages its deinitialization.
- [static func applyReduction(BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](./bnns/applyreduction%28_,input,output,weights,filterparameters%29.md)
  Applies the specified reduction function.
- [struct BNNSReduceFunction](./bnnsreducefunction.md)
  Constants that describe reduction functions.
- [struct BNNSLayerParametersReduction](./bnnslayerparametersreduction.md)
  A set of parameters that define a reduction layer.
- [func BNNSFilterCreateLayerReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerreduction%28_,_%29.md)
  Returns a new reduction layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdirectapplyreduction(_:_:))*