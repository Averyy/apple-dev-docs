# BNNS.ActivationLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A layer object that wraps an activation filter and manages its deinitialization.

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
class ActivationLayer
```

## Topics

### Creating an Activation Layer
- [convenience init?(function: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?)](./activationlayer/init%28function,input,output,filterparameters%29.md)
  Returns a new activation layer.
### Specifying an Activation Function
- [BNNS.ActivationFunction](./activationfunction.md)
  Constants that describe activation functions.
### Directly Applying Activation
- [static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](./applyactivation%28activation,input,output,batchsize,filterparameters%29.md)
  Applies the specified activation function.
### Initializers
- [convenience init?(function: BNNS.ActivationFunction, axes: [Int], input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?)](./activationlayer/init%28function,axes,input,output,filterparameters%29.md)

## Relationships

### Inherits From
- [BNNS.UnaryLayer](./unarylayer.md)

## See Also

### Activation layers
- [func BNNSFilterCreateVectorActivationLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatevectoractivationlayer%28_,_,_,_%29.md)
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
- [static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](./applyactivation%28activation,input,output,batchsize,filterparameters%29.md)
  Applies the specified activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/activationlayer)*