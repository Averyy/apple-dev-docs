# BNNSFilterCreatePoolingLayer(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a pooling  filter, initialized with input, output, layer, and filter parameters.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerPooling(_:_:))
- iPadOS 10.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerPooling(_:_:))
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerPooling(_:_:))
- macOS 10.12+ - Deprecated in 11.0 (renamed: BNNSFilterCreateLayerPooling(_:_:))
- tvOS 10.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerPooling(_:_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: BNNSFilterCreateLayerPooling(_:_:))
- watchOS 3.0+ - Deprecated in 7.0 (renamed: BNNSFilterCreateLayerPooling(_:_:))

> **Deprecated**: Use [`BNNSFilterCreateLayerPooling(_:_:)`](./bnnsfiltercreatelayerpooling%28_,_%29.md) instead.

## Declaration

```swift
func BNNSFilterCreatePoolingLayer(_ in_desc: UnsafePointer<BNNSImageStackDescriptor>, _ out_desc: UnsafePointer<BNNSImageStackDescriptor>, _ layer_params: UnsafePointer<BNNSPoolingLayerParameters>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

```c
BNNSFilterBNNSFilterCreatePoolingLayer(const BNNSImageStackDescriptor *in_desc, const BNNSImageStackDescriptor *out_desc, const BNNSPoolingLayerParameters *layer_params, const BNNSFilterParameters *filter_params);
```

#### Return Value

A BNNSFilter object representing a pooling filter configured with the specified  parameters

## Parameters

- `in_desc`: Pointer to a `BNNSImageStackDescriptor` struct describing the input
- `out_desc`: Pointer to a `v` struct describing the output
- `layer_params`: Pointer to a `BNNSPoolingLayerParameters` struct describing the layer parameters
- `filter_params`: Pointer to a `BNNSFilterParameters` struct describing the filter parameters

## See Also

### Pooling layers
- [struct BNNSPoolingLayerParameters](./bnnspoolinglayerparameters.md)
  A structure containing pooling layer parameters.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatepoolinglayer(_:_:_:_:))*