# BNNSLayerParametersPooling

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a pooling layer.

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
struct BNNSLayerParametersPooling
```

## Topics

### Initializers
- [init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor, activation: BNNSActivation, pooling_function: BNNSPoolingFunction, k_width: Int, k_height: Int, x_stride: Int, y_stride: Int, x_dilation_stride: Int, y_dilation_stride: Int, x_padding: Int, y_padding: Int, pad: (Int, Int, Int, Int))](bnnslayerparameterspooling/init(i_desc:o_desc:bias:activation:pooling_function:k_width:k_height:x_stride:y_stride:x_dilation_stride:y_dilation_stride:x_padding:y_padding:pad:).md)
  Returns a new pooling layer parameters structure from the specified parameters.
- [init()](bnnslayerparameterspooling/init.md)
  Returns a new pooling layer parameters structure.
### Instance Properties
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
- [var y_padding: Int](bnnslayerparameterspooling/y_padding.md)
  The height padding, which is the number of virtual zeros added to the top and bottom of each channel.
- [var pad: (Int, Int, Int, Int)](bnnslayerparameterspooling/pad.md)
  Asymmetric padding, ignored if `x_padding` or `y_padding` are greater than zero.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct BNNSPoolingLayerParameters](bnnspoolinglayerparameters.md)
  A structure containing pooling layer parameters.
- [func BNNSFilterCreatePoolingLayer(UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSPoolingLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatepoolinglayer(_:_:_:_:).md)
  Returns a pooling  filter, initialized with input, output, layer, and filter parameters.
- [class PoolingLayer](bnns/poolinglayer.md)
  A layer object that wraps a pooling filter and manages its deinitialization.
- [struct BNNSPoolingFunction](bnnspoolingfunction.md)
  Constants that describe pooling functions.
- [var BNNSPoolingFunctionAverage: BNNSPoolingFunction](bnnspoolingfunctionaverage.md)
- [var BNNSPoolingFunctionMax: BNNSPoolingFunction](bnnspoolingfunctionmax.md)
- [func BNNSFilterCreateLayerPooling(UnsafePointer<BNNSLayerParametersPooling>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerpooling(_:_:).md)
  Returns a new pooling layer.
- [func BNNSPoolingFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, UnsafeMutablePointer<Int>?, Int) -> Int32](bnnspoolingfilterapplybatch(_:_:_:_:_:_:_:_:).md)
  Applies a pooling filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSPoolingFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafePointer<Int>?, Int) -> Int32](bnnspoolingfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a pooling filter backward to generate gradients.
- [func BNNSPoolingFilterApplyBatchEx(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, BNNSDataType, UnsafeMutableRawPointer?, Int) -> Int32](bnnspoolingfilterapplybatchex(_:_:_:_:_:_:_:_:_:).md)
  Applies a pooling filter to a set of input objects with support for multiple data types for indices.
- [func BNNSPoolingFilterApplyBackwardBatchEx(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, BNNSDataType, UnsafeRawPointer?, Int) -> Int32](bnnspoolingfilterapplybackwardbatchex(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a pooling filter backward to generate gradients with support for multiple data types for indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspooling)*