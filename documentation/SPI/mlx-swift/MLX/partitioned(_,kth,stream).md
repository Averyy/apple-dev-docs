---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/partitioned(_:kth:stream:)"
framework: "mlx-swift/MLX"
---

# partitioned(_:kth:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Returns a partitioned copy of the flattened array such that the smaller `kth` elements are first.

## Declaration

```swift
func partitioned(_ array: MLXArray, kth: Int, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

The ordering of the elements in partitions is undefined.

##### See Also

- [Sorting](./sorting.md)
- [`partitioned(_:kth:axis:stream:)`](./partitioned%28_,kth,axis,stream%29.md)
- [`argPartition(_:kth:axis:stream:)`](./argpartition%28_,kth,axis,stream%29.md)

## Parameters

- `array`: Input array
- `kth`: Element at the `kth` index will be in its sorted position in the output. All elements before the kth index will be less or equal to the `kth` element and all elements after will be greater or equal to the `kth` element in the output.
- `stream`: Stream or device to evaluate on

## See Also

### Sorting
- [func argSort(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./argsort%28_,axis,stream%29.md)
  Returns the indices that sort the array.
- [func argPartition(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./argpartition%28_,kth,axis,stream%29.md)
  Returns the indices that partition the array.
- [func sorted(MLXArray, stream: StreamOrDevice) -> MLXArray](./sorted%28_,stream%29.md)
  Returns a sorted copy of the flattened array.
- [func sorted(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./sorted%28_,axis,stream%29.md)
  Returns a sorted copy of the array.
- [func partitioned(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./partitioned%28_,kth,axis,stream%29.md)
  Returns a partitioned copy of the array such that the smaller `kth` elements are first.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/partitioned(_:kth:stream:))*