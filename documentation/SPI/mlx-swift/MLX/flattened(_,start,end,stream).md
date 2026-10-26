---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/flattened(_:start:end:stream:)"
framework: "mlx-swift/MLX"
---

# flattened(_:start:end:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Flatten an array.

## Declaration

```swift
func flattened(_ array: MLXArray, start: Int = 0, end: Int = -1, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

#### Discussion

The axes flattened will be between `start` and `end`, inclusive. Negative axes are supported. After converting negative axis to positive, axes outside the valid range will be clamped to a valid value, `start` to `0` and `end` to `ndim - 1`.

For example:

```swift
let a = MLXArray(0 ..< (8 * 4 * 3), [8, 4, 3])

// f1 is shape [8 * 4 * 3] = [96]
let f1 = a.flattened()

// f2 is [8, 4 * 3] = [8, 12]
let f2 = a.flattened(start: 1)
```

##### See Also

- [Shapes](./shapes.md)
- [`flattened(start:end:stream:)`](./mlxarray/flattened%28start,end,stream%29.md)

## Parameters

- `array`: Input array
- `start`: First dimension to flatten
- `end`: Last dimension to flatten
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
- [func reshaped(MLXArray, some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./reshaped%28_,_,stream%29-9w4n3.md)
  Reshape an array while preserving the size.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/flattened(_:start:end:stream:))*