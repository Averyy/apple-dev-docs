---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/split(parts:axis:stream:)"
framework: "mlx-swift/MLX"
---

# split(parts:axis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Split an array into equal size pieces along a given axis.

## Declaration

```swift
func split(parts: Int, axis: Int = 0, stream: StreamOrDevice = .default) -> [MLXArray]
```

## Mentions

- [Converting From Python](../converting-python.md)

## Discussion

Splits the array into equal size pieces along a given axis and returns an array of `MLXArray`:

```swift
let array = MLXArray(0 ..< 12, (4, 3))

let halves = array.split(2)
print(halves)

[array([[0, 1, 2],
        [3, 4, 5]], dtype=int64),
 array([[6, 7, 8],
        [9, 10, 11]], dtype=int64)]
```

### See Also

- [Shapes](../shapes.md)
- [`split(axis:stream:)`](./split%28axis,stream%29.md)
- [`split(indices:axis:stream:)`](./split%28indices,axis,stream%29.md)
- [`split(_:parts:axis:stream:)`](../split%28_,parts,axis,stream%29.md)

## Parameters

- `parts`: Array is split into that many sections of equal size. It is a fatal error if this is not possible
- `axis`: Axis to split along
- `stream`: Stream or device to evaluate on

## See Also

### MLXArray Shape Methods (Change Size)
- [func movedAxis(source: Int, destination: Int, stream: StreamOrDevice) -> MLXArray](./movedaxis%28source,destination,stream%29.md)
  Move an axis to a new position.
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
- [func transposed(Int..., stream: StreamOrDevice) -> MLXArray](./transposed%28_,stream%29.md)
  Transpose the dimensions of the array.
- [var T: MLXArray](./t.md)
  Transpose the dimensions of the array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/split(parts:axis:stream:))*