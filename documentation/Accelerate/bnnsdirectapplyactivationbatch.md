# BNNSDirectApplyActivationBatch(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies an activation filter to a set of input objects, writing out the result to a set of output objects.

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
func BNNSDirectApplyActivationBatch(_ layer_params: UnsafePointer<BNNSLayerParametersActivation>, _ filter_params: UnsafePointer<BNNSFilterParameters>?, _ batch_size: Int, _ in_stride: Int, _ out_stride: Int) -> Int32
```

#### Discussion

Calling this function is equal to calling [`BNNSFilterCreateLayerActivation(_:_:)`](bnnsfiltercreatelayeractivation(_:_:).md), [`BNNSFilterApplyBatch(_:_:_:_:_:_:)`](bnnsfilterapplybatch(_:_:_:_:_:_:).md), and [`BNNSFilterDestroy(_:)`](bnnsfilterdestroy(_:).md).

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: Filter runtime parameters.
- `batch_size`: The number of input-output pairs.
- `in_stride`: The increment, in values, between inputs.
- `out_stride`: The increment, in values, between outputs.

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
- [func BNNSFilterCreateLayerActivation(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayeractivation(_:_:).md)
  Returns a new activation layer.
- [static func applyActivation(activation: BNNS.ActivationFunction, axes: [Int], input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:axes:input:output:batchsize:filterparameters:).md)
  Applies an activation function on the specified axes.
- [static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:input:output:batchsize:filterparameters:).md)
  Applies the specified activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdirectapplyactivationbatch(_:_:_:_:_:))*