# BNNSFullyConnectedLayerParameters

**Framework**: Accelerate  
**Kind**: struct

A structure containing fully connected layer parameters.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct BNNSFullyConnectedLayerParameters
```

## Topics

### Initializers
- [init()](bnnsfullyconnectedlayerparameters/init.md)
- [init(in_size: Int, out_size: Int, weights: BNNSLayerData, bias: BNNSLayerData, activation: BNNSActivation)](bnnsfullyconnectedlayerparameters/init(in_size:out_size:weights:bias:activation:).md)
  Returns a new fully connected layer parameters structure.
- [init(in_size: Int, out_size: Int, weights: BNNSLayerData)](bnnsfullyconnectedlayerparameters/init(in_size:out_size:weights:).md)
### Instance Properties
- [var activation: BNNSActivation](bnnsfullyconnectedlayerparameters/activation.md)
  The layer activation function.
- [var bias: BNNSLayerData](bnnsfullyconnectedlayerparameters/bias.md)
  Layer bias, one for each output component.
- [var in_size: Int](bnnsfullyconnectedlayerparameters/in_size.md)
  The size of the input vector.
- [var out_size: Int](bnnsfullyconnectedlayerparameters/out_size.md)
  The size of the output vector.
- [var weights: BNNSLayerData](bnnsfullyconnectedlayerparameters/weights.md)
  Matrix coefficients.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func BNNSFilterCreateFullyConnectedLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSFullyConnectedLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatefullyconnectedlayer(_:_:_:_:).md)
  Returns a fully connected filter, initialized with input, output, layer, and filter parameters.
- [class FullyConnectedLayer](bnns/fullyconnectedlayer.md)
  A layer object that wraps a fully connected filter and manages its deinitialization.
- [struct BNNSLayerParametersFullyConnected](bnnslayerparametersfullyconnected.md)
  A structure that contains the parameters of a fully connected layer.
- [func BNNSFilterCreateLayerFullyConnected(UnsafePointer<BNNSLayerParametersFullyConnected>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerfullyconnected(_:_:).md)
  Returns a new fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfullyconnectedlayerparameters)*