---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/transposed(_:stream:)"
framework: "mlx-swift/MLX"
---

# transposed(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Transpose the dimensions of the array.

## Declaration

```swift
func transposed(_ axes: Int..., stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

##### See Also

- [Shapes](../shapes.md)
- [`transposed(axes:stream:)`](./transposed%28axes,stream%29.md)
- [`transposed(axis:stream:)`](./transposed%28axis,stream%29.md)
- [`transposed(stream:)`](./transposed%28stream%29.md)
- [`transposed(_:axes:stream:)`](../transposed%28_,axes,stream%29.md)

## Parameters

- `axes`: Specifies the source axis for each axis in the new array
- `stream`: Stream or device to evaluate on

## See Also

### MLXArray Shape Methods (Change Size)
- [func movedAxis(source: Int, destination: Int, stream: StreamOrDevice) -> MLXArray](./movedaxis%28source,destination,stream%29.md)
  Move an axis to a new position.
- [func split(parts: Int, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28parts,axis,stream%29.md)
  Split an array into equal size pieces along a given axis.
- [func split(indices: some Collection<Int>, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28indices,axis,stream%29.md)
  Split an array along a given axis.
- [func split(axis: Int, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./split%28axis,stream%29.md)
  Split an array into 2 pieces along an axis and returns a tuple – convenient for destructuring.
- [func swappedAxes(Int, Int, stream: StreamOrDevice) -> MLXArray](./swappedaxes%28_,_,stream%29.md)
  Swap two axes of an array.
- [func transposed(stream: StreamOrDevice) -> MLXArray](./transposed%28stream%29.md)
  Transpose the dimensions of the array.
- [func transposed(axis: Int, stream: StreamOrDevice) -> MLXArray](./transposed%28axis,stream%29.md)
  Transpose the dimensions of the array.
- [func transposed(axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./transposed%28axes,stream%29.md)
  Transpose the dimensions of the array.
- [var T: MLXArray](./t.md)
  Transpose the dimensions of the array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/transposed(_:stream:))*