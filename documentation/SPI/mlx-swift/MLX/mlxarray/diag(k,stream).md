---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/diag(k:stream:)"
framework: "mlx-swift/MLX"
---

# diag(k:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Extract a diagonal or construct a diagonal matrix.

## Declaration

```swift
func diag(k: Int = 0, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

If self is 1-D then a diagonal matrix is constructed with self on the `k`-th diagonal. If self is 2-D then the `k`-th diagonal is returned.

##### See Also

- [`diagonal(offset:axis1:axis2:stream:)`](./diagonal%28offset,axis1,axis2,stream%29.md)

## Parameters

- `k`: The diagonal to extract or construct
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/diag(k:stream:))*