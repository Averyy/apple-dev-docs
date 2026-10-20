# pooling_function

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The pooling function to apply to each sample.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersPooling)
- iPadOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersPooling)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: BNNSLayerParametersPooling)
- macOS 10.12+ - Deprecated in 11.0 (renamed: BNNSLayerParametersPooling)
- tvOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersPooling)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: BNNSLayerParametersPooling)
- watchOS 3.0+ - Deprecated in 7.0 (renamed: BNNSLayerParametersPooling)

## Declaration

```swift
var pooling_function: BNNSPoolingFunction
```

```c
BNNSPoolingFunction pooling_function;
```

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
- [var x_padding: Int](./x_padding.md)
  The X padding.
- [var x_stride: Int](./x_stride.md)
  The X increment in the input image.
- [var y_padding: Int](./y_padding.md)
  The Y padding.
- [var y_stride: Int](./y_stride.md)
  The Y increment in the input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnspoolinglayerparameters/pooling_function)*