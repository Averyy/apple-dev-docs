# applyActivation(activation:axes:input:output:batchSize:filterParameters:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Applies an activation function on the specified axes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
static func applyActivation(activation: BNNS.ActivationFunction, axes: [Int], input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters? = nil) throws
```

## Parameters

- `activation`: The activation that the function applies.
- `axes`: The indices of the axes on which the function applies certain activation functions, such as [`softmax`](../bnnsactivationfunction/softmax.md).
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
- [static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](./applyactivation%28activation,input,output,batchsize,filterparameters%29.md)
  Applies the specified activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/applyactivation(activation:axes:input:output:batchsize:filterparameters:))*