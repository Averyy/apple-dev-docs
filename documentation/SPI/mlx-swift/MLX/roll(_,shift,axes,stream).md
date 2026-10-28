---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/roll(_:shift:axes:stream:)"
framework: "mlx-swift/MLX"
---

# roll(_:shift:axes:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Roll array elements along a given axis.

## Declaration

```swift
func roll(_ a: MLXArray, shift: Int, axes: (some Collection<Int>)? = [Int]?.none, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

Elements that are rolled beyond the end of the array are introduced at the beggining and vice-versa.

### See Also

- [Shapes](./shapes.md)

## Parameters

- `a`: Input array
- `shift`: The number of places by which elements are shifted. If positive the array is rolled to the right, if negative it is rolled to the left.
- `axes`: The axes along which to roll the elements, or all if omitted
- `stream`: Stream or device to evaluate on

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
- [func atLeast1D(MLXArray, stream: StreamOrDevice) -> MLXArray](./atleast1d%28_,stream%29.md)
  Convert array to have at least 1 dimension.
- [func atLeast2D(MLXArray, stream: StreamOrDevice) -> MLXArray](./atleast2d%28_,stream%29.md)
  Convert array to have at least 2 dimensions.
- [func atLeast3D(MLXArray, stream: StreamOrDevice) -> MLXArray](./atleast3d%28_,stream%29.md)
  Convert array to have at least 3 dimensions.
- [func flattened(MLXArray, start: Int, end: Int, stream: StreamOrDevice) -> MLXArray](./flattened%28_,start,end,stream%29.md)
  Flatten an array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/roll(_:shift:axes:stream:))*