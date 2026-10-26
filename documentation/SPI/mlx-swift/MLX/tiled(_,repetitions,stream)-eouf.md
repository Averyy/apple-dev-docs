---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/tiled(_:repetitions:stream:)-eouf"
framework: "mlx-swift/MLX"
---

# tiled(_:repetitions:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Construct array by repeating given array the number of times given by `repetitions`.

## Declaration

```swift
func tiled(_ array: MLXArray, repetitions: Int, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

Tiled array

##### See Also

- [Shapes](./shapes.md)
- [`tiled(_:repetitions:stream:)`](./tiled%28_,repetitions,stream%29-eouf.md)

## Parameters

- `array`: Input array
- `repetitions`: Number of repetitions for all axes
- `stream`: Stream or device to evaluate on

## See Also

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
- [func tiled(MLXArray, repetitions: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./tiled%28_,repetitions,stream%29-8krce.md)
  Construct array by repeating given array the number of times given by `repetitions`.
- [func transposed(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./transposed%28_,axes,stream%29.md)
  Transpose the dimensions of the array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/tiled(_:repetitions:stream:)-eouf)*