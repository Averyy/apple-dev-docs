---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/indexes"
framework: "mlx-swift/MLX"
---

# Indexes

**Framework**: mlx-swift/MLX  
**Role**: API Collection

Functions to produce and consume array indexes.

#### Overview

MLX has a number of functions (typically named `argX()`) that can produce array indices and a few functions that can consume them.

```swift
// array with values in random order
let array = MLXRandom.randInt(0 ..< 100, [10])

let sortIndexes = argSort(array, axis: -1)

// the array in sorted order
let sorted = array[sortIndexes]
```

## Topics

### Index Producing Functions
- [func argMax(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/argmax%28keepdims,stream%29.md)
  Indices of the maximum value over the entire array.
- [func argMax(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/argmax%28axis,keepdims,stream%29.md)
  Indices of the maximum values along the axis.
- [func argMin(keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/argmin%28keepdims,stream%29.md)
  Indices of the minimum value over the entire array.
- [func argMin(axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/argmin%28axis,keepdims,stream%29.md)
  Indices of the minimum values along the axis.
- [func argMax(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmax%28_,keepdims,stream%29.md)
  Indices of the maximum value over the entire array.
- [func argMax(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmax%28_,axis,keepdims,stream%29.md)
  Indices of the maximum values along the axis.
- [func argMin(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmin%28_,keepdims,stream%29.md)
  Indices of the minimum value over the entire array.
- [func argMin(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmin%28_,axis,keepdims,stream%29.md)
  Indices of the minimum values along the axis.
- [func argPartition(MLXArray, kth: Int, stream: StreamOrDevice) -> MLXArray](./argpartition%28_,kth,stream%29.md)
  Returns the indices that partition the flattened array.
- [func argPartition(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./argpartition%28_,kth,axis,stream%29.md)
  Returns the indices that partition the array.
- [func argSort(MLXArray, stream: StreamOrDevice) -> MLXArray](./argsort%28_,stream%29.md)
  Returns the indices that sort the array.
- [func argSort(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./argsort%28_,axis,stream%29.md)
  Returns the indices that sort the array.
### Index Consuming Functions
- [class MLXArray](./mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [func take(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/take%28_,axis,stream%29.md)
  Take elements along an axis.
- [func takeAlong(MLXArray, MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./takealong%28_,_,axis,stream%29.md)
  Take values along an axis at the specified indices.

## See Also

### Indexing
- [Indexing](./indexing.md)
  Array subscripts.
- [Sorting](./sorting.md)
  Sorting and partitioning values and indices.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/indexes)*