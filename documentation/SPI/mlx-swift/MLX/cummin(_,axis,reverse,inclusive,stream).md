---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/cummin(_:axis:reverse:inclusive:stream:)"
framework: "mlx-swift/MLX"
---

# cummin(_:axis:reverse:inclusive:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Return the cumulative minimum of the elements along the given axis.

## Declaration

```swift
func cummin(_ array: MLXArray, axis: Int, reverse: Bool = false, inclusive: Bool = true, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

#### Discussion

```swift
let array = MLXArray([5, 8, 4, 9], [2, 2])

// result is [[5, 8], [4, 8]] -- cumulative min along the columns
let result = array.cummin(axis: 0)
```

##### See Also

- [Cumulative Operations](./cumulative.md)
- [`cummin(_:reverse:inclusive:stream:)`](./cummin%28_,reverse,inclusive,stream%29.md)
- [`cummin(axis:reverse:inclusive:stream:)`](./mlxarray/cummin%28axis,reverse,inclusive,stream%29.md)

## See Also

### Cumulative
- [func cummax(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummax%28_,axis,reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements along the given axis.
- [func cummax(MLXArray, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummax%28_,reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements over the flattened array.
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/cummin(_:axis:reverse:inclusive:stream:))*