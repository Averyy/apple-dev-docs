---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/search(sorted:values:side:stream:)"
framework: "mlx-swift/MLX"
---

# search(sorted:values:side:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Find the indices that keep `sorted` sorted when inserting `values`.

## Declaration

```swift
func search(sorted: MLXArray, values: MLXArray, side: SearchSortedSide = .left, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

`.uint32` array in the same shape as `values`

## Parameters

- `sorted`: 1-D array in ascending order.
- `values`: Values to insert in any shape
- `side`: If `.left` the first suitable index is returned, otherwise last
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/search(sorted:values:side:stream:))*