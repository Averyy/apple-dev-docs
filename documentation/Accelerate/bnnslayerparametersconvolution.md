# BNNSLayerParametersConvolution

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a convolution layer.

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
struct BNNSLayerParametersConvolution
```

## Topics

### Initializers
- [init(i_desc: BNNSNDArrayDescriptor, w_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor, activation: BNNSActivation, x_stride: Int, y_stride: Int, x_dilation_stride: Int, y_dilation_stride: Int, x_padding: Int, y_padding: Int, groups: Int, pad: (Int, Int, Int, Int))](bnnslayerparametersconvolution/init(i_desc:w_desc:o_desc:bias:activation:x_stride:y_stride:x_dilation_stride:y_dilation_stride:x_padding:y_padding:groups:pad:).md)
  Returns a new convolution layer parameters structure from the specified parameters.
- [init()](bnnslayerparametersconvolution/init.md)
  Returns a new convolution layer parameters structure.
### Instance Properties
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
- [var y_dilation_stride: Int](bnnslayerparametersconvolution/y_dilation_stride.md)
  The height increment between elements in the input image during convolution.
- [var x_padding: Int](bnnslayerparametersconvolution/x_padding.md)
  The width padding, which is the number of virtual zeros added to the left and right of each channel.
- [var y_padding: Int](bnnslayerparametersconvolution/y_padding.md)
  The height padding, which is the number of virtual zeros added to the top and bottom of each channel.
- [var groups: Int](bnnslayerparametersconvolution/groups.md)
  Convolution group size.
- [var pad: (Int, Int, Int, Int)](bnnslayerparametersconvolution/pad.md)
  Padding which is asymmetric and ignored if the width or height padding values are greater than zero.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct BNNSConvolutionLayerParameters](bnnsconvolutionlayerparameters.md)
  A structure containing convolution parameters.
- [func BNNSFilterCreateConvolutionLayer(UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSConvolutionLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreateconvolutionlayer(_:_:_:_:).md)
  Returns a convolution filter, initialized with input, output, layer, and filter parameters.
- [class ConvolutionLayer](bnns/convolutionlayer.md)
  A layer object that wraps a convolution filter and manages its deinitialization.
- [func BNNSFilterCreateLayerConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerconvolution(_:_:).md)
  Returns a new convolution layer.
- [func BNNSFilterCreateLayerTransposedConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayertransposedconvolution(_:_:).md)
  Returns a new transposed convolution layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersconvolution)*