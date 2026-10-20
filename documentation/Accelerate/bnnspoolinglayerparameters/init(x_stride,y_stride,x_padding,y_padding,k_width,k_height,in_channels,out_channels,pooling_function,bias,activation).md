# init(x_stride:y_stride:x_padding:y_padding:k_width:k_height:in_channels:out_channels:pooling_function:bias:activation:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new pooling layer parameters structure

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
init(x_stride: Int, y_stride: Int, x_padding: Int, y_padding: Int, k_width: Int, k_height: Int, in_channels: Int, out_channels: Int, pooling_function: BNNSPoolingFunction, bias: BNNSLayerData, activation: BNNSActivation)
```

## Parameters

- `x_stride`: The X increment in the input image.
- `y_stride`: The Y increment in the input image.
- `x_padding`: The X padding.
- `y_padding`: The Y padding.
- `k_width`: The width of the convolution kernel.
- `k_height`: The height of the convolution kernel.
- `in_channels`: The number of input channels.
- `out_channels`: The number of output channels.
- `pooling_function`: The pooling function to apply to each sample
- `bias`: Layer bias, one for each output channel.
- `activation`: The layer activation function

## See Also

### Initializers
- [init()](./init%28%29.md)
- [init(x_stride: Int, y_stride: Int, x_padding: Int, y_padding: Int, k_width: Int, k_height: Int, in_channels: Int, out_channels: Int, pooling_function: BNNSPoolingFunction)](./init%28x_stride,y_stride,x_padding,y_padding,k_width,k_height,in_channels,out_channels,pooling_function%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnspoolinglayerparameters/init(x_stride:y_stride:x_padding:y_padding:k_width:k_height:in_channels:out_channels:pooling_function:bias:activation:))*