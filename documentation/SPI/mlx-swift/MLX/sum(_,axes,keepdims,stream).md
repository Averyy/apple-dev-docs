---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/sum(_:axes:keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# sum(_:axes:keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Sum reduce the array over the given axes.

## Declaration

```swift
func sum(_ array: MLXArray, axes: some Collection<Int>, keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

### See Also

- [Reduction Functions](./reduction.md)
- [`sum(_:axis:keepDims:stream:)`](./sum%28_,axis,keepdims,stream%29.md)
- [`sum(_:keepDims:stream:)`](./sum%28_,keepdims,stream%29.md)
- [`sum(axes:keepDims:stream:)`](./mlxarray/sum%28axes,keepdims,stream%29.md)

## Parameters

- `array`: Input array
- `axes`: Axes to reduce over
- `keepDims`: If `true` keep the reduces axes as singleton dimensions
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
- [func min(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./min%28_,axes,keepdims,stream%29.md)
  A `min` reduction over the given axes.
- [func variance(MLXArray, axes: some Collection<Int>, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./variance%28_,axes,keepdims,ddof,stream%29.md)
  Compute the variance(s) over the given axes


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/sum(_:axes:keepdims:stream:))*