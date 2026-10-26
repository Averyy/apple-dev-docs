---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/all(keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# all(keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

An `and` reduction over the given axes.

## Declaration

```swift
func all(keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

##### See Also

- [Reduction Functions](../reduction.md)
- [`all(axes:keepDims:stream:)`](./all%28axes,keepdims,stream%29.md)
- [`all(axis:keepDims:stream:)`](./all%28axis,keepdims,stream%29.md)
- [`all(_:axes:keepDims:stream:)`](../all%28_,axes,keepdims,stream%29.md)

## Parameters

- `keepDims`: If `true` keep reduced axis as singleton dimension
- `stream`: Stream or device to evaluate on

## See Also

### MLXArray Logical Reduction Functions
- [func all(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28axis,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func all(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func any(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func any(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28axis,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func any(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28axes,keepdims,stream%29.md)
  An `or` reduction over the given axes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/all(keepdims:stream:))*