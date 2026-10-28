---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/sorted(_:axis:stream:)"
framework: "mlx-swift/MLX"
---

# sorted(_:axis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Returns a sorted copy of the array.

## Declaration

```swift
func sorted(_ array: MLXArray, axis: Int, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

### See Also

- [Sorting](./sorting.md)
- [`sorted(_:stream:)`](./sorted%28_,stream%29.md)
- [`argSort(_:axis:stream:)`](./argsort%28_,axis,stream%29.md)

## Parameters

- `array`: Input array
- `axis`: Axis to sort over
- `stream`: Stream or device to evaluate on

## See Also

### Sorting
- [func argSort(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./argsort%28_,axis,stream%29.md)
  Returns the indices that sort the array.
- [func argPartition(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./argpartition%28_,kth,axis,stream%29.md)
  Returns the indices that partition the array.
- [func sorted(MLXArray, stream: StreamOrDevice) -> MLXArray](./sorted%28_,stream%29.md)
  Returns a sorted copy of the flattened array.
- [func partitioned(MLXArray, kth: Int, stream: StreamOrDevice) -> MLXArray](./partitioned%28_,kth,stream%29.md)
  Returns a partitioned copy of the flattened array such that the smaller `kth` elements are first.
- [func partitioned(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./partitioned%28_,kth,axis,stream%29.md)
  Returns a partitioned copy of the array such that the smaller `kth` elements are first.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/sorted(_:axis:stream:))*