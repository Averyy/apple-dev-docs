---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/cross(_:_:axis:stream:)"
framework: "mlx-swift/MLXLinalg"
---

# cross(_:_:axis:stream:)

**Framework**: mlx-swift/MLXLinalg  
**Kind**: func  
**Role**: Function

Compute the cross product of two arrays along a specified axis.

> **Deprecated**: cross is now available in the main MLX module

## Declaration

```swift
func cross(_ a: MLXArray, _ b: MLXArray, axis: Int = -1, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

The cross product is defined for arrays with size 2 or 3 in the specified axis. If the size is 2 then the third value is assumed to be zero.

## Parameters

- `a`: Input array
- `b`: Input array
- `axis`: Axis along which to compute the cross product
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg/cross(_:_:axis:stream:))*