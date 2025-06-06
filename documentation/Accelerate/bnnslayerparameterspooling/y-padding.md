# y_padding

**Framework**: Accelerate  
**Kind**: property

The height padding, which is the number of virtual zeros added to the top and bottom of each channel.

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
var y_padding: Int
```

## See Also

- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparameterspooling/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparameterspooling/o_desc.md)
  The descriptor of the output.
- [var bias: BNNSNDArrayDescriptor](bnnslayerparameterspooling/bias.md)
  The descriptor of the bias.
- [var activation: BNNSActivation](bnnslayerparameterspooling/activation.md)
  The activation function that the layer applies to the output.
- [var pooling_function: BNNSPoolingFunction](bnnslayerparameterspooling/pooling_function.md)
  The variable that specifies the pooling function.
- [var k_width: Int](bnnslayerparameterspooling/k_width.md)
  The width of the kernel.
- [var k_height: Int](bnnslayerparameterspooling/k_height.md)
  The height of the kernel.
- [var x_stride: Int](bnnslayerparameterspooling/x_stride.md)
  The width increment of the input image.
- [var y_stride: Int](bnnslayerparameterspooling/y_stride.md)
  The height increment of the input image.
- [var x_dilation_stride: Int](bnnslayerparameterspooling/x_dilation_stride.md)
  The width increment between elements in the input image during convolution.
- [var y_dilation_stride: Int](bnnslayerparameterspooling/y_dilation_stride.md)
  The height increment between elements in the input image during convolution.
- [var x_padding: Int](bnnslayerparameterspooling/x_padding.md)
  The width padding, which is the number of virtual zeros added to the left and right of each channel.
- [var pad: (Int, Int, Int, Int)](bnnslayerparameterspooling/pad.md)
  Asymmetric padding, ignored if `x_padding` or `y_padding` are greater than zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspooling/y_padding)*