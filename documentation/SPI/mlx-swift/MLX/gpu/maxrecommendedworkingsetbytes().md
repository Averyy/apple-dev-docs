---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/maxrecommendedworkingsetbytes()"
framework: "mlx-swift/MLX"
---

# maxRecommendedWorkingSetBytes()

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Returns Metal’s recommended working set size in bytes as an `Int`.

## Declaration

```swift
static func maxRecommendedWorkingSetBytes() -> Int?
```

## Discussion

This value is derived from [`maxRecommendedWorkingSetSize`](./deviceinfo/maxrecommendedworkingsetsize.md) and is clamped to `Int.max` when necessary. Returns `nil` when unavailable.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/maxrecommendedworkingsetbytes())*