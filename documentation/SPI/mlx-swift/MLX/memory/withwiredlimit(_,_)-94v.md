---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/withwiredlimit(_:_:)-94v"
framework: "mlx-swift/MLX"
---

# withWiredLimit(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Perform the block with a temporarily altered wired memory limit.

> **Deprecated**: Deprecated. Use WiredMemoryManager and tickets; synchronous variant is a no-op.

## Declaration

```swift
static func withWiredLimit<R>(_ limit: Int, _ body: () throws -> R) rethrows -> R
```

#### Discussion

> ❗ **Important**: This synchronous overload is deprecated and is now a no-op. Use [`WiredMemoryManager`](../wiredmemorymanager.md) with tickets instead.

## Parameters

- `limit`: Requested limit in bytes (ignored)
- `body`: Block to perform


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/withwiredlimit(_:_:)-94v)*