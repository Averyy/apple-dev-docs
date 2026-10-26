---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/flatten(_:startaxis:endaxis:stream:)"
framework: "mlx-swift/MLX"
---

# flatten(_:startAxis:endAxis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Flatten an array.

## Declaration

```swift
func flatten(_ a: MLXArray, startAxis: Int, endAxis: Int = -1, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

The axes flattened will be between `start_axis` and `end_axis`, inclusive. Negative axes are supported. After converting negative axis to positive, axes outside the valid range will be clamped to a valid value, `start_axis` to `0` and `end_axis` to `ndim - 1`.

## Parameters

- `a`: Input array
- `startAxis`: First dim to flatten
- `endAxis`: Last dim to flatten
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/flatten(_:startaxis:endaxis:stream:))*