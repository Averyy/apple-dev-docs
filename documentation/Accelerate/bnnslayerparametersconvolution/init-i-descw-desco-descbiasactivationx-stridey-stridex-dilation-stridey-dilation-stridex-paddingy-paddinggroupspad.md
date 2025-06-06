# init(i_desc:w_desc:o_desc:bias:activation:x_stride:y_stride:x_dilation_stride:y_dilation_stride:x_padding:y_padding:groups:pad:)

**Framework**: Accelerate  
**Kind**: init

Returns a new convolution layer parameters structure from the specified parameters.

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
init(i_desc: BNNSNDArrayDescriptor, w_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor, activation: BNNSActivation, x_stride: Int, y_stride: Int, x_dilation_stride: Int, y_dilation_stride: Int, x_padding: Int, y_padding: Int, groups: Int, pad: (Int, Int, Int, Int))
```

#### Discussion

If `groups` is greater than 1, the layer uses input, output, weights, and bias for a set of convolutions, and you must meet the following:

- Input and output channels must be divisible by groups.
- The layout of the weights descriptor must be [`BNNSDataLayoutConvolutionWeightsOIHW`](bnnsdatalayoutconvolutionweightsoihw.md).
- The size of the second dimension of the weights must equal the number of input channels.
- The size of the third dimension of the weights must equal the number of output channels.
- When calling apply forward and backward functions, `in_stride`, `out_stride`, and gradient strides should be the strides for the entire convolution group.
- This functionality isn’t supported in transposed convolution.

> ❗ **Important**:  Convolution layers only support arrays with a data type of `float`, `float16`, `int8`, or `uint8`.

 Convolution layers only support arrays with a data type of `float`, `float16`, `int8`, or `uint8`.

## Parameters

- `i_desc`: The descriptor of the input. The data type of the input must be  .
- `w_desc`: The descriptor of the weights. The data type of the weights must be  ,  ,  , or  .
- `o_desc`: The descriptor of the output. The data type of the output must be  .
- `bias`: The descriptor of the bias.
- `activation`: The activation function that the layer applies to the output.
- `x_stride`: The width increment of the input image.
- `y_stride`: The height increment of the input image.
- `x_dilation_stride`: The width increment between elements in the input image during convolution.
- `y_dilation_stride`: The height increment between elements in the input image during convolution.
- `x_padding`: The width padding, which is the number of virtual zeros added to the top and bottom of each channel.
- `y_padding`: The height padding, which is the number of virtual zeros added to the top and bottom of each channel.
- `groups`: The number of convolution groups.
- `pad`: Padding which is asymmetric and ignored if the width or height padding values are greater than zero.

## See Also

- [init()](bnnslayerparametersconvolution/init.md)
  Returns a new convolution layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersconvolution/init(i_desc:w_desc:o_desc:bias:activation:x_stride:y_stride:x_dilation_stride:y_dilation_stride:x_padding:y_padding:groups:pad:))*