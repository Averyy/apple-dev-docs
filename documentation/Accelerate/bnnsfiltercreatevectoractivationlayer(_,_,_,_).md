# BNNSFilterCreateVectorActivationLayer(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 11.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerActivation(_:_:))
- iPadOS 11.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerActivation(_:_:))
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerActivation(_:_:))
- macOS 10.13+ - Deprecated in 11.0 (renamed: BNNSFilterCreateLayerActivation(_:_:))
- tvOS 11.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerActivation(_:_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: BNNSFilterCreateLayerActivation(_:_:))
- watchOS 4.0+ - Deprecated in 7.0 (renamed: BNNSFilterCreateLayerActivation(_:_:))

> **Deprecated**: Use [`BNNSFilterCreateLayerActivation(_:_:)`](./bnnsfiltercreatelayeractivation%28_,_%29.md) instead.

## Declaration

```swift
func BNNSFilterCreateVectorActivationLayer(_ in_desc: UnsafePointer<BNNSVectorDescriptor>, _ out_desc: UnsafePointer<BNNSVectorDescriptor>, _ activation: UnsafePointer<BNNSActivation>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

```c
BNNSFilterBNNSFilterCreateVectorActivationLayer(const BNNSVectorDescriptor *in_desc, const BNNSVectorDescriptor *out_desc, const BNNSActivation *activation, const BNNSFilterParameters *filter_params);
```

## See Also

### Activation layers
- [class ActivationLayer](./bnns/activationlayer.md)
  A layer object that wraps an activation filter and manages its deinitialization.
- [struct BNNSActivationFunction](./bnnsactivationfunction.md)
  Constants that describe activation functions.
- [struct BNNSActivation](./bnnsactivation.md)
  A set of parameters that describe common activation functions.
- [struct BNNSLayerParametersActivation](./bnnslayerparametersactivation.md)
  A set of parameters that define an activation layer.
- [func BNNSFilterCreateLayerActivation(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayeractivation%28_,_%29.md)
  Returns a new activation layer.
- [func BNNSDirectApplyActivationBatch(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](./bnnsdirectapplyactivationbatch%28_,_,_,_,_%29.md)
  Applies an activation filter to a set of input objects, writing out the result to a set of output objects.
- [static func applyActivation(activation: BNNS.ActivationFunction, axes: [Int], input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](./bnns/applyactivation%28activation,axes,input,output,batchsize,filterparameters%29.md)
  Applies an activation function on the specified axes.
- [static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](./bnns/applyactivation%28activation,input,output,batchsize,filterparameters%29.md)
  Applies the specified activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatevectoractivationlayer(_:_:_:_:))*