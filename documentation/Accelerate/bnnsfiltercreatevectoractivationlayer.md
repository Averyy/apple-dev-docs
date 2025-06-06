# BNNSFilterCreateVectorActivationLayer(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func BNNSFilterCreateVectorActivationLayer(_ in_desc: UnsafePointer<BNNSVectorDescriptor>, _ out_desc: UnsafePointer<BNNSVectorDescriptor>, _ activation: UnsafePointer<BNNSActivation>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

## See Also

- [class ActivationLayer](bnns/activationlayer.md)
  A layer object that wraps an activation filter and manages its deinitialization.
- [struct BNNSActivationFunction](bnnsactivationfunction.md)
  Constants that describe activation functions.
- [struct BNNSActivation](bnnsactivation.md)
  A set of parameters that describe common activation functions.
- [struct BNNSLayerParametersActivation](bnnslayerparametersactivation.md)
  A set of parameters that define an activation layer.
- [func BNNSFilterCreateLayerActivation(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayeractivation(_:_:).md)
  Returns a new activation layer.
- [func BNNSDirectApplyActivationBatch(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](bnnsdirectapplyactivationbatch(_:_:_:_:_:).md)
  Applies an activation filter to a set of input objects, writing out the result to a set of output objects.
- [static func applyActivation(activation: BNNS.ActivationFunction, axes: [Int], input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:axes:input:output:batchsize:filterparameters:).md)
  Applies an activation function on the specified axes.
- [static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:input:output:batchsize:filterparameters:).md)
  Applies the specified activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatevectoractivationlayer(_:_:_:_:))*