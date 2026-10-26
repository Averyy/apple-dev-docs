---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/logcumsumexp(_:reverse:inclusive:stream:)"
framework: "mlx-swift/MLX"
---

# logCumsumExp(_:reverse:inclusive:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Return the cumulative logsumexp of the elements of the flattened array.

## Declaration

```swift
func logCumsumExp(_ array: MLXArray, reverse: Bool = false, inclusive: Bool = true, stream: StreamOrDevice = .default) -> MLXArray
```

##### See Also

- [Cumulative Operations](./cumulative.md)

## Parameters

- `array`: Input array
- `reverse`: Reverse the reduction
- `inclusive`: Include the initial value
- `stream`: Stream or device to evaluate on

## See Also

### Free Functions
- [func cummax(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummax%28_,axis,reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements along the given axis.
- [func cummax(MLXArray, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummax%28_,reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements over the flattened array.
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
- [func logCumsumExp(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./logcumsumexp%28_,axis,reverse,inclusive,stream%29.md)
  Return the cumulative logsumexp of the elements along the given axis.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/logcumsumexp(_:reverse:inclusive:stream:))*