# weights

**Framework**: Accelerate  
**Kind**: property

Convolution weights.

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
var weights: BNNSLayerData
```

#### Discussion

This parameter should contain [`k_width`](bnnsconvolutionlayerparameters/k_width.md) `*` [`k_height`](bnnsconvolutionlayerparameters/k_height.md) `*` [`in_channels`](bnnsconvolutionlayerparameters/in_channels.md) `*` [`out_channels`](bnnsconvolutionlayerparameters/out_channels.md) values.

## See Also

- [var activation: BNNSActivation](bnnsconvolutionlayerparameters/activation.md)
  The layer activation function.
- [var bias: BNNSLayerData](bnnsconvolutionlayerparameters/bias.md)
  Layer bias, one for each output channel.
- [var in_channels: Int](bnnsconvolutionlayerparameters/in_channels.md)
  The number of input channels.
- [var k_height: Int](bnnsconvolutionlayerparameters/k_height.md)
  The height of the convolution kernel.
- [var k_width: Int](bnnsconvolutionlayerparameters/k_width.md)
  The width of the convolution kernel.
- [var out_channels: Int](bnnsconvolutionlayerparameters/out_channels.md)
  The number of output channels.
- [var x_padding: Int](bnnsconvolutionlayerparameters/x_padding.md)
  The X padding.
- [var x_stride: Int](bnnsconvolutionlayerparameters/x_stride.md)
  The X increment in the input image.
- [var y_padding: Int](bnnsconvolutionlayerparameters/y_padding.md)
  The Y padding.
- [var y_stride: Int](bnnsconvolutionlayerparameters/y_stride.md)
  The Y increment in the input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsconvolutionlayerparameters/weights)*