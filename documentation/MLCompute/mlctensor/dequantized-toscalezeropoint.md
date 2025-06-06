# dequantized(to:scale:zeroPoint:)

**Framework**: ML Compute  
**Kind**: method

Converts a tensor you quantize to a 32-bit floating-point tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
func dequantized(to type: MLCDataType, scale: MLCTensor, zeroPoint bias: MLCTensor) -> MLCTensor?
```

#### Return Value

A tensor the system dequantizes.

#### Discussion

> ❗ **Important**:  The tensor type must be [`MLCDataType.float32`](mlcdatatype/float32.md).

 The tensor type must be [`MLCDataType.float32`](mlcdatatype/float32.md).

## Parameters

- `type`: The tensor data type.
- `scale`: The scale the system uses when quantizing the data.
- `bias`: The offset value the system uses when quantizing the data.

## See Also

- [func quantized(to: MLCDataType, scale: Float, bias: Int) -> MLCTensor?](mlctensor/quantized(to:scale:bias:).md)
  Converts a 32-bit floating-point tensor with the scale and bias you specify.
- [func quantized(to: MLCDataType, scale: MLCTensor, bias: MLCTensor, axis: Int) -> MLCTensor?](mlctensor/quantized(to:scale:bias:axis:).md)
  Converts a 32-bit floating-point tensor with the scale and bias you specify.
- [func dequantized(to: MLCDataType, scale: MLCTensor, bias: MLCTensor, axis: Int) -> MLCTensor?](mlctensor/dequantized(to:scale:bias:axis:).md)
  Converts a tensor you quantize to a 32-bit floating-point tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/dequantized(to:scale:zeropoint:))*