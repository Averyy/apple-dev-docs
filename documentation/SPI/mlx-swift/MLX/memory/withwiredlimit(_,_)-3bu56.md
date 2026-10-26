---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/withwiredlimit(_:_:)-3bu56"
framework: "mlx-swift/MLX"
---

# withWiredLimit(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Perform the block with a temporarily altered wired memory limit.

> **Deprecated**: Deprecated. Use WiredMemoryManager and tickets; async variant uses the shared manager.

## Declaration

```swift
static func withWiredLimit<R>(_ limit: Int, _ body: () async throws -> R) async rethrows -> R
```

#### Discussion

> ❗ **Important**: This overload is deprecated and now uses the shared [`WiredMemoryManager`](../wiredmemorymanager.md) with a static sum policy to avoid bypassing admission control.

## Parameters

- `limit`: Requested limit in bytes
- `body`: Block to perform


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/withwiredlimit(_:_:)-3bu56)*