---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanager/end(id:policy:)"
framework: "mlx-swift/MLX"
---

# end(id:policy:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Releases a ticket and recomputes the limit.

## Declaration

```swift
func end(id: UUID, policy: any WiredMemoryPolicy) -> Int
```

## Discussion

If this was the last ticket, the manager restores the baseline and clears internal state.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanager/end(id:policy:))*