---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/cummax(axis:reverse:inclusive:stream:)"
framework: "mlx-swift/MLX"
---

# cummax(axis:reverse:inclusive:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Return the cumulative maximum of the elements along the given axis.

## Declaration

```swift
func cummax(axis: Int, reverse: Bool = false, inclusive: Bool = true, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

#### Discussion

```swift
let array = MLXArray([5, 8, 4, 9], [2, 2])

// result is [[5, 8], [5, 9]] -- cumulative max along the columns
let result = array.cummax(axis: 0)
```

##### See Also

- [Cumulative Operations](../cumulative.md)
- [`cummax(reverse:inclusive:stream:)`](./cummax%28reverse,inclusive,stream%29.md)
- [`cummax(_:axis:reverse:inclusive:stream:)`](../cummax%28_,axis,reverse,inclusive,stream%29.md)

## Parameters

- `axis`: Axis to reduce over
- `reverse`: Reverse the reduction
- `inclusive`: Include the initial value
- `stream`: Stream or device to evaluate on

## See Also

### MLXArray Methods
- [func cummax(reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummax%28reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements over the flattened array.
- [func cummin(axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummin%28axis,reverse,inclusive,stream%29.md)
  Return the cumulative minimum of the elements along the given axis.
- [func cummin(reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummin%28reverse,inclusive,stream%29.md)
  Return the cumulative minimum of the elements over the flattened array.
- [func cumprod(axis: Int, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumprod%28axis,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative product of the elements along the given axis.
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [func cumsum(axis: Int, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumsum%28axis,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative sum of the elements along the given axis.
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [func logCumsumExp(axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./logcumsumexp%28axis,reverse,inclusive,stream%29.md)
  Return the cumulative logsumexp of the elements along the given axis.
- [func logCumsumExp(reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./logcumsumexp%28reverse,inclusive,stream%29.md)
  Return the cumulative logsumexp of the elements of the flattened array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/cummax(axis:reverse:inclusive:stream:))*