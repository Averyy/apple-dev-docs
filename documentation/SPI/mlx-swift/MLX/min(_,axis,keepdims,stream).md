---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/min(_:axis:keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# min(_:axis:keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

A `min` reduction over the given axis.

## Declaration

```swift
func min(_ array: MLXArray, axis: Int, keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

```swift
let array = MLXArray([5, 8, 4, 9], [2, 2])

// result is [5, 4]
let result = array.min(axis=1)
```

##### See Also

- [Reduction Functions](./reduction.md)
- [`min(_:axes:keepDims:stream:)`](./min%28_,axes,keepdims,stream%29.md)
- [`min(_:keepDims:stream:)`](./min%28_,keepdims,stream%29.md)
- [`min(axes:keepDims:stream:)`](./mlxarray/min%28axes,keepdims,stream%29.md)

## Parameters

- `array`: Input array
- `axis`: Axis to reduce over
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/min(_:axis:keepdims:stream:))*