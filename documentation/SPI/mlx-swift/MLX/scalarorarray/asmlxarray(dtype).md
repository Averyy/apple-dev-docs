---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/scalarorarray/asmlxarray(dtype:)"
framework: "mlx-swift/MLX"
---

# asMLXArray(dtype:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Convert to [`MLXArray`](../mlxarray.md) using the optional suggested [`DType`](../dtype.md).

## Declaration

```swift
func asMLXArray(dtype: DType?) -> MLXArray
```

## Discussion

If the receiver is a scalar this should consider the `dtype` when producing an `MLXArray`.  For example:

```swift
let x = MLXArray(1.5, dtype: .float16)

// the 2.5 is expected to conform to the .float16 of the other
// argument and r will be a .float16 result.
let r = x + 2.5
```

See also `toArrays(_:_:)` (internal).

## Default Implementations

### ScalarOrArray Implementations
- [func asMLXArray(dtype: DType?) -> MLXArray](./asmlxarray%28dtype%29-14eqb.md)
  Convert to [`MLXArray`](../mlxarray.md) using the optional suggested [`DType`](../dtype.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/scalarorarray/asmlxarray(dtype:))*