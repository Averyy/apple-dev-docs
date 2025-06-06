# y_dilation_stride

**Framework**: Accelerate  
**Kind**: property

The height increment between elements in the input image during convolution.

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
var y_dilation_stride: Int
```

## See Also

- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparametersconvolution/i_desc.md)
  The descriptor of the input.
- [var w_desc: BNNSNDArrayDescriptor](bnnslayerparametersconvolution/w_desc.md)
  The descriptor of the weights.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersconvolution/o_desc.md)
  The descriptor of the output.
- [var bias: BNNSNDArrayDescriptor](bnnslayerparametersconvolution/bias.md)
  The bias descriptor.
- [var activation: BNNSActivation](bnnslayerparametersconvolution/activation.md)
  The activation function that the layer applies to the output.
- [var x_stride: Int](bnnslayerparametersconvolution/x_stride.md)
  The width increment of the input image.
- [var y_stride: Int](bnnslayerparametersconvolution/y_stride.md)
  The height increment of the input image.
- [var x_dilation_stride: Int](bnnslayerparametersconvolution/x_dilation_stride.md)
  The width increment between elements in the input image during convolution.
- [var x_padding: Int](bnnslayerparametersconvolution/x_padding.md)
  The width padding, which is the number of virtual zeros added to the left and right of each channel.
- [var y_padding: Int](bnnslayerparametersconvolution/y_padding.md)
  The height padding, which is the number of virtual zeros added to the top and bottom of each channel.
- [var groups: Int](bnnslayerparametersconvolution/groups.md)
  Convolution group size.
- [var pad: (Int, Int, Int, Int)](bnnslayerparametersconvolution/pad.md)
  Padding which is asymmetric and ignored if the width or height padding values are greater than zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersconvolution/y_dilation_stride)*