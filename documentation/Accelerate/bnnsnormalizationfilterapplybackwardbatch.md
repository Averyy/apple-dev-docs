# BNNSNormalizationFilterApplyBackwardBatch(_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a normalization filter backward to generate gradients.

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
func BNNSNormalizationFilterApplyBackwardBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ in_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ in_delta_stride: Int, _ out: UnsafeRawPointer?, _ out_stride: Int, _ out_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ out_delta_stride: Int, _ beta_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ gamma_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?) -> Int32
```

## Parameters

- `filter`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `in_delta`: The descriptor of the input delta.
- `in_delta_stride`: Increment, in values, between input delta objects.
- `out`: Pointer to output object.
- `out_stride`: Increment, in values, between output objects.
- `out_delta`: The descriptor of the output delta.
- `out_delta_stride`: Increment, in values, between output delta objects.
- `beta_delta`: The descriptor of the beta delta.
- `gamma_delta`: The descriptor of the gamma delta.

## See Also

- [class NormalizationLayer](bnns/normalizationlayer.md)
  A layer object that wraps a normalization filter and manages its deinitialization.
- [struct BNNSLayerParametersNormalization](bnnslayerparametersnormalization.md)
  A structure that contains the parameters of a normalization layer.
- [func BNNSFilterCreateLayerNormalization(BNNSFilterType, UnsafePointer<BNNSLayerParametersNormalization>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayernormalization(_:_:_:).md)
  Returns a new normalization layer.
- [func BNNSNormalizationFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, Bool) -> Int32](bnnsnormalizationfilterapplybatch(_:_:_:_:_:_:_:).md)
  Applies a normalization filter to a set of input objects, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsnormalizationfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:))*