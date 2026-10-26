---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/l2normalized(axis:eps:)"
framework: "mlx-swift/MLX"
---

# l2Normalized(axis:eps:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Returns a new array normalized by its L2 norm along the specified axis.

## Declaration

```swift
func l2Normalized(axis: Int = -1, eps: Float = 1e-12) -> MLXArray
```

#### Return Value

An `MLXArray` with the same shape as the original, normalized along `axis`.

#### Discussion

This operation scales the vectors along `axis` to unit length. If the norm is smaller than `eps`, it is clamped to `eps` to ensure numerical stability and prevent division by zero.

> **Complexity**: O(n), where n is the total number of elements in the array.

## Parameters

- `axis`: The axis along which to compute the norm. Defaults to `-1`.
- `eps`: A small epsilon value to prevent division by zero. Defaults to `1e-12`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/l2normalized(axis:eps:))*