---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/min(_:axes:keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# min(_:axes:keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

A `min` reduction over the given axes.

## Declaration

```swift
func min(_ array: MLXArray, axes: some Collection<Int>, keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

## Discussion

```swift
let array = MLXArray([5, 8, 4, 9], [2, 2])

// result is [4, 8]
let result = array.min(axis=[0])
```

### See Also

- [Reduction Functions](./reduction.md)
- [`min(_:axis:keepDims:stream:)`](./min%28_,axis,keepdims,stream%29.md)
- [`min(_:keepDims:stream:)`](./min%28_,keepdims,stream%29.md)
- [`min(axes:keepDims:stream:)`](./mlxarray/min%28axes,keepdims,stream%29.md)

## Parameters

- `array`: Input array
- `axes`: Axes to reduce over
- `keepDims`: If `true` keep reduced axis as singleton dimension
- `stream`: Stream or device to evaluate on

## See Also

### Aggregating Reduction
- [func logSumExp(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28_,axes,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the given axes.
- [func product(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./product%28_,axis,keepdims,stream%29.md)
  A `product` reduction over the given axis.
- [func max(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28_,axes,keepdims,stream%29.md)
  A `max` reduction over the given axes.
- [func mean(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28_,axes,keepdims,stream%29.md)
  A `mean` reduction over the given axes.
- [func sum(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./sum%28_,axes,keepdims,stream%29.md)
  Sum reduce the array over the given axes.
- [func variance(MLXArray, axes: some Collection<Int>, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./variance%28_,axes,keepdims,ddof,stream%29.md)
  Compute the variance(s) over the given axes


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/min(_:axes:keepdims:stream:))*