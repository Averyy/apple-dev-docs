---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/transposed(_:stream:)"
framework: "mlx-swift/MLX"
---

# transposed(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Transpose the dimensions of the array.

## Declaration

```swift
func transposed(_ array: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

With no axes specified this will reverse the axes in the array.

##### See Also

- [Shapes](./shapes.md)
- [`transposed(_:axes:stream:)`](./transposed%28_,axes,stream%29.md)
- [`transposed(_:axis:stream:)`](./transposed%28_,axis,stream%29.md)
- [`transposed(axes:stream:)`](./mlxarray/transposed%28axes,stream%29.md)

## See Also

### Shapes
- [func asStrided(MLXArray, (some Collection<Int>)?, strides: (some Collection<Int>)?, offset: Int, stream: StreamOrDevice) -> MLXArray](./asstrided%28_,_,strides,offset,stream%29.md)
  Create a view into the array with the given shape and strides.
- [func broadcast(MLXArray, to: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./broadcast%28_,to,stream%29.md)
  Broadcast an array to the given shape.
- [func concatenated(some Collection<MLXArray>, axis: Int, stream: StreamOrDevice) -> MLXArray](./concatenated%28_,axis,stream%29.md)
  Concatenate the arrays along the given axis.
- [func expandedDimensions(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./expandeddimensions%28_,axes,stream%29.md)
  Add a size one dimension at the given axis.
- [func expandedDimensions(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./expandeddimensions%28_,axis,stream%29.md)
  Add a size one dimension at the given axis.
- [func movedAxis(MLXArray, source: Int, destination: Int, stream: StreamOrDevice) -> MLXArray](./movedaxis%28_,source,destination,stream%29.md)
  Move an axis to a new position.
- [func padded(MLXArray, width: IntOrPair, mode: PadMode, value: MLXArray?, stream: StreamOrDevice) -> MLXArray](./padded%28_,width,mode,value,stream%29.md)
  Pad an array with a constant value.
- [func padded(MLXArray, widths: some Collection<IntOrPair>, mode: PadMode, value: MLXArray?, stream: StreamOrDevice) -> MLXArray](./padded%28_,widths,mode,value,stream%29.md)
  Pad an array with a constant value.
- [func reshaped(MLXArray, some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./reshaped%28_,_,stream%29-9w4n3.md)
  Reshape an array while preserving the size.
- [func reshaped(MLXArray, Int..., stream: StreamOrDevice) -> MLXArray](./reshaped%28_,_,stream%29-96lgr.md)
  Reshape an array while preserving the size.
- [func split(MLXArray, indices: some Collection<Int>, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28_,indices,axis,stream%29.md)
  Split an array along a given axis.
- [func split(MLXArray, parts: Int, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28_,parts,axis,stream%29.md)
  Split an array into equal size pieces along a given axis.
- [func split(MLXArray, axis: Int, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./split%28_,axis,stream%29.md)
  Split an array into 2 equal size pieces along a given axis.
- [func squeezed(MLXArray, stream: StreamOrDevice) -> MLXArray](./squeezed%28_,stream%29.md)
  Remove all length one axes from an array.
- [func squeezed(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./squeezed%28_,axis,stream%29.md)
  Remove length one axes from an array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/transposed(_:stream:))*