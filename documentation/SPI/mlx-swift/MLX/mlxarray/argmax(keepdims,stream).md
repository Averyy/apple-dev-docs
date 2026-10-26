---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/argmax(keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# argMax(keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Indices of the maximum value over the entire array.

## Declaration

```swift
func argMax(keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

```swift
let array = MLXArray(4 ..< 16, [4, 3])

// this will produce [11] -- the index in the flattened array of the largest value
let i = array.argMax()
```

##### See Also

- [Indexes](../indexes.md)
- [`argMax(axis:keepDims:stream:)`](./argmax%28axis,keepdims,stream%29.md)
- [`argMin(axis:keepDims:stream:)`](./argmin%28axis,keepdims,stream%29.md)
- [`argMax(_:axis:keepDims:stream:)`](../argmax%28_,axis,keepdims,stream%29.md)

## Parameters

- `keepDims`: If `true` keep reduced axis as singleton dimension
- `stream`: Stream or device to evaluate on

## See Also

### Index Producing Functions
- [func argMax(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmax%28axis,keepdims,stream%29.md)
  Indices of the maximum values along the axis.
- [func argMin(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmin%28keepdims,stream%29.md)
  Indices of the minimum value over the entire array.
- [func argMin(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmin%28axis,keepdims,stream%29.md)
  Indices of the minimum values along the axis.
- [func argMax(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](../argmax%28_,keepdims,stream%29.md)
  Indices of the maximum value over the entire array.
- [func argMax(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](../argmax%28_,axis,keepdims,stream%29.md)
  Indices of the maximum values along the axis.
- [func argMin(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](../argmin%28_,keepdims,stream%29.md)
  Indices of the minimum value over the entire array.
- [func argMin(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](../argmin%28_,axis,keepdims,stream%29.md)
  Indices of the minimum values along the axis.
- [func argPartition(MLXArray, kth: Int, stream: StreamOrDevice) -> MLXArray](../argpartition%28_,kth,stream%29.md)
  Returns the indices that partition the flattened array.
- [func argPartition(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](../argpartition%28_,kth,axis,stream%29.md)
  Returns the indices that partition the array.
- [func argSort(MLXArray, stream: StreamOrDevice) -> MLXArray](../argsort%28_,stream%29.md)
  Returns the indices that sort the array.
- [func argSort(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](../argsort%28_,axis,stream%29.md)
  Returns the indices that sort the array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/argmax(keepdims:stream:))*