# BNNSConvolutionLayerParameters

**Framework**: Accelerate  
**Kind**: struct

A structure containing convolution parameters.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct BNNSConvolutionLayerParameters
```

## Topics

### Initializers
- [init()](bnnsconvolutionlayerparameters/init.md)
- [init(x_stride: Int, y_stride: Int, x_padding: Int, y_padding: Int, k_width: Int, k_height: Int, in_channels: Int, out_channels: Int, weights: BNNSLayerData, bias: BNNSLayerData, activation: BNNSActivation)](bnnsconvolutionlayerparameters/init(x_stride:y_stride:x_padding:y_padding:k_width:k_height:in_channels:out_channels:weights:bias:activation:).md)
  Returns a new convolution parameters structure.
- [init(x_stride: Int, y_stride: Int, x_padding: Int, y_padding: Int, k_width: Int, k_height: Int, in_channels: Int, out_channels: Int, weights: BNNSLayerData)](bnnsconvolutionlayerparameters/init(x_stride:y_stride:x_padding:y_padding:k_width:k_height:in_channels:out_channels:weights:).md)
### Instance Properties
- [var activation: BNNSActivation](bnnsconvolutionlayerparameters/activation.md)
  The layer activation function.
- [var bias: BNNSLayerData](bnnsconvolutionlayerparameters/bias.md)
  Layer bias, one for each output channel.
- [var in_channels: Int](bnnsconvolutionlayerparameters/in_channels.md)
  The number of input channels.
- [var k_height: Int](bnnsconvolutionlayerparameters/k_height.md)
  The height of the convolution kernel.
- [var k_width: Int](bnnsconvolutionlayerparameters/k_width.md)
  The width of the convolution kernel.
- [var out_channels: Int](bnnsconvolutionlayerparameters/out_channels.md)
  The number of output channels.
- [var weights: BNNSLayerData](bnnsconvolutionlayerparameters/weights.md)
  Convolution weights.
- [var x_padding: Int](bnnsconvolutionlayerparameters/x_padding.md)
  The X padding.
- [var x_stride: Int](bnnsconvolutionlayerparameters/x_stride.md)
  The X increment in the input image.
- [var y_padding: Int](bnnsconvolutionlayerparameters/y_padding.md)
  The Y padding.
- [var y_stride: Int](bnnsconvolutionlayerparameters/y_stride.md)
  The Y increment in the input image.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func BNNSFilterCreateConvolutionLayer(UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSConvolutionLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreateconvolutionlayer(_:_:_:_:).md)
  Returns a convolution filter, initialized with input, output, layer, and filter parameters.
- [class ConvolutionLayer](bnns/convolutionlayer.md)
  A layer object that wraps a convolution filter and manages its deinitialization.
- [struct BNNSLayerParametersConvolution](bnnslayerparametersconvolution.md)
  A structure that contains the parameters of a convolution layer.
- [func BNNSFilterCreateLayerConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerconvolution(_:_:).md)
  Returns a new convolution layer.
- [func BNNSFilterCreateLayerTransposedConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayertransposedconvolution(_:_:).md)
  Returns a new transposed convolution layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsconvolutionlayerparameters)*