# applyActivation(activation:input:output:batchSize:filterParameters:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Applies the specified activation function.

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
static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters? = nil) throws
```

## Parameters

- `activation`: The activation that the function applies.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `batchSize`: The number of input-output pairs.
- `filterParameters`: The filter runtime parameters.

## See Also

### Activation layers
- [func BNNSFilterCreateVectorActivationLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatevectoractivationlayer%28_,_,_,_%29.md)
- [class ActivationLayer](./activationlayer.md)
  A layer object that wraps an activation filter and manages its deinitialization.
- [struct BNNSActivationFunction](../bnnsactivationfunction.md)
  Constants that describe activation functions.
- [struct BNNSActivation](../bnnsactivation.md)
  A set of parameters that describe common activation functions.
- [struct BNNSLayerParametersActivation](../bnnslayerparametersactivation.md)
  A set of parameters that define an activation layer.
- [func BNNSFilterCreateLayerActivation(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatelayeractivation%28_,_%29.md)
  Returns a new activation layer.
- [func BNNSDirectApplyActivationBatch(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](../bnnsdirectapplyactivationbatch%28_,_,_,_,_%29.md)
  Applies an activation filter to a set of input objects, writing out the result to a set of output objects.
- [static func applyActivation(activation: BNNS.ActivationFunction, axes: [Int], input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](./applyactivation%28activation,axes,input,output,batchsize,filterparameters%29.md)
  Applies an activation function on the specified axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/applyactivation(activation:input:output:batchsize:filterparameters:))*