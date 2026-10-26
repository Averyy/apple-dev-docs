---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/putalong(_:_:values:stream:)"
framework: "mlx-swift/MLX"
---

# putAlong(_:_:values:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Put values along an axis at the specified indices in a flattened array.

## Declaration

```swift
func putAlong(_ array: MLXArray, _ indices: MLXArray, values: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

##### See Also

- [Indexes](./indexes.md)
- ``takeAlong(*:*:axis:stream:)

## Parameters

- `array`: Destination array
- `indices`: Indices array. These should be broadcastable with the flattened input array
- `values`: Values array. These should be broadcastable with the flattened input array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/putalong(_:_:values:stream:))*