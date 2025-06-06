# BNNSPermuteFilterApplyBackwardBatch(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a permute filter backward to generate gradients.

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
func BNNSPermuteFilterApplyBackwardBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ in_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ in_delta_stride: Int, _ out_delta: UnsafePointer<BNNSNDArrayDescriptor>, _ out_delta_stride: Int) -> Int32
```

## Parameters

- `filter`: The filter to apply.
- `batch_size`: Number of input-output pairs to process.
- `in_delta`: The descriptor of the input delta.
- `in_delta_stride`: Increment, in values, between input delta objects.
- `out_delta`: The descriptor of the output delta.
- `out_delta_stride`: Increment, in values, between output delta objects.

## See Also

- [class PermuteLayer](bnns/permutelayer.md)
  A layer object that wraps a permute filter and manages its deinitialization.
- [struct BNNSLayerParametersPermute](bnnslayerparameterspermute.md)
  A structure that contains the parameters of a permute layer.
- [func BNNSFilterCreateLayerPermute(UnsafePointer<BNNSLayerParametersPermute>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerpermute(_:_:).md)
  Returns a new permute layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnspermutefilterapplybackwardbatch(_:_:_:_:_:_:))*