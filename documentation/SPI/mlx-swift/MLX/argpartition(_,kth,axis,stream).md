---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/argpartition(_:kth:axis:stream:)"
framework: "mlx-swift/MLX"
---

# argPartition(_:kth:axis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Returns the indices that partition the array.

## Declaration

```swift
func argPartition(_ array: MLXArray, kth: Int, axis: Int, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

## Discussion

The ordering of the elements within a partition in given by the indices is undefined.

For example:

```swift
// array with values in random order
let array = MLXRandom.randInt(0 ..< 100, [10])

let partitionIndexes = argPartition(array, kth: 3)

// the partitioned array.  the pivot is at partitioned[3] and all values
// with lower indexes will be less than (in undefined order)
let partitioned = array[sortIndexes]
```

### See Also

- [Indexes](./indexes.md)
- [`argPartition(_:kth:stream:)`](./argpartition%28_,kth,stream%29.md)
- [`partitioned(_:kth:axis:stream:)`](./partitioned%28_,kth,axis,stream%29.md)

## Parameters

- `array`: Input array
- `kth`: Element index at the `kth` position in the output will give the sorted position.  All indices before the`kth` position will be of elements less than or equal to the element at the `kth` index and all indices after will be elemenents greater than or equal to the element at the `kth` position.
- `axis`: Axis to partition over
- `stream`: Stream or device to evaluate on

## See Also

### Indexes
- [func argMax(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmax%28_,axis,keepdims,stream%29.md)
  Indices of the maximum values along the axis.
- [func argMax(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmax%28_,keepdims,stream%29.md)
  Indices of the maximum value over the entire array.
- [func argMin(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmin%28_,axis,keepdims,stream%29.md)
  Indices of the minimum values along the axis.
- [func argMin(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmin%28_,keepdims,stream%29.md)
  Indices of the minimum value over the entire array.
- [func argPartition(MLXArray, kth: Int, stream: StreamOrDevice) -> MLXArray](./argpartition%28_,kth,stream%29.md)
  Returns the indices that partition the flattened array.
- [func argSort(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./argsort%28_,axis,stream%29.md)
  Returns the indices that sort the array.
- [func argSort(MLXArray, stream: StreamOrDevice) -> MLXArray](./argsort%28_,stream%29.md)
  Returns the indices that sort the array.
- [func takeAlong(MLXArray, MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./takealong%28_,_,axis,stream%29.md)
  Take values along an axis at the specified indices.
- [func takeAlong(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./takealong%28_,_,stream%29.md)
  Take values along an axis at the specified indices from a flattened array.
- [func take(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./take%28_,_,stream%29.md)
  Take elements from flattened 1-D array.
- [func take(MLXArray, MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./take%28_,_,axis,stream%29.md)
  Take elements along an axis.
- [func top(MLXArray, k: Int, stream: StreamOrDevice) -> MLXArray](./top%28_,k,stream%29.md)
  Returns the `k` largest elements from the flattened input along a given axis.
- [func top(MLXArray, k: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./top%28_,k,axis,stream%29.md)
  Returns the `k` largest elements from the input along a given axis.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/argpartition(_:kth:axis:stream:))*