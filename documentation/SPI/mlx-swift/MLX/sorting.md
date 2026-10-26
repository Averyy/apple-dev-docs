---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/sorting"
framework: "mlx-swift/MLX"
---

# Sorting

**Framework**: mlx-swift/MLX  
**Role**: API Collection

Sorting and partitioning values and indices.

#### Overview

MLX has a number of methods that produce an array of indexes, including for sorting and partitioning:

```swift
// array with values in random order
let array = MLXRandom.randInt(0 ..< 100, [10])

let sortIndexes = argSort(array, axis: -1)

// the array in sorted order
let sorted = array[sortIndexes]
```

There are other methods that produce a new sorted or partitioned array:

```swift
// array with values in random order
let array = MLXRandom.randInt(0 ..< 100, [10])

// the array in sorted order
let sorted = sort(array)
```

See related items in [Indexes](./indexes.md).

## Topics

### Index Producing Functions
- [func argSort(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./argsort%28_,axis,stream%29.md)
  Returns the indices that sort the array.
- [func argPartition(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./argpartition%28_,kth,axis,stream%29.md)
  Returns the indices that partition the array.
### Sorting Functions
- [func sorted(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./sorted%28_,axis,stream%29.md)
  Returns a sorted copy of the array.
- [func partitioned(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./partitioned%28_,kth,axis,stream%29.md)
  Returns a partitioned copy of the array such that the smaller `kth` elements are first.

## See Also

### Indexing
- [Indexes](./indexes.md)
  Functions to produce and consume array indexes.
- [Indexing](./indexing.md)
  Array subscripts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/sorting)*