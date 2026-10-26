---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/identity(_:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# identity(_:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Create a square identity matrix with a given [`DType`](../dtype.md).

## Declaration

```swift
static func identity(_ n: Int, dtype: DType, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Example:

```swift
//  create [10, 10] array with 1's on the diagonal.
let r = MLXArray.identity(10, dtype: .int32)
```

##### See Also

- [Initialization](../initialization.md)
- [`eye(_:m:k:type:stream:)`](./eye%28_,m,k,type,stream%29.md)

## Parameters

- `n`: Number of rows and columns in the output
- `dtype`: Data type of the output array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/identity(_:dtype:stream:))*