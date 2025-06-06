# quantized(to:scale:bias:axis:)

**Framework**: ML Compute  
**Kind**: method

Converts a 32-bit floating-point tensor with the scale and bias you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
func quantized(to type: MLCDataType, scale: MLCTensor, bias: MLCTensor, axis: Int) -> MLCTensor?
```

#### Return Value

A tensor the system quantizes.

#### Discussion

> ❗ **Important**:  The tensor type must be [`MLCDataType.int8`](mlcdatatype/int8.md), [`MLCDataType.uint8`](mlcdatatype/uint8.md), or [`MLCDataType.int32`](mlcdatatype/int32.md).

 The tensor type must be [`MLCDataType.int8`](mlcdatatype/int8.md), [`MLCDataType.uint8`](mlcdatatype/uint8.md), or [`MLCDataType.int32`](mlcdatatype/int32.md).

## Parameters

- `type`: The tensor data type.
- `scale`: The scale to apply for quantizing.
- `bias`: The offset value that maps to float zero.
- `axis`: The dimension on which to apply per-channel quantization.

## See Also

- [func quantized(to: MLCDataType, scale: Float, bias: Int) -> MLCTensor?](mlctensor/quantized(to:scale:bias:).md)
  Converts a 32-bit floating-point tensor with the scale and bias you specify.
- [func dequantized(to: MLCDataType, scale: MLCTensor, zeroPoint: MLCTensor) -> MLCTensor?](mlctensor/dequantized(to:scale:zeropoint:).md)
  Converts a tensor you quantize to a 32-bit floating-point tensor.
- [func dequantized(to: MLCDataType, scale: MLCTensor, bias: MLCTensor, axis: Int) -> MLCTensor?](mlctensor/dequantized(to:scale:bias:axis:).md)
  Converts a tensor you quantize to a 32-bit floating-point tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/quantized(to:scale:bias:axis:))*