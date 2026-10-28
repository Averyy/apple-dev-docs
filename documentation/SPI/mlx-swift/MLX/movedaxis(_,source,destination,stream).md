---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/movedaxis(_:source:destination:stream:)"
framework: "mlx-swift/MLX"
---

# movedAxis(_:source:destination:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Move an axis to a new position.

## Declaration

```swift
func movedAxis(_ array: MLXArray, source: Int, destination: Int, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

## Discussion

```swift
let array = MLXArray(0 ..< 16, [2, 2, 2, 2])
print(array)
// array([[[[0, 1],
//          [2, 3]],
//         [[4, 5],
//          [6, 7]]],
//        [[[8, 9],
//          [10, 11]],
//         [[12, 13],
//          [14, 15]]]], dtype=int64)

let r = array.movedAxis(source: 0, destination: 3)
print(r)
// array([[[[0, 8],
//          [1, 9]],
//         [[2, 10],
//          [3, 11]]],
//        [[[4, 12],
//          [5, 13]],
//         [[6, 14],
//          [7, 15]]]], dtype=int64)
```

### See Also

- [Shapes](./shapes.md)
- [`swappedAxes(_:_:_:stream:)`](./swappedaxes%28_,_,_,stream%29.md)
- [`movedAxis(source:destination:stream:)`](./mlxarray/movedaxis%28source,destination,stream%29.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/movedaxis(_:source:destination:stream:))*