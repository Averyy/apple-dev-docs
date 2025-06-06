# BNNSPoolingFilterApplyBatchEx(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a pooling filter to a set of input objects with support for multiple data types for indices.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func BNNSPoolingFilterApplyBatchEx(_ filter: BNNSFilter?, _ batch_size: Int, _ in: UnsafeRawPointer, _ in_stride: Int, _ out: UnsafeMutableRawPointer, _ out_stride: Int, _ indices_data_type: BNNSDataType, _ indices: UnsafeMutableRawPointer?, _ idx_stride: Int) -> Int32
```

#### Discussion

This function is an extension to [`BNNSPoolingFilterApplyBatch(_:_:_:_:_:_:_:_:)`](bnnspoolingfilterapplybatch(_:_:_:_:_:_:_:_:).md) that supports 32- and 64-bit unsigned-integer indices for max pooling and unpooling.

## Parameters

- `filter`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `in`: A pointer to the input data.
- `in_stride`: The increment, in values, between inputs.
- `out`: A pointer to the output data.
- `out_stride`: The increment, in values, between outputs.
- `indices_data_type`: The data type of the indices data.
- `indices`: A pointer to the indices data.
- `idx_stride`: The increment, in values, between indices.

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
- [struct BNNSLayerParametersPooling](bnnslayerparameterspooling.md)
  A structure that contains the parameters of a pooling layer.
- [func BNNSFilterCreateLayerPooling(UnsafePointer<BNNSLayerParametersPooling>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerpooling(_:_:).md)
  Returns a new pooling layer.
- [func BNNSPoolingFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, UnsafeMutablePointer<Int>?, Int) -> Int32](bnnspoolingfilterapplybatch(_:_:_:_:_:_:_:_:).md)
  Applies a pooling filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSPoolingFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafePointer<Int>?, Int) -> Int32](bnnspoolingfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a pooling filter backward to generate gradients.
- [func BNNSPoolingFilterApplyBackwardBatchEx(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, BNNSDataType, UnsafeRawPointer?, Int) -> Int32](bnnspoolingfilterapplybackwardbatchex(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a pooling filter backward to generate gradients with support for multiple data types for indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnspoolingfilterapplybatchex(_:_:_:_:_:_:_:_:_:))*