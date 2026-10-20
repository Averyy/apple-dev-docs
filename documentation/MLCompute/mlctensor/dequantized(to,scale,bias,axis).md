# dequantized(to:scale:bias:axis:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Converts a tensor you quantize to a 32-bit floating-point tensor.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
func dequantized(to type: MLCDataType, scale: MLCTensor, bias: MLCTensor, axis: Int) -> MLCTensor?
```

```objc
- (MLCTensor *) tensorByDequantizingToType:(MLCDataType) type scale:(MLCTensor *) scale bias:(MLCTensor *) bias axis:(NSInteger) axis;
```

#### Return Value

A tensor the system dequantizes.

#### Discussion

> ❗ **Important**:  The tensor type must be [`MLCDataType.float32`](../mlcdatatype/float32.md).

## Parameters

- `type`: The tensor data type.
- `scale`: The scale the system uses when quantizing the data.
- `bias`: The offset value the system uses when quantizing the data.
- `axis`: The dimension on which to apply per-channel quantization.

## See Also

### Converting Tensors
- [func quantized(to: MLCDataType, scale: Float, bias: Int) -> MLCTensor?](./quantized%28to,scale,bias%29.md)
  Converts a 32-bit floating-point tensor with the scale and bias you specify.
- [func quantized(to: MLCDataType, scale: MLCTensor, bias: MLCTensor, axis: Int) -> MLCTensor?](./quantized%28to,scale,bias,axis%29.md)
  Converts a 32-bit floating-point tensor with the scale and bias you specify.
- [func dequantized(to: MLCDataType, scale: MLCTensor, zeroPoint: MLCTensor) -> MLCTensor?](./dequantized%28to,scale,zeropoint%29.md)
  Converts a tensor you quantize to a 32-bit floating-point tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/dequantized(to:scale:bias:axis:))*