---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/top(_:k:stream:)"
framework: "mlx-swift/MLX"
---

# top(_:k:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Returns the `k` largest elements from the flattened input along a given axis.

## Declaration

```swift
func top(_ array: MLXArray, k: Int, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

The elements will not necessarily be in sorted order.

##### See Also

- [Sorting](./sorting.md)
- [`top(_:k:axis:stream:)`](./top%28_,k,axis,stream%29.md)

## Parameters

- `array`: Input array
- `k`: How many values
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
- [func argPartition(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./argpartition%28_,kth,axis,stream%29.md)
  Returns the indices that partition the array.
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
- [func top(MLXArray, k: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./top%28_,k,axis,stream%29.md)
  Returns the `k` largest elements from the input along a given axis.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/top(_:k:stream:))*