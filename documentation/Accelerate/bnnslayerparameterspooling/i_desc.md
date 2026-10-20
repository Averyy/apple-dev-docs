# i_desc

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The descriptor of the input.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
var i_desc: BNNSNDArrayDescriptor
```

```c
BNNSNDArrayDescriptor i_desc;
```

## See Also

### Instance Properties
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.
- [var bias: BNNSNDArrayDescriptor](./bias.md)
  The descriptor of the bias.
- [var activation: BNNSActivation](./activation.md)
  The activation function that the layer applies to the output.
- [var pooling_function: BNNSPoolingFunction](./pooling_function.md)
  The variable that specifies the pooling function.
- [var k_width: Int](./k_width.md)
  The width of the kernel.
- [var k_height: Int](./k_height.md)
  The height of the kernel.
- [var x_stride: Int](./x_stride.md)
  The width increment of the input image.
- [var y_stride: Int](./y_stride.md)
  The height increment of the input image.
- [var x_dilation_stride: Int](./x_dilation_stride.md)
  The width increment between elements in the input image during convolution.
- [var y_dilation_stride: Int](./y_dilation_stride.md)
  The height increment between elements in the input image during convolution.
- [var x_padding: Int](./x_padding.md)
  The width padding, which is the number of virtual zeros added to the left and right of each channel.
- [var y_padding: Int](./y_padding.md)
  The height padding, which is the number of virtual zeros added to the top and bottom of each channel.
- [var pad: (Int, Int, Int, Int)](./pad.md)
  Asymmetric padding, ignored if `x_padding` or `y_padding` are greater than zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspooling/i_desc)*