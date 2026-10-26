---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/split(axis:stream:)"
framework: "mlx-swift/MLX"
---

# split(axis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Split an array into 2 pieces along an axis and returns a tuple – convenient for destructuring.

## Declaration

```swift
func split(axis: Int = 0, stream: StreamOrDevice = .default) -> (MLXArray, MLXArray)
```

## Mentions

- [Converting From Python](../converting-python.md)

#### Discussion

Splits the array into 2 pieces along a given axis and returns an tuple of `MLXArray`:

```swift
let array = MLXArray(0 ..< 12, (4, 3))

let (a, b) = array.split()
```

##### See Also

- [Shapes](../shapes.md)
- [`split(parts:axis:stream:)`](./split%28parts,axis,stream%29.md)
- [`split(indices:axis:stream:)`](./split%28indices,axis,stream%29.md)
- [`split(_:parts:axis:stream:)`](../split%28_,parts,axis,stream%29.md)

## Parameters

- `axis`: Axis to split along
- `stream`: Stream or device to evaluate on

## See Also

### MLXArray Shape Methods (Change Size)
- [func movedAxis(source: Int, destination: Int, stream: StreamOrDevice) -> MLXArray](./movedaxis%28source,destination,stream%29.md)
  Move an axis to a new position.
- [func split(parts: Int, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28parts,axis,stream%29.md)
  Split an array into equal size pieces along a given axis.
- [func split(indices: some Collection<Int>, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28indices,axis,stream%29.md)
  Split an array along a given axis.
- [func swappedAxes(Int, Int, stream: StreamOrDevice) -> MLXArray](./swappedaxes%28_,_,stream%29.md)
  Swap two axes of an array.
- [func transposed(stream: StreamOrDevice) -> MLXArray](./transposed%28stream%29.md)
  Transpose the dimensions of the array.
- [func transposed(axis: Int, stream: StreamOrDevice) -> MLXArray](./transposed%28axis,stream%29.md)
  Transpose the dimensions of the array.
- [func transposed(axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./transposed%28axes,stream%29.md)
  Transpose the dimensions of the array.
- [func transposed(Int..., stream: StreamOrDevice) -> MLXArray](./transposed%28_,stream%29.md)
  Transpose the dimensions of the array.
- [var T: MLXArray](./t.md)
  Transpose the dimensions of the array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/split(axis:stream:))*