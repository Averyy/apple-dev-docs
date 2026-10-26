---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/eye(_:m:k:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# eye(_:m:k:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Create an identity matrix or a general diagonal matrix given a [`DType`](../dtype.md).

## Declaration

```swift
static func eye(_ n: Int, m: Int? = nil, k: Int = 0, dtype: DType, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Example:

```swift
//  create [10, 10] array with 1's on the diagonal.
let r = MLXArray.eye(10, dtype: .int32)
```

##### See Also

- [Initialization](../initialization.md)
- [`identity(_:type:stream:)`](./identity%28_,type,stream%29.md)

## Parameters

- `n`: Number of rows in the output
- `m`: Number of columns in the output – equal to `n` if not specified
- `k`: Index of the diagonal
- `dtype`: Data type of the output array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/eye(_:m:k:dtype:stream:))*