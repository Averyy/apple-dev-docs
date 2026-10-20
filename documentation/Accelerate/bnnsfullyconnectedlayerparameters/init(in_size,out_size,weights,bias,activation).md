# init(in_size:out_size:weights:bias:activation:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new fully connected layer parameters structure.

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
init(in_size: Int, out_size: Int, weights: BNNSLayerData, bias: BNNSLayerData, activation: BNNSActivation)
```

## Parameters

- `in_size`: The size of the input vector.
- `out_size`: The size of the output vector.
- `weights`: Matrix coefficients, containing [`in_size`](./in_size.md) `*` [`out_size`](./out_size.md) values.
- `bias`: Layer bias, containing [`out_size`](./out_size.md) values, one for each output component.
- `activation`: The layer activation function.

## See Also

### Initializers
- [init()](./init%28%29.md)
- [init(in_size: Int, out_size: Int, weights: BNNSLayerData)](./init%28in_size,out_size,weights%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfullyconnectedlayerparameters/init(in_size:out_size:weights:bias:activation:))*