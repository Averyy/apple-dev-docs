---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/diagonal(offset:axis1:axis2:stream:)"
framework: "mlx-swift/MLX"
---

# diagonal(offset:axis1:axis2:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Return specified diagonals.

## Declaration

```swift
func diagonal(offset: Int = 0, axis1: Int = 0, axis2: Int = 1, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

If self is 2-D, then a 1-D array containing the diagonal at the given `offset` is returned.

If self has more than two dimensions, then `axis1` and `axis2` determine the 2D subarrays from which diagonals are extracted. The new shape is the original shape with `axis1` and `axis2` removed and a new dimension inserted at the end corresponding to the diagonal.

### See Also

- [`diag(k:stream:)`](./diag%28k,stream%29.md)

## Parameters

- `offset`: Offset of the diagonal.  Can be positive or negative
- `axis1`: First axis of the 2-D sub-array from which the diagonals should be taken
- `axis2`: Second axis of the 2-D sub-array from which the diagonals should be taken
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/diagonal(offset:axis1:axis2:stream:))*