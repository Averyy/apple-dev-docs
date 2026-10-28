---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/atleast1d(_:stream:)"
framework: "mlx-swift/MLX"
---

# atLeast1D(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Convert array to have at least 1 dimension.

## Declaration

```swift
func atLeast1D(_ array: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

### See Also

- [Shapes](./shapes.md)

## See Also

### MLXArray Shape Methods (Same Size)
- [func expandedDimensions(axis: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/expandeddimensions%28axis,stream%29.md)
  Add a size one dimension at the given axis.
- [func expandedDimensions(axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./mlxarray/expandeddimensions%28axes,stream%29.md)
  Add a size one dimension at the given axis.
- [func flattened(start: Int, end: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/flattened%28start,end,stream%29.md)
  Flatten an array.
- [func reshaped(some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./mlxarray/reshaped%28_,stream%29-2mzhh.md)
  Reshape an array while preserving the size.
- [func reshaped(Int..., stream: StreamOrDevice) -> MLXArray](./mlxarray/reshaped%28_,stream%29-67a89.md)
  Reshape an array while preserving the size.
- [func squeezed(stream: StreamOrDevice) -> MLXArray](./mlxarray/squeezed%28stream%29.md)
  Remove all length one axes from an array.
- [func squeezed(axis: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/squeezed%28axis,stream%29.md)
  Remove length one axes from an array.
- [func squeezed(axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./mlxarray/squeezed%28axes,stream%29.md)
  Remove length one axes from an array.
- [func expandedDimensions(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./expandeddimensions%28_,axis,stream%29.md)
  Add a size one dimension at the given axis.
- [func expandedDimensions(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./expandeddimensions%28_,axes,stream%29.md)
  Add a size one dimension at the given axis.
- [func asStrided(MLXArray, (some Collection<Int>)?, strides: (some Collection<Int>)?, offset: Int, stream: StreamOrDevice) -> MLXArray](./asstrided%28_,_,strides,offset,stream%29.md)
  Create a view into the array with the given shape and strides.
- [func atLeast2D(MLXArray, stream: StreamOrDevice) -> MLXArray](./atleast2d%28_,stream%29.md)
  Convert array to have at least 2 dimensions.
- [func atLeast3D(MLXArray, stream: StreamOrDevice) -> MLXArray](./atleast3d%28_,stream%29.md)
  Convert array to have at least 3 dimensions.
- [func flattened(MLXArray, start: Int, end: Int, stream: StreamOrDevice) -> MLXArray](./flattened%28_,start,end,stream%29.md)
  Flatten an array.
- [func reshaped(MLXArray, some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./reshaped%28_,_,stream%29-9w4n3.md)
  Reshape an array while preserving the size.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/atleast1d(_:stream:))*