---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanager/start(id:size:policy:kind:)"
framework: "mlx-swift/MLX"
---

# start(id:size:policy:kind:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Main entry point for ticket admission.

## Declaration

```swift
func start(id: UUID, size: Int, policy: any WiredMemoryPolicy, kind: WiredMemoryTicketKind) async -> Int
```

#### Discussion

Flow:

1. Capture the baseline (current wired limit).
2. If `canAdmit` fails, suspend until capacity is available.
3. Register the ticket, recompute desired limit, and apply it.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanager/start(id:size:policy:kind:))*