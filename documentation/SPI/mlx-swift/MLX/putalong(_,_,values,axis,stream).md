---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/putalong(_:_:values:axis:stream:)"
framework: "mlx-swift/MLX"
---

# putAlong(_:_:values:axis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Put values along an axis at the specified indices.

## Declaration

```swift
func putAlong(_ array: MLXArray, _ indices: MLXArray, values: MLXArray, axis: Int, stream: StreamOrDevice = .default) -> MLXArray
```

### See Also

- [Indexes](./indexes.md)
- [`takeAlong(_:_:stream:)`](./takealong%28_,_,stream%29.md)

## Parameters

- `array`: Destination array
- `indices`: Indices array. These should be broadcastable with the input array excluding the `axis` dimension.
- `values`: Values array. These should be broadcastable with the indices.
- `axis`: Axis in the destination to put the values to
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/putalong(_:_:values:axis:stream:))*