---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/shapes"
framework: "mlx-swift/MLX"
---

# Shapes

**Framework**: mlx-swift/MLX  
**Role**: API Collection

Shape is a term to describe the number and size of the dimensions of an N dimension (ND) array.

## Overview

[`MLXArray`](./mlxarray.md) is an N dimensional array.  The number of dimensions is described by [`ndim`](./mlxarray/ndim.md) and the size of each dimension can be examined with [`dim(_:)`](./mlxarray/dim%28_%29.md) or [`shape`](./mlxarray/shape.md).

Some of these functions can manipulate the shape without changing the contents while others will moves rows and columns as they modify the shape.

## Topics

### Reading Shapes
- [var shape: [Int]](./mlxarray/shape.md)
  Dimensions of the array.
- [var shape2: (Int, Int)](./mlxarray/shape2.md)
  Dimensions of the 2d array as a tuple.
- [var shape3: (Int, Int, Int)](./mlxarray/shape3.md)
  Dimensions of the 3d array as a tuple.
- [var shape4: (Int, Int, Int, Int)](./mlxarray/shape4.md)
  Dimensions of the 4d array as a tuple.
- [func dim(Int) -> Int](./mlxarray/dim%28_%29.md)
  Read a dimension of the array.
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
- [func reshaped(MLXArray, some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./reshaped%28_,_,stream%29-9w4n3.md)
  Reshape an array while preserving the size.
- [func squeezed(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./squeezed%28_,axes,stream%29.md)
  Remove length one axes from an array.
- [func roll(MLXArray, shift: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./roll%28_,shift,axis,stream%29.md)
  Roll array elements along a given axis.
- [func roll(MLXArray, shift: Int, axes: (some Collection<Int>)?, stream: StreamOrDevice) -> MLXArray](./roll%28_,shift,axes,stream%29.md)
  Roll array elements along a given axis.
### MLXArray Shape Methods (Change Size)
- [func movedAxis(source: Int, destination: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/movedaxis%28source,destination,stream%29.md)
  Move an axis to a new position.
- [func split(parts: Int, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./mlxarray/split%28parts,axis,stream%29.md)
  Split an array into equal size pieces along a given axis.
- [func split(indices: some Collection<Int>, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./mlxarray/split%28indices,axis,stream%29.md)
  Split an array along a given axis.
- [func split(axis: Int, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./mlxarray/split%28axis,stream%29.md)
  Split an array into 2 pieces along an axis and returns a tuple – convenient for destructuring.
- [func swappedAxes(Int, Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/swappedaxes%28_,_,stream%29.md)
  Swap two axes of an array.
- [func transposed(stream: StreamOrDevice) -> MLXArray](./mlxarray/transposed%28stream%29.md)
  Transpose the dimensions of the array.
- [func transposed(axis: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/transposed%28axis,stream%29.md)
  Transpose the dimensions of the array.
- [func transposed(axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./mlxarray/transposed%28axes,stream%29.md)
  Transpose the dimensions of the array.
- [func transposed(Int..., stream: StreamOrDevice) -> MLXArray](./mlxarray/transposed%28_,stream%29.md)
  Transpose the dimensions of the array.
- [var T: MLXArray](./mlxarray/t.md)
  Transpose the dimensions of the array.
### Free Functions To Manipulate Shapes
- [func asStrided(MLXArray, (some Collection<Int>)?, strides: (some Collection<Int>)?, offset: Int, stream: StreamOrDevice) -> MLXArray](./asstrided%28_,_,strides,offset,stream%29.md)
  Create a view into the array with the given shape and strides.
- [func broadcast(MLXArray, to: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./broadcast%28_,to,stream%29.md)
  Broadcast an array to the given shape.
- [func concatenated(some Collection<MLXArray>, axis: Int, stream: StreamOrDevice) -> MLXArray](./concatenated%28_,axis,stream%29.md)
  Concatenate the arrays along the given axis.
- [func expandedDimensions(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./expandeddimensions%28_,axes,stream%29.md)
  Add a size one dimension at the given axis.
- [func movedAxis(MLXArray, source: Int, destination: Int, stream: StreamOrDevice) -> MLXArray](./movedaxis%28_,source,destination,stream%29.md)
  Move an axis to a new position.
- [func padded(MLXArray, width: IntOrPair, mode: PadMode, value: MLXArray?, stream: StreamOrDevice) -> MLXArray](./padded%28_,width,mode,value,stream%29.md)
  Pad an array with a constant value.
- [func padded(MLXArray, widths: some Collection<IntOrPair>, mode: PadMode, value: MLXArray?, stream: StreamOrDevice) -> MLXArray](./padded%28_,widths,mode,value,stream%29.md)
  Pad an array with a constant value.
- [func split(MLXArray, indices: some Collection<Int>, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28_,indices,axis,stream%29.md)
  Split an array along a given axis.
- [func split(MLXArray, parts: Int, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28_,parts,axis,stream%29.md)
  Split an array into equal size pieces along a given axis.
- [func split(MLXArray, axis: Int, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./split%28_,axis,stream%29.md)
  Split an array into 2 equal size pieces along a given axis.
- [func stacked(some Collection<MLXArray>, axis: Int, stream: StreamOrDevice) -> MLXArray](./stacked%28_,axis,stream%29.md)
  Stacks the arrays along a new axis.
- [func swappedAxes(MLXArray, Int, Int, stream: StreamOrDevice) -> MLXArray](./swappedaxes%28_,_,_,stream%29.md)
  Swap two axes of an array.
- [func tiled(MLXArray, repetitions: Int, stream: StreamOrDevice) -> MLXArray](./tiled%28_,repetitions,stream%29-eouf.md)
  Construct array by repeating given array the number of times given by `repetitions`.
- [func tiled(MLXArray, repetitions: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./tiled%28_,repetitions,stream%29-8krce.md)
  Construct array by repeating given array the number of times given by `repetitions`.
- [func transposed(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./transposed%28_,axes,stream%29.md)
  Transpose the dimensions of the array.

## See Also

### Shapes
- [Reduction Functions](./reduction.md)
  Reduction or aggregation functions.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/shapes)*