---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/product(_:axis:keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# product(_:axis:keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

A `product` reduction over the given axis.

## Declaration

```swift
func product(_ array: MLXArray, axis: Int, keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

```swift
let array = MLXArray([5, 8, 4, 9], [2, 2])

// result is [40, 36]
let result = array.product(axis=1)
```

##### See Also

- [Reduction Functions](./reduction.md)
- [`product(_:axes:keepDims:stream:)`](./product%28_,axes,keepdims,stream%29.md)
- [`product(_:keepDims:stream:)`](./product%28_,keepdims,stream%29.md)
- [`product(axes:keepDims:stream:)`](./mlxarray/product%28axes,keepdims,stream%29.md)

## Parameters

- `array`: Input array
- `axis`: Axis to reduce over
- `keepDims`: If `true` keep reduced axis as singleton dimension
- `stream`: Stream or device to evaluate on

## See Also

### Aggregating Reduction
- [func logSumExp(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28_,axes,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the given axes.
- [func max(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28_,axes,keepdims,stream%29.md)
  A `max` reduction over the given axes.
- [func mean(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28_,axes,keepdims,stream%29.md)
  A `mean` reduction over the given axes.
- [func min(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./min%28_,axes,keepdims,stream%29.md)
  A `min` reduction over the given axes.
- [func sum(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./sum%28_,axes,keepdims,stream%29.md)
  Sum reduce the array over the given axes.
- [func variance(MLXArray, axes: some Collection<Int>, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./variance%28_,axes,keepdims,ddof,stream%29.md)
  Compute the variance(s) over the given axes


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/product(_:axis:keepdims:stream:))*