# BNNSNormalizationFilterApplyBatch(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a normalization filter to a set of input objects, writing the result to a set of output objects.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
func BNNSNormalizationFilterApplyBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ in: UnsafeRawPointer, _ in_stride: Int, _ out: UnsafeMutableRawPointer, _ out_stride: Int, _ training: Bool) -> Int32
```

```c
int BNNSNormalizationFilterApplyBatch(BNNSFilter filter, size_t batch_size, const void *in, size_t in_stride, void *out, size_t out_stride, bool training);
```

## Parameters

- `filter`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `in`: Pointer to the input data.
- `in_stride`: Increment, in values, between inputs.
- `out`: Pointer to the output data.
- `out_stride`: Increment, in values, between outputs.
- `training`: Set to true during training and false during inference.

## See Also

### Normalization layers
- [class NormalizationLayer](./bnns/normalizationlayer.md)
  A layer object that wraps a normalization filter and manages its deinitialization.
- [struct BNNSLayerParametersNormalization](./bnnslayerparametersnormalization.md)
  A structure that contains the parameters of a normalization layer.
- [func BNNSFilterCreateLayerNormalization(BNNSFilterType, UnsafePointer<BNNSLayerParametersNormalization>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayernormalization%28_,_,_%29.md)
  Returns a new normalization layer.
- [func BNNSNormalizationFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?) -> Int32](./bnnsnormalizationfilterapplybackwardbatch%28_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a normalization filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsnormalizationfilterapplybatch(_:_:_:_:_:_:_:))*