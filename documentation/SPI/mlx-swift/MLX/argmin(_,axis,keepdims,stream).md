---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/argmin(_:axis:keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# argMin(_:axis:keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Indices of the minimum values along the axis.

## Declaration

```swift
func argMin(_ array: MLXArray, axis: Int, keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

#### Discussion

```swift
let array = MLXArray(4 ..< 16, [4, 3])

// this will produce [0, 0, 0] -- the index in each column for the minimum value
let i = array.argMin(axis=0)
```

##### See Also

- [Indexes](./indexes.md)
- [`argMin(_:keepDims:stream:)`](./argmin%28_,keepdims,stream%29.md)
- [`argMax(_:axis:keepDims:stream:)`](./argmax%28_,axis,keepdims,stream%29.md)
- [`argMin(axis:keepDims:stream:)`](./mlxarray/argmin%28axis,keepdims,stream%29.md)

## Parameters

- `array`: Input array
- `axis`: Axis to reduce over
- `keepDims`: If `true` keep reduced axis as singleton dimension
- `stream`: Stream or device to evaluate on

## See Also

### Indexes
- [func argMax(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmax%28_,axis,keepdims,stream%29.md)
  Indices of the maximum values along the axis.
- [func argMax(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmax%28_,keepdims,stream%29.md)
  Indices of the maximum value over the entire array.
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
- [func top(MLXArray, k: Int, stream: StreamOrDevice) -> MLXArray](./top%28_,k,stream%29.md)
  Returns the `k` largest elements from the flattened input along a given axis.
- [func top(MLXArray, k: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./top%28_,k,axis,stream%29.md)
  Returns the `k` largest elements from the input along a given axis.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/argmin(_:axis:keepdims:stream:))*