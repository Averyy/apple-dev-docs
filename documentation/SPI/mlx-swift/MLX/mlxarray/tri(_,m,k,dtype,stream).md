---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/tri(_:m:k:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# tri(_:m:k:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

An array with ones at and below the given diagonal and zeros elsewhere and a given [`DType`](../dtype.md).

## Declaration

```swift
static func tri(_ n: Int, m: Int? = nil, k: Int = 0, dtype: DType, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Example:

```swift
// [5, 5] array with the lower triangle filled with 1s
let r = MLXArray.triangle(5, dtype: .int32)
```

##### See Also

- [Initialization](../initialization.md)

## Parameters

- `n`: Number of rows in the output
- `m`: Number of columns in the output – equal to `n` if not specified
- `k`: Index of the diagonal
- `dtype`: Data type of the output array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/tri(_:m:k:dtype:stream:))*