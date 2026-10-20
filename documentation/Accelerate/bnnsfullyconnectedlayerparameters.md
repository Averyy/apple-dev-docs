# BNNSFullyConnectedLayerParameters

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure containing fully connected layer parameters.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersFullyConnected)
- iPadOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersFullyConnected)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: BNNSLayerParametersFullyConnected)
- macOS 10.12+ - Deprecated in 11.0 (renamed: BNNSLayerParametersFullyConnected)
- tvOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersFullyConnected)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: BNNSLayerParametersFullyConnected)
- watchOS 3.0+ - Deprecated in 7.0 (renamed: BNNSLayerParametersFullyConnected)

> **Deprecated**: Use [`BNNSLayerParametersFullyConnected`](./bnnslayerparametersfullyconnected.md) instead.

## Declaration

```swift
struct BNNSFullyConnectedLayerParameters
```

```c
typedef struct { ... } BNNSFullyConnectedLayerParameters;
```

## Topics

### Initializers
- [init()](./bnnsfullyconnectedlayerparameters/init%28%29.md)
- [init(in_size: Int, out_size: Int, weights: BNNSLayerData, bias: BNNSLayerData, activation: BNNSActivation)](./bnnsfullyconnectedlayerparameters/init%28in_size,out_size,weights,bias,activation%29.md)
  Returns a new fully connected layer parameters structure.
- [init(in_size: Int, out_size: Int, weights: BNNSLayerData)](./bnnsfullyconnectedlayerparameters/init%28in_size,out_size,weights%29.md)
### Instance Properties
- [var activation: BNNSActivation](./bnnsfullyconnectedlayerparameters/activation.md)
  The layer activation function.
- [var bias: BNNSLayerData](./bnnsfullyconnectedlayerparameters/bias.md)
  Layer bias, one for each output component.
- [var in_size: Int](./bnnsfullyconnectedlayerparameters/in_size.md)
  The size of the input vector.
- [var out_size: Int](./bnnsfullyconnectedlayerparameters/out_size.md)
  The size of the output vector.
- [var weights: BNNSLayerData](./bnnsfullyconnectedlayerparameters/weights.md)
  Matrix coefficients.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Fully connected layers
- [func BNNSFilterCreateFullyConnectedLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSFullyConnectedLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatefullyconnectedlayer%28_,_,_,_%29.md)
  Returns a fully connected filter, initialized with input, output, layer, and filter parameters.
- [class FullyConnectedLayer](./bnns/fullyconnectedlayer.md)
  A layer object that wraps a fully connected filter and manages its deinitialization.
- [struct BNNSLayerParametersFullyConnected](./bnnslayerparametersfullyconnected.md)
  A structure that contains the parameters of a fully connected layer.
- [func BNNSFilterCreateLayerFullyConnected(UnsafePointer<BNNSLayerParametersFullyConnected>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerfullyconnected%28_,_%29.md)
  Returns a new fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfullyconnectedlayerparameters)*