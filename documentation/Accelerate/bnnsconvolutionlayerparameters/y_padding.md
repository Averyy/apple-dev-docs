# y_padding

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The Y padding.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersConvolution)
- iPadOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersConvolution)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: BNNSLayerParametersConvolution)
- macOS 10.12+ - Deprecated in 11.0 (renamed: BNNSLayerParametersConvolution)
- tvOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersConvolution)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: BNNSLayerParametersConvolution)
- watchOS 3.0+ - Deprecated in 7.0 (renamed: BNNSLayerParametersConvolution)

## Declaration

```swift
var y_padding: Int
```

```c
size_t y_padding;
```

#### Discussion

Virtual 0 values added to the left and right of each channel of the input stack.

## See Also

### Instance Properties
- [var activation: BNNSActivation](./activation.md)
  The layer activation function.
- [var bias: BNNSLayerData](./bias.md)
  Layer bias, one for each output channel.
- [var in_channels: Int](./in_channels.md)
  The number of input channels.
- [var k_height: Int](./k_height.md)
  The height of the convolution kernel.
- [var k_width: Int](./k_width.md)
  The width of the convolution kernel.
- [var out_channels: Int](./out_channels.md)
  The number of output channels.
- [var weights: BNNSLayerData](./weights.md)
  Convolution weights.
- [var x_padding: Int](./x_padding.md)
  The X padding.
- [var x_stride: Int](./x_stride.md)
  The X increment in the input image.
- [var y_stride: Int](./y_stride.md)
  The Y increment in the input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsconvolutionlayerparameters/y_padding)*