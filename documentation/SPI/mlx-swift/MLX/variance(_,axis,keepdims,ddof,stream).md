---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/variance(_:axis:keepdims:ddof:stream:)"
framework: "mlx-swift/MLX"
---

# variance(_:axis:keepDims:ddof:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the variance(s) over the given axes

## Declaration

```swift
func variance(_ array: MLXArray, axis: Int, keepDims: Bool = false, ddof: Int = 0, stream: StreamOrDevice = .default) -> MLXArray
```

##### See Also

- [Reduction Functions](./reduction.md)
- [`variance(_:axes:keepDims:ddof:stream:)`](./variance%28_,axes,keepdims,ddof,stream%29.md)
- [`variance(_:keepDims:ddof:stream:)`](./variance%28_,keepdims,ddof,stream%29.md)
- [`variance(axes:keepDims:ddof:stream:)`](./mlxarray/variance%28axes,keepdims,ddof,stream%29.md)

## Parameters

- `array`: Input array
- `axis`: Axes to reduce over
- `keepDims`: If `true` keep the reduces axis as singleton dimensions
- `ddof`: The divisor to compute the variance is `N - ddof`
- `stream`: Stream or device to evaluate on

## See Also

### Aggregating Reduction Free Functions
- [func countNonzero(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./countnonzero%28_,keepdims,stream%29.md)
  Count the number of non-zero elements in the array over all axes.
- [func countNonzero(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./countnonzero%28_,axis,keepdims,stream%29.md)
  Count the number of non-zero elements in the array over the given axis.
- [func countNonzero(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./countnonzero%28_,axes,keepdims,stream%29.md)
  Count the number of non-zero elements in the array over the given axes.
- [func logSumExp(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28_,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the entire array.
- [func logSumExp(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28_,axis,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the given axis.
- [func logSumExp(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28_,axes,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the given axes.
- [func product(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./product%28_,keepdims,stream%29.md)
  A `product` reduction over the entire array.
- [func product(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./product%28_,axis,keepdims,stream%29.md)
  A `product` reduction over the given axis.
- [func product(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./product%28_,axes,keepdims,stream%29.md)
  A `product` reduction over the given axes.
- [func max(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28_,keepdims,stream%29.md)
  A `max` reduction over the entire array.
- [func max(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28_,axis,keepdims,stream%29.md)
  A `max` reduction over the given axis.
- [func max(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28_,axes,keepdims,stream%29.md)
  A `max` reduction over the given axes.
- [func mean(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28_,keepdims,stream%29.md)
  A `mean` reduction over the entire array.
- [func mean(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28_,axis,keepdims,stream%29.md)
  A `mean` reduction over the given axis.
- [func mean(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28_,axes,keepdims,stream%29.md)
  A `mean` reduction over the given axes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/variance(_:axis:keepdims:ddof:stream:))*