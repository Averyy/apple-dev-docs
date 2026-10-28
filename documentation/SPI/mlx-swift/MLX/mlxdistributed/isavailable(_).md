---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/isavailable(_:)"
framework: "mlx-swift/MLX"
---

# isAvailable(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Check if a communication backend is available.

## Declaration

```swift
static func isAvailable(_ backend: MLXDistributed.Backend = .any) -> Bool
```

## Return Value

Whether MLX has the capability of instantiating that backend

## Parameters

- `backend`: The backend to check for, defaulting to [`MLXDistributed.Backend.any`](./backend/any.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/isavailable(_:))*