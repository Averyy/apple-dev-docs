# init(i_desc:o_desc:bias:activation:pooling_function:k_width:k_height:x_stride:y_stride:x_dilation_stride:y_dilation_stride:x_padding:y_padding:pad:)

**Framework**: Accelerate  
**Kind**: init

Returns a new pooling layer parameters structure from the specified parameters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor, activation: BNNSActivation, pooling_function: BNNSPoolingFunction, k_width: Int, k_height: Int, x_stride: Int, y_stride: Int, x_dilation_stride: Int, y_dilation_stride: Int, x_padding: Int, y_padding: Int, pad: (Int, Int, Int, Int))
```

#### Discussion

> ❗ **Important**:  The number of input channels must be equal to number of output channels. The pooling layer supports `float16` and `float`, and the input data type must be equal to the output data type. The pooling layer only supports dilation stride for max and unmax pooling functions and in that case, data type must be `float`.

## Parameters

- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `bias`: The descriptor of the bias.
- `activation`: The activation function that the layer applies to the output.
- `pooling_function`: The variable that specifies the pooling function.
- `k_width`: The width of the kernel.
- `k_height`: The height of the kernel.
- `x_stride`: The width increment of the input image.
- `y_stride`: The height increment of the input image.
- `x_dilation_stride`: The width increment between elements in the input image during convolution.
- `y_dilation_stride`: The height increment between elements in the input image during convolution.
- `x_padding`: The width padding, which is the number of virtual zeros added to the left and right of each channel.
- `y_padding`: The height padding, which is the number of virtual zeros added to the top and bottom of each channel.
- `pad`: The height padding, which is the number of virtual zeros added to the top and bottom of each channel.

## See Also

- [init()](bnnslayerparameterspooling/init.md)
  Returns a new pooling layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspooling/init(i_desc:o_desc:bias:activation:pooling_function:k_width:k_height:x_stride:y_stride:x_dilation_stride:y_dilation_stride:x_padding:y_padding:pad:))*