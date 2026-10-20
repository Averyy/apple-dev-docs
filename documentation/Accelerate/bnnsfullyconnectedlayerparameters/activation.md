# activation

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The layer activation function.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersFullyConnected)
- iPadOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersFullyConnected)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: BNNSLayerParametersFullyConnected)
- macOS 10.12+ - Deprecated in 11.0 (renamed: BNNSLayerParametersFullyConnected)
- tvOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersFullyConnected)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: BNNSLayerParametersFullyConnected)
- watchOS 3.0+ - Deprecated in 7.0 (renamed: BNNSLayerParametersFullyConnected)

## Declaration

```swift
var activation: BNNSActivation
```

```c
BNNSActivation activation;
```

## See Also

### Instance Properties
- [var bias: BNNSLayerData](./bias.md)
  Layer bias, one for each output component.
- [var in_size: Int](./in_size.md)
  The size of the input vector.
- [var out_size: Int](./out_size.md)
  The size of the output vector.
- [var weights: BNNSLayerData](./weights.md)
  Matrix coefficients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfullyconnectedlayerparameters/activation)*