---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/withwiredlimit(_:_:)-8nory"
framework: "mlx-swift/MLX"
---

# withWiredLimit(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Perform the block with a temporarily altered wired memory limit.

> **Deprecated**: Deprecated. Use WiredMemoryManager and tickets instead.

## Declaration

```swift
static func withWiredLimit<R>(_ limit: Int, _ body: () async throws -> R) async rethrows -> R
```

#### Discussion

Note: this manipulates a global value.  Nested calls will work as expected but concurrent calls cannot.

See also [`maxRecommendedWorkingSetSize`](./deviceinfo/maxrecommendedworkingsetsize.md).

## Parameters

- `limit`: New limit in bytes
- `body`: Block to perform


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/withwiredlimit(_:_:)-8nory)*