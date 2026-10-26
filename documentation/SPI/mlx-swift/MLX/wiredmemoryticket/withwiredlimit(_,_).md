---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemoryticket/withwiredlimit(_:_:)"
framework: "mlx-swift/MLX"
---

# withWiredLimit(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Keeps the ticket active until the body returns or throws, including during cancellation.

## Declaration

```swift
static func withWiredLimit<R>(_ ticket: WiredMemoryTicket, _ body: () async throws -> R) async rethrows -> R
```

#### Discussion

If admission is cancelled, the body still runs in the cancelled task so it can clean up. Check cancellation before starting work that requires admission. Use a distinct ticket for each overlapping scope.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemoryticket/withwiredlimit(_:_:))*