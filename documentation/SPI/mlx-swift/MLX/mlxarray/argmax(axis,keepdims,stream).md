---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/argmax(axis:keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# argMax(axis:keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Indices of the maximum values along the axis.

## Declaration

```swift
func argMax(axis: Int, keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

## Discussion

```swift
let array = MLXArray(4 ..< 16, [4, 3])

// this will produce [3, 3, 3] -- the index in each column for the maximum value
let i = array.argMax(axis=0)
```

### See Also

- [Indexes](../indexes.md)
- [`argMax(keepDims:stream:)`](./argmax%28keepdims,stream%29.md)
- [`argMin(axis:keepDims:stream:)`](./argmin%28axis,keepdims,stream%29.md)
- [`argMax(_:axis:keepDims:stream:)`](../argmax%28_,axis,keepdims,stream%29.md)

## Parameters

- `axis`: Axis to reduce over
- `keepDims`: If `true` keep reduced axis as singleton dimension
- `stream`: Stream or device to evaluate on

## See Also

### Index Producing Functions
- [func argMax(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmax%28keepdims,stream%29.md)
  Indices of the maximum value over the entire array.
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/argmax(axis:keepdims:stream:))*