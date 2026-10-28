---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/contiguous(_:allowcolmajor:stream:)"
framework: "mlx-swift/MLX"
---

# contiguous(_:allowColMajor:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Force an array to be row contiguous. Copy if necessary.

## Declaration

```swift
func contiguous(_ a: MLXArray, allowColMajor: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

The row or col contiguous output.

## Parameters

- `a`: Input array
- `allowColMajor`: Consider column major as contiguous and don’t copy
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/contiguous(_:allowcolmajor:stream:))*