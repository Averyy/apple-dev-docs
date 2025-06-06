# BNNSFilterCreateLayerActivation(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new activation layer.

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
func BNNSFilterCreateLayerActivation(_ layer_params: UnsafePointer<BNNSLayerParametersActivation>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: The filter runtime parameters.

## See Also

- [func BNNSFilterCreateVectorActivationLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatevectoractivationlayer(_:_:_:_:).md)
- [class ActivationLayer](bnns/activationlayer.md)
  A layer object that wraps an activation filter and manages its deinitialization.
- [struct BNNSActivationFunction](bnnsactivationfunction.md)
  Constants that describe activation functions.
- [struct BNNSActivation](bnnsactivation.md)
  A set of parameters that describe common activation functions.
- [struct BNNSLayerParametersActivation](bnnslayerparametersactivation.md)
  A set of parameters that define an activation layer.
- [func BNNSDirectApplyActivationBatch(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](bnnsdirectapplyactivationbatch(_:_:_:_:_:).md)
  Applies an activation filter to a set of input objects, writing out the result to a set of output objects.
- [static func applyActivation(activation: BNNS.ActivationFunction, axes: [Int], input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:axes:input:output:batchsize:filterparameters:).md)
  Applies an activation function on the specified axes.
- [static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:input:output:batchsize:filterparameters:).md)
  Applies the specified activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatelayeractivation(_:_:))*