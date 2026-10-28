---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/cross(_:_:axis:stream:)"
framework: "mlx-swift/MLX"
---

# cross(_:_:axis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Compute the cross product of two arrays along a specified axis.

## Declaration

```swift
static func cross(_ a: MLXArray, _ b: MLXArray, axis: Int = -1, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The cross product is defined for arrays with size 2 or 3 in the specified axis. If the size is 2 then the third value is assumed to be zero.

## Parameters

- `a`: Input array
- `b`: Input array
- `axis`: Axis along which to compute the cross product
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/cross(_:_:axis:stream:))*