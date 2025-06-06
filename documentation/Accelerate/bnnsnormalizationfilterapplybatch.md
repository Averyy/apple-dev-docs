# BNNSNormalizationFilterApplyBatch(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a normalization filter to a set of input objects, writing the result to a set of output objects.

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
func BNNSNormalizationFilterApplyBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ in: UnsafeRawPointer, _ in_stride: Int, _ out: UnsafeMutableRawPointer, _ out_stride: Int, _ training: Bool) -> Int32
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

- [class NormalizationLayer](bnns/normalizationlayer.md)
  A layer object that wraps a normalization filter and manages its deinitialization.
- [struct BNNSLayerParametersNormalization](bnnslayerparametersnormalization.md)
  A structure that contains the parameters of a normalization layer.
- [func BNNSFilterCreateLayerNormalization(BNNSFilterType, UnsafePointer<BNNSLayerParametersNormalization>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayernormalization(_:_:_:).md)
  Returns a new normalization layer.
- [func BNNSNormalizationFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?) -> Int32](bnnsnormalizationfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:).md)
  Applies a normalization filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsnormalizationfilterapplybatch(_:_:_:_:_:_:_:))*