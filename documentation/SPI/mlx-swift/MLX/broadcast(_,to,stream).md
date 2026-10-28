---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/broadcast(_:to:stream:)"
framework: "mlx-swift/MLX"
---

# broadcast(_:to:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Broadcast an array to the given shape.

## Declaration

```swift
func broadcast(_ array: MLXArray, to shape: some Collection<Int>, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

### See Also

- [Numpy Style Broadcasting](./broadcasting.md)

## Parameters

- `array`: Input array
- `shape`: Shape to broadcast to
- `stream`: Stream or device to evaluate on

## See Also

### Shapes
- [func asStrided(MLXArray, (some Collection<Int>)?, strides: (some Collection<Int>)?, offset: Int, stream: StreamOrDevice) -> MLXArray](./asstrided%28_,_,strides,offset,stream%29.md)
  Create a view into the array with the given shape and strides.
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
- [func squeezed(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./squeezed%28_,axes,stream%29.md)
  Remove length one axes from an array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/broadcast(_:to:stream:))*