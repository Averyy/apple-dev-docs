---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/snapshot()"
framework: "mlx-swift/MLX"
---

# snapshot()

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Return a snapshot of memory stats – see [`Memory.Snapshot`](../memory/snapshot.md) for more details.

## Declaration

```swift
static func snapshot() -> GPU.Snapshot
```

## Discussion

Get the current memory use.  This can be used to measure before/after and current memory use:

```swift
let currentMemory = Memory.snapshot()
print(currentMemory)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/snapshot())*