---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/cummax(_:reverse:inclusive:stream:)"
framework: "mlx-swift/MLX"
---

# cummax(_:reverse:inclusive:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Return the cumulative maximum of the elements over the flattened array.

## Declaration

```swift
func cummax(_ array: MLXArray, reverse: Bool = false, inclusive: Bool = true, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

```swift
let array = MLXArray([5, 8, 4, 9], [2, 2])

// result is [5, 8, 8, 9]
let result = array.cummax()
```

##### See Also

- [Cumulative Operations](./cumulative.md)
- [`cummax(_:axis:reverse:inclusive:stream:)`](./cummax%28_,axis,reverse,inclusive,stream%29.md)
- [`cummax(axis:reverse:inclusive:stream:)`](./mlxarray/cummax%28axis,reverse,inclusive,stream%29.md)

## See Also

### Cumulative
- [func cummax(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummax%28_,axis,reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements along the given axis.
- [func cummin(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummin%28_,axis,reverse,inclusive,stream%29.md)
  Return the cumulative minimum of the elements along the given axis.
- [func cummin(MLXArray, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummin%28_,reverse,inclusive,stream%29.md)
  Return the cumulative minimum of the elements over the flattened array.
- [func cumprod(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumprod%28_,axis,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative product of the elements along the given axis.
- [func cumprod(MLXArray, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumprod%28_,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative product of the elements over the flattened array.
- [func cumsum(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumsum%28_,axis,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative sum of the elements along the given axis.
- [func cumsum(MLXArray, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumsum%28_,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative sum of the elements over the flattened array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/cummax(_:reverse:inclusive:stream:))*