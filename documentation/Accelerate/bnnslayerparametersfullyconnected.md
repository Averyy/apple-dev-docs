# BNNSLayerParametersFullyConnected

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters of a fully connected layer.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
struct BNNSLayerParametersFullyConnected
```

```c
typedef struct { ... } BNNSLayerParametersFullyConnected;
```

## Topics

### Initializers
- [init(i_desc: BNNSNDArrayDescriptor, w_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor, activation: BNNSActivation)](./bnnslayerparametersfullyconnected/init%28i_desc,w_desc,o_desc,bias,activation%29.md)
  Returns a new fully connected layer parameters structure from the specified parameters.
- [init()](./bnnslayerparametersfullyconnected/init%28%29.md)
  Returns a new fully connected layer parameters structure.
### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](./bnnslayerparametersfullyconnected/i_desc.md)
  The descriptor of the input.
- [var w_desc: BNNSNDArrayDescriptor](./bnnslayerparametersfullyconnected/w_desc.md)
  The descriptor of the weights.
- [var o_desc: BNNSNDArrayDescriptor](./bnnslayerparametersfullyconnected/o_desc.md)
  The descriptor of the output.
- [var bias: BNNSNDArrayDescriptor](./bnnslayerparametersfullyconnected/bias.md)
  The descriptor of the bias.
- [var activation: BNNSActivation](./bnnslayerparametersfullyconnected/activation.md)
  The activation function that the layer applies to the output.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Fully connected layers
- [struct BNNSFullyConnectedLayerParameters](./bnnsfullyconnectedlayerparameters.md)
  A structure containing fully connected layer parameters.
- [func BNNSFilterCreateFullyConnectedLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSFullyConnectedLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatefullyconnectedlayer%28_,_,_,_%29.md)
  Returns a fully connected filter, initialized with input, output, layer, and filter parameters.
- [class FullyConnectedLayer](./bnns/fullyconnectedlayer.md)
  A layer object that wraps a fully connected filter and manages its deinitialization.
- [func BNNSFilterCreateLayerFullyConnected(UnsafePointer<BNNSLayerParametersFullyConnected>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerfullyconnected%28_,_%29.md)
  Returns a new fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersfullyconnected)*