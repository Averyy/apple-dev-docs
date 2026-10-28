---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/variance(axes:keepdims:ddof:stream:)"
framework: "mlx-swift/MLX"
---

# variance(axes:keepDims:ddof:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Compute the variance(s) over the given axes

## Declaration

```swift
func variance(axes: some Collection<Int>, keepDims: Bool = false, ddof: Int = 0, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

### See Also

- [Reduction Functions](../reduction.md)
- [`variance(axis:keepDims:ddof:stream:)`](./variance%28axis,keepdims,ddof,stream%29.md)
- [`variance(keepDims:ddof:stream:)`](./variance%28keepdims,ddof,stream%29.md)
- [`variance(_:axes:keepDims:ddof:stream:)`](../variance%28_,axes,keepdims,ddof,stream%29.md)

## Parameters

- `axes`: Axes to reduce over
- `keepDims`: If `true` keep the reduces axes as singleton dimensions
- `ddof`: The divisor to compute the variance is `N - ddof`
- `stream`: Stream or device to evaluate on

## See Also

### MLXArray Aggregating Reduction Functions
- [func countNonzero(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./countnonzero%28keepdims,stream%29.md)
  Count the number of non-zero elements in the array over all axes.
- [func countNonzero(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./countnonzero%28axis,keepdims,stream%29.md)
  Count the number of non-zero elements in the array over the given axis.
- [func countNonzero(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./countnonzero%28axes,keepdims,stream%29.md)
  Count the number of non-zero elements in the array over the given axes.
- [func logSumExp(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28keepdims,stream%29.md)
  A `log-sum-exp` reduction over the entire array.
- [func logSumExp(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28axis,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the given axis.
- [func logSumExp(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28axes,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the given axes.
- [func product(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./product%28keepdims,stream%29.md)
  A `product` reduction over the entire array.
- [func product(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./product%28axis,keepdims,stream%29.md)
  A `product` reduction over the given axis.
- [func product(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./product%28axes,keepdims,stream%29.md)
  A `product` reduction over the given axes.
- [func max(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28keepdims,stream%29.md)
  A `max` reduction over the entire array.
- [func max(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28axis,keepdims,stream%29.md)
  A `max` reduction over the given axis.
- [func max(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28axes,keepdims,stream%29.md)
  A `max` reduction over the given axes.
- [func mean(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28keepdims,stream%29.md)
  A `mean` reduction over the entire array.
- [func mean(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28axis,keepdims,stream%29.md)
  A `mean` reduction over the given axis.
- [func mean(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28axes,keepdims,stream%29.md)
  A `mean` reduction over the given axes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/variance(axes:keepdims:ddof:stream:))*