---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/takealong(_:_:axis:stream:)"
framework: "mlx-swift/MLX"
---

# takeAlong(_:_:axis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Take values along an axis at the specified indices.

## Declaration

```swift
func takeAlong(_ array: MLXArray, _ indices: MLXArray, axis: Int, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

##### See Also

- [Indexes](./indexes.md)
- [`takeAlong(_:_:stream:)`](./takealong%28_,_,stream%29.md)

## Parameters

- `array`: The left hand side array
- `indices`: Should be broadcastable to `array` excluding the `axis` dimension
- `axis`: Axis in the input to take the values from
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/takealong(_:_:axis:stream:))*