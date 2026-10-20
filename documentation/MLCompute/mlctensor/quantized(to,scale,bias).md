# quantized(to:scale:bias:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Converts a 32-bit floating-point tensor with the scale and bias you specify.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
func quantized(to type: MLCDataType, scale: Float, bias: Int) -> MLCTensor?
```

```objc
- (MLCTensor *) tensorByQuantizingToType:(MLCDataType) type scale:(float) scale bias:(NSInteger) bias;
```

#### Return Value

A tensor the system quantizes.

#### Discussion

> ❗ **Important**:  The tensor type must be [`MLCDataType.int8`](../mlcdatatype/int8.md), [`MLCDataType.uint8`](../mlcdatatype/uint8.md), or [`MLCDataType.int32`](../mlcdatatype/int32.md).

## Parameters

- `type`: The tensor data type.
- `scale`: The scale to apply for quantizing.
- `bias`: The offset value that maps to float zero.

## See Also

### Converting Tensors
- [func quantized(to: MLCDataType, scale: MLCTensor, bias: MLCTensor, axis: Int) -> MLCTensor?](./quantized%28to,scale,bias,axis%29.md)
  Converts a 32-bit floating-point tensor with the scale and bias you specify.
- [func dequantized(to: MLCDataType, scale: MLCTensor, zeroPoint: MLCTensor) -> MLCTensor?](./dequantized%28to,scale,zeropoint%29.md)
  Converts a tensor you quantize to a 32-bit floating-point tensor.
- [func dequantized(to: MLCDataType, scale: MLCTensor, bias: MLCTensor, axis: Int) -> MLCTensor?](./dequantized%28to,scale,bias,axis%29.md)
  Converts a tensor you quantize to a 32-bit floating-point tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/quantized(to:scale:bias:))*