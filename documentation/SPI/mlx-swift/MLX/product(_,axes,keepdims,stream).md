---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/product(_:axes:keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# product(_:axes:keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

A `product` reduction over the given axes.

## Declaration

```swift
func product(_ array: MLXArray, axes: some Collection<Int>, keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

## Discussion

```swift
let array = MLXArray([5, 8, 4, 9], [2, 2])

// result is [20, 72]
let result = array.product(axis=[0])
```

### See Also

- [Reduction Functions](./reduction.md)
- [`product(_:axis:keepDims:stream:)`](./product%28_,axis,keepdims,stream%29.md)
- [`product(_:keepDims:stream:)`](./product%28_,keepdims,stream%29.md)
- [`product(axes:keepDims:stream:)`](./mlxarray/product%28axes,keepdims,stream%29.md)

## Parameters

- `array`: Input array
- `axes`: Axes to reduce over
- `keepDims`: If `true` keep reduced axis as singleton dimension
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
- [func median(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./median%28_,keepdims,stream%29.md)
  Compute the median(s) over the full array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/product(_:axes:keepdims:stream:))*