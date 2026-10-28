---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/contiguous(allowcolmajor:stream:)"
framework: "mlx-swift/MLX"
---

# contiguous(allowColMajor:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Force an array to be row contiguous. Copy if necessary.

## Declaration

```swift
func contiguous(allowColMajor: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

The row or col contiguous output.

## Parameters

- `allowColMajor`: Consider column major as contiguous and don’t copy
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/contiguous(allowcolmajor:stream:))*