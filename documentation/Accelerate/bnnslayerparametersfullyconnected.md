# BNNSLayerParametersFullyConnected

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a fully connected layer.

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
struct BNNSLayerParametersFullyConnected
```

## Topics

### Initializers
- [init(i_desc: BNNSNDArrayDescriptor, w_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor, activation: BNNSActivation)](bnnslayerparametersfullyconnected/init(i_desc:w_desc:o_desc:bias:activation:).md)
  Returns a new fully connected layer parameters structure from the specified parameters.
- [init()](bnnslayerparametersfullyconnected/init.md)
  Returns a new fully connected layer parameters structure.
### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparametersfullyconnected/i_desc.md)
  The descriptor of the input.
- [var w_desc: BNNSNDArrayDescriptor](bnnslayerparametersfullyconnected/w_desc.md)
  The descriptor of the weights.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersfullyconnected/o_desc.md)
  The descriptor of the output.
- [var bias: BNNSNDArrayDescriptor](bnnslayerparametersfullyconnected/bias.md)
  The descriptor of the bias.
- [var activation: BNNSActivation](bnnslayerparametersfullyconnected/activation.md)
  The activation function that the layer applies to the output.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct BNNSFullyConnectedLayerParameters](bnnsfullyconnectedlayerparameters.md)
  A structure containing fully connected layer parameters.
- [func BNNSFilterCreateFullyConnectedLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSFullyConnectedLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatefullyconnectedlayer(_:_:_:_:).md)
  Returns a fully connected filter, initialized with input, output, layer, and filter parameters.
- [class FullyConnectedLayer](bnns/fullyconnectedlayer.md)
  A layer object that wraps a fully connected filter and manages its deinitialization.
- [func BNNSFilterCreateLayerFullyConnected(UnsafePointer<BNNSLayerParametersFullyConnected>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerfullyconnected(_:_:).md)
  Returns a new fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersfullyconnected)*