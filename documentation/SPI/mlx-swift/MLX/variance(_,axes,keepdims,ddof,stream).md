---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/variance(_:axes:keepdims:ddof:stream:)"
framework: "mlx-swift/MLX"
---

# variance(_:axes:keepDims:ddof:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute the variance(s) over the given axes

## Declaration

```swift
func variance(_ array: MLXArray, axes: some Collection<Int>, keepDims: Bool = false, ddof: Int = 0, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

### See Also

- [Reduction Functions](./reduction.md)
- [`variance(_:axis:keepDims:ddof:stream:)`](./variance%28_,axis,keepdims,ddof,stream%29.md)
- [`variance(_:keepDims:ddof:stream:)`](./variance%28_,keepdims,ddof,stream%29.md)
- [`variance(axes:keepDims:ddof:stream:)`](./mlxarray/variance%28axes,keepdims,ddof,stream%29.md)

## Parameters

- `array`: Input array
- `axes`: Axes to reduce over
- `keepDims`: If `true` keep the reduces axes as singleton dimensions
- `ddof`: The divisor to compute the variance is `N - ddof`
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
- [func sum(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./sum%28_,axes,keepdims,stream%29.md)
  Sum reduce the array over the given axes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/variance(_:axes:keepdims:ddof:stream:))*