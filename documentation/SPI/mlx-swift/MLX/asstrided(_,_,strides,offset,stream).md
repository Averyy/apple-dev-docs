---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/asstrided(_:_:strides:offset:stream:)"
framework: "mlx-swift/MLX"
---

# asStrided(_:_:strides:offset:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Create a view into the array with the given shape and strides.

## Declaration

```swift
func asStrided(_ array: MLXArray, _ shape: (some Collection<Int>)? = [Int]?.none, strides: (some Collection<Int>)? = [Int]?.none, offset: Int = 0, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

#### Return Value

The output array which is the strided view of the input

#### Discussion

The resulting array will always be as if the provided array was row contiguous regardless of the provided arrays storage order and current strides.

> **Note**: This function should be used with caution as it changes the shape and strides of the array directly. This can lead to the resulting array pointing to invalid memory locations which can result into crashes.

Here are two examples of use:

```swift
// strides in the reverse order is a transpose
let a = MLXArray(0 ..< 12, [4, 3])

let transposed = asStrided(a, [3, 4], strides: [1, 3])
```

and:

```swift
// negative strides and an offset produce a reversed array
let a = MLXArray(0 ..< 16, [4, 4])

let b = asStrided(a, [4, 4], strides: [-4, -1], offset: 15)
let same = MLXArray((0 ..< 16).reversed(), [4, 4])
```

##### See Also

- [Shapes](./shapes.md)

## Parameters

- `array`: Input array
- `shape`: The shape of the resulting array. If not specified it defaults to `array.shape`
- `strides`: The strides of the resulting array. If not specified it defaults to the reverse exclusive cumulative product of `array.shape`
- `offset`: Skip that many elements from the beginning of the input array
- `stream`: Stream or device to evaluate on

## See Also

### Shapes
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
- [func squeezed(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./squeezed%28_,axes,stream%29.md)
  Remove length one axes from an array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/asstrided(_:_:strides:offset:stream:))*