# init(x_stride:y_stride:x_padding:y_padding:k_width:k_height:in_channels:out_channels:weights:bias:activation:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new convolution parameters structure.

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
init(x_stride: Int, y_stride: Int, x_padding: Int, y_padding: Int, k_width: Int, k_height: Int, in_channels: Int, out_channels: Int, weights: BNNSLayerData, bias: BNNSLayerData, activation: BNNSActivation)
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
- `weights`: Convolution weights.
- `bias`: Layer bias, one for each output channel.
- `activation`: The layer activation function

## See Also

### Initializers
- [init()](./init%28%29.md)
- [init(x_stride: Int, y_stride: Int, x_padding: Int, y_padding: Int, k_width: Int, k_height: Int, in_channels: Int, out_channels: Int, weights: BNNSLayerData)](./init%28x_stride,y_stride,x_padding,y_padding,k_width,k_height,in_channels,out_channels,weights%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsconvolutionlayerparameters/init(x_stride:y_stride:x_padding:y_padding:k_width:k_height:in_channels:out_channels:weights:bias:activation:))*