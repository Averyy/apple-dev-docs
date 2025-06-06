# init(in_size:out_size:weights:bias:activation:)

**Framework**: Accelerate  
**Kind**: init

Returns a new fully connected layer parameters structure.

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
init(in_size: Int, out_size: Int, weights: BNNSLayerData, bias: BNNSLayerData, activation: BNNSActivation)
```

## Parameters

- `in_size`: The size of the input vector.
- `out_size`: The size of the output vector.
- `weights`: Matrix coefficients, containing       values.
- `bias`: Layer bias, containing   values, one for each output component.
- `activation`: The layer activation function.

## See Also

- [init()](bnnsfullyconnectedlayerparameters/init.md)
- [init(in_size: Int, out_size: Int, weights: BNNSLayerData)](bnnsfullyconnectedlayerparameters/init(in_size:out_size:weights:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfullyconnectedlayerparameters/init(in_size:out_size:weights:bias:activation:))*