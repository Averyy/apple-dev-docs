# BNNSPoolingFilterApplyBackwardBatch(_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a pooling filter backward to generate gradients.

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
func BNNSPoolingFilterApplyBackwardBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ in: UnsafeRawPointer?, _ in_stride: Int, _ in_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ in_delta_stride: Int, _ out: UnsafeRawPointer?, _ out_stride: Int, _ out_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ out_delta_stride: Int, _ bias_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ indices: UnsafePointer<Int>?, _ idx_stride: Int) -> Int32
```

## Parameters

- `filter`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `in`: Pointer to input object.
- `in_stride`: Increment, in values, between input objects.
- `in_delta`: The descriptor of the input delta.
- `in_delta_stride`: Increment, in values, between input delta objects.
- `out`: Pointer to output object.
- `out_stride`: Increment, in values, between output objects.
- `out_delta`: The descriptor of the output delta.
- `out_delta_stride`: Increment, in values, between output delta objects.
- `bias_delta`: The descriptor of the bias delta.
- `indices`: Pointer to indices object.
- `idx_stride`: Increment, in values, between indices objects.

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
- [func BNNSPoolingFilterApplyBatchEx(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, BNNSDataType, UnsafeMutableRawPointer?, Int) -> Int32](bnnspoolingfilterapplybatchex(_:_:_:_:_:_:_:_:_:).md)
  Applies a pooling filter to a set of input objects with support for multiple data types for indices.
- [func BNNSPoolingFilterApplyBackwardBatchEx(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, BNNSDataType, UnsafeRawPointer?, Int) -> Int32](bnnspoolingfilterapplybackwardbatchex(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a pooling filter backward to generate gradients with support for multiple data types for indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnspoolingfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:_:_:))*