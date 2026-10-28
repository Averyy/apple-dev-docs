---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/logsumexp(axis:keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# logSumExp(axis:keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

A `log-sum-exp` reduction over the given axis.

## Declaration

```swift
func logSumExp(axis: Int, keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The log-sum-exp reduction is a numerically stable version of:

```swift
log(sum(exp(a), axis))
```

### See Also

- [Reduction Functions](../reduction.md)
- [`logSumExp(axes:keepDims:stream:)`](./logsumexp%28axes,keepdims,stream%29.md)
- [`logSumExp(keepDims:stream:)`](./logsumexp%28keepdims,stream%29.md)
- [`logSumExp(_:axes:keepDims:stream:)`](../logsumexp%28_,axes,keepdims,stream%29.md)

## Parameters

- `axis`: Axis to reduce over
- `keepDims`: If `true` keep reduced axis as singleton dimension
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
- [func min(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./min%28keepdims,stream%29.md)
  A `min` reduction over the entire array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/logsumexp(axis:keepdims:stream:))*