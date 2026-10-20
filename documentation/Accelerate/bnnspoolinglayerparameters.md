# BNNSPoolingLayerParameters

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure containing pooling layer parameters.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersPooling)
- iPadOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersPooling)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: BNNSLayerParametersPooling)
- macOS 10.12+ - Deprecated in 11.0 (renamed: BNNSLayerParametersPooling)
- tvOS 10.0+ - Deprecated in 14.0 (renamed: BNNSLayerParametersPooling)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: BNNSLayerParametersPooling)
- watchOS 3.0+ - Deprecated in 7.0 (renamed: BNNSLayerParametersPooling)

> **Deprecated**: Use [`BNNSLayerParametersPooling`](./bnnslayerparameterspooling.md) instead.

## Declaration

```swift
struct BNNSPoolingLayerParameters
```

```c
typedef struct { ... } BNNSPoolingLayerParameters;
```

## Topics

### Initializers
- [init()](./bnnspoolinglayerparameters/init%28%29.md)
- [init(x_stride: Int, y_stride: Int, x_padding: Int, y_padding: Int, k_width: Int, k_height: Int, in_channels: Int, out_channels: Int, pooling_function: BNNSPoolingFunction, bias: BNNSLayerData, activation: BNNSActivation)](./bnnspoolinglayerparameters/init%28x_stride,y_stride,x_padding,y_padding,k_width,k_height,in_channels,out_channels,pooling_function,bias,activation%29.md)
  Returns a new pooling layer parameters structure
- [init(x_stride: Int, y_stride: Int, x_padding: Int, y_padding: Int, k_width: Int, k_height: Int, in_channels: Int, out_channels: Int, pooling_function: BNNSPoolingFunction)](./bnnspoolinglayerparameters/init%28x_stride,y_stride,x_padding,y_padding,k_width,k_height,in_channels,out_channels,pooling_function%29.md)
### Instance Properties
- [var activation: BNNSActivation](./bnnspoolinglayerparameters/activation.md)
  The layer activation function.
- [var bias: BNNSLayerData](./bnnspoolinglayerparameters/bias.md)
  Layer bias, one for each output channel.
- [var in_channels: Int](./bnnspoolinglayerparameters/in_channels.md)
  The number of input channels.
- [var k_height: Int](./bnnspoolinglayerparameters/k_height.md)
  The height of the convolution kernel.
- [var k_width: Int](./bnnspoolinglayerparameters/k_width.md)
  The width of the convolution kernel.
- [var out_channels: Int](./bnnspoolinglayerparameters/out_channels.md)
  The number of output channels.
- [var pooling_function: BNNSPoolingFunction](./bnnspoolinglayerparameters/pooling_function.md)
  The pooling function to apply to each sample.
- [var x_padding: Int](./bnnspoolinglayerparameters/x_padding.md)
  The X padding.
- [var x_stride: Int](./bnnspoolinglayerparameters/x_stride.md)
  The X increment in the input image.
- [var y_padding: Int](./bnnspoolinglayerparameters/y_padding.md)
  The Y padding.
- [var y_stride: Int](./bnnspoolinglayerparameters/y_stride.md)
  The Y increment in the input image.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Pooling layers
- [func BNNSFilterCreatePoolingLayer(UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSPoolingLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatepoolinglayer%28_,_,_,_%29.md)
  Returns a pooling  filter, initialized with input, output, layer, and filter parameters.
- [class PoolingLayer](./bnns/poolinglayer.md)
  A layer object that wraps a pooling filter and manages its deinitialization.
- [struct BNNSPoolingFunction](./bnnspoolingfunction.md)
  Constants that describe pooling functions.
- [var BNNSPoolingFunctionAverage: BNNSPoolingFunction](./bnnspoolingfunctionaverage.md)
- [var BNNSPoolingFunctionMax: BNNSPoolingFunction](./bnnspoolingfunctionmax.md)
- [struct BNNSLayerParametersPooling](./bnnslayerparameterspooling.md)
  A structure that contains the parameters of a pooling layer.
- [func BNNSFilterCreateLayerPooling(UnsafePointer<BNNSLayerParametersPooling>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerpooling%28_,_%29.md)
  Returns a new pooling layer.
- [func BNNSPoolingFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, UnsafeMutablePointer<Int>?, Int) -> Int32](./bnnspoolingfilterapplybatch%28_,_,_,_,_,_,_,_%29.md)
  Applies a pooling filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSPoolingFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafePointer<Int>?, Int) -> Int32](./bnnspoolingfilterapplybackwardbatch%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a pooling filter backward to generate gradients.
- [func BNNSPoolingFilterApplyBatchEx(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, BNNSDataType, UnsafeMutableRawPointer?, Int) -> Int32](./bnnspoolingfilterapplybatchex%28_,_,_,_,_,_,_,_,_%29.md)
  Applies a pooling filter to a set of input objects with support for multiple data types for indices.
- [func BNNSPoolingFilterApplyBackwardBatchEx(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, BNNSDataType, UnsafeRawPointer?, Int) -> Int32](./bnnspoolingfilterapplybackwardbatchex%28_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a pooling filter backward to generate gradients with support for multiple data types for indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnspoolinglayerparameters)*