---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/swappedaxes(_:_:stream:)"
framework: "mlx-swift/MLX"
---

# swappedAxes(_:_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Swap two axes of an array.

## Declaration

```swift
func swappedAxes(_ axis1: Int, _ axis2: Int, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

#### Discussion

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

let r = array.swappedAxes(2, 1)
print(r)
// array([[[[0, 8],
//          [2, 10]],
//         [[4, 12],
//          [6, 14]]],
//        [[[1, 9],
//          [3, 11]],
//         [[5, 13],
//          [7, 15]]]], dtype=int64)
```

##### See Also

- [Shapes](../shapes.md)
- [`swappedAxes(_:_:_:stream:)`](../swappedaxes%28_,_,_,stream%29.md)

## Parameters

- `axis1`: First axis
- `axis2`: Second axis
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/swappedaxes(_:_:stream:))*