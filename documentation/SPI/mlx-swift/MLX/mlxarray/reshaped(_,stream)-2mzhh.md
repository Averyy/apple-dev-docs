---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/reshaped(_:stream:)-2mzhh"
framework: "mlx-swift/MLX"
---

# reshaped(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Reshape an array while preserving the size.

## Declaration

```swift
func reshaped(_ newShape: some Collection<Int>, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

## Discussion

```swift
let array = MLXArray(0 ..< 12)

let r = array.reshaped([4, 3])
```

### See Also

- [Shapes](../shapes.md)
- [`reshaped(_:stream:)`](./reshaped%28_,stream%29-2mzhh.md)
- [`reshaped(_:_:stream:)`](../reshaped%28_,_,stream%29-9w4n3.md)

## Parameters

- `newShape`: The new shape
- `stream`: Stream or device to evaluate on

## See Also

### MLXArray Shape Methods (Same Size)
- [func expandedDimensions(axis: Int, stream: StreamOrDevice) -> MLXArray](./expandeddimensions%28axis,stream%29.md)
  Add a size one dimension at the given axis.
- [func expandedDimensions(axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./expandeddimensions%28axes,stream%29.md)
  Add a size one dimension at the given axis.
- [func flattened(start: Int, end: Int, stream: StreamOrDevice) -> MLXArray](./flattened%28start,end,stream%29.md)
  Flatten an array.
- [func reshaped(Int..., stream: StreamOrDevice) -> MLXArray](./reshaped%28_,stream%29-67a89.md)
  Reshape an array while preserving the size.
- [func squeezed(stream: StreamOrDevice) -> MLXArray](./squeezed%28stream%29.md)
  Remove all length one axes from an array.
- [func squeezed(axis: Int, stream: StreamOrDevice) -> MLXArray](./squeezed%28axis,stream%29.md)
  Remove length one axes from an array.
- [func squeezed(axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./squeezed%28axes,stream%29.md)
  Remove length one axes from an array.
- [func expandedDimensions(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](../expandeddimensions%28_,axis,stream%29.md)
  Add a size one dimension at the given axis.
- [func expandedDimensions(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](../expandeddimensions%28_,axes,stream%29.md)
  Add a size one dimension at the given axis.
- [func asStrided(MLXArray, (some Collection<Int>)?, strides: (some Collection<Int>)?, offset: Int, stream: StreamOrDevice) -> MLXArray](../asstrided%28_,_,strides,offset,stream%29.md)
  Create a view into the array with the given shape and strides.
- [func atLeast1D(MLXArray, stream: StreamOrDevice) -> MLXArray](../atleast1d%28_,stream%29.md)
  Convert array to have at least 1 dimension.
- [func atLeast2D(MLXArray, stream: StreamOrDevice) -> MLXArray](../atleast2d%28_,stream%29.md)
  Convert array to have at least 2 dimensions.
- [func atLeast3D(MLXArray, stream: StreamOrDevice) -> MLXArray](../atleast3d%28_,stream%29.md)
  Convert array to have at least 3 dimensions.
- [func flattened(MLXArray, start: Int, end: Int, stream: StreamOrDevice) -> MLXArray](../flattened%28_,start,end,stream%29.md)
  Flatten an array.
- [func reshaped(MLXArray, some Collection<Int>, stream: StreamOrDevice) -> MLXArray](../reshaped%28_,_,stream%29-9w4n3.md)
  Reshape an array while preserving the size.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/reshaped(_:stream:)-2mzhh)*