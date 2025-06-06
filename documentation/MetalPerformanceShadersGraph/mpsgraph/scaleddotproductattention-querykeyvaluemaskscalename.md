# scaledDotProductAttention(query:key:value:mask:scale:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a scaled dot product attention (SDPA) operation and returns the result tensor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func scaledDotProductAttention(query queryTensor: MPSGraphTensor, key keyTensor: MPSGraphTensor, value valueTensor: MPSGraphTensor, mask maskTensor: MPSGraphTensor?, scale: Float, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

SDPA Op computes attention by computing softmax(scale * QK^T + M)V. queryTensor Q with shape [B, Hq, Nq, F] and keyTensor K with shape [B, Hq, Nkv, F], with Q’s H dimension expandable to satisfy matmul QK^T. maskTensor M’s shape should be broadcast compatible to satisfy (QK^T + M). valueTensor V with shape [B, Hv, Nkv, F] should satisfy the matmul (QK^T + M)V.

## Parameters

- `queryTensor`: A tensor that represents the query projection.
- `keyTensor`: A tensor that represents the key projection.
- `valueTensor`: A tensor that represents the value projection.
- `maskTensor`: An optional tensor that contains a mask that is applied to the scaled, matrix   multiplied query and value matrices. If mask tensor is nil, the QK^T is not element-wise masked.
- `scale`: A scale that is applied to the result of query and value matrix multiply.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/scaleddotproductattention(query:key:value:mask:scale:name:))*