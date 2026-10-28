---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/take(_:axis:stream:)"
framework: "mlx-swift/MLX"
---

# take(_:axis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Take elements along an axis.

## Declaration

```swift
func take(_ indices: MLXArray, axis: Int, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The elements are taken from `indices` along the specified axis.

```swift
let array = MLXArray(0 ..< 12, [3, 4])

/// produces a [3, 2] result with the index 0 and 2 columns from the array
let col = array.take([0, 2], axis: 1)
```

### See Also

- [`take(_:stream:)`](./take%28_,stream%29.md)
- [`take(_:_:axis:stream:)`](../take%28_,_,axis,stream%29.md)

## Parameters

- `indices`: Array of indices
- `axis`: Axis to take from
- `stream`: Stream or device to evaluate on

## See Also

### Index Consuming Functions
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [func takeAlong(MLXArray, MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](../takealong%28_,_,axis,stream%29.md)
  Take values along an axis at the specified indices.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/take(_:axis:stream:))*