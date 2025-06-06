# BNNSFusedFilterApplyBackwardBatch(_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a fused filter backward to generate input gradients.

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
func BNNSFusedFilterApplyBackwardBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ in: UnsafeRawPointer?, _ in_stride: Int, _ in_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ in_delta_stride: Int, _ out: UnsafeRawPointer?, _ out_stride: Int, _ out_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ out_delta_stride: Int, _ delta_parameters: UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32
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
- `delta_parameters`: Pointer to an array of parameter delta pointers.

## See Also

- [protocol FusableLayerParameters](fusablelayerparameters.md)
- [class FusedParametersLayer](bnns/fusedparameterslayer.md)
  A layer object that wraps a fused layer and manages its deinitialization.
- [class FusedConvolutionNormalizationLayer](bnns/fusedconvolutionnormalizationlayer.md)
  A layer object that wraps a fused, convolution normalization layer and manages its deinitialization.
- [class FusedFullyConnectedNormalizationLayer](bnns/fusedfullyconnectednormalizationlayer.md)
  A layer object that wraps a fused, fully connected normalization layer and manages its deinitialization.
- [struct BNNSFilterType](bnnsfiltertype.md)
  Constants that define the component filters of a fused layer.
- [func BNNSFilterCreateFusedLayer(Int, UnsafePointer<BNNSFilterType>, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatefusedlayer(_:_:_:_:).md)
  Returns a new fused layer.
- [func BNNSFusedFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, Bool) -> Int32](bnnsfusedfilterapplybatch(_:_:_:_:_:_:_:).md)
  Applies a fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<Int>, UnsafeMutableRawPointer, Int, Bool) -> Int32](bnnsfusedfilterapplymultiinputbatch(_:_:_:_:_:_:_:_:).md)
  Applies a multiple-input fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyBackwardMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafePointer<Int>?, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafePointer<Int>, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32](bnnsfusedfilterapplybackwardmultiinputbatch(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a multiple-input fused filter backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfusedfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:))*