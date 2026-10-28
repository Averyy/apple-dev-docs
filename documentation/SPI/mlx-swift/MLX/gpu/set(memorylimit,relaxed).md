---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/set(memorylimit:relaxed:)"
framework: "mlx-swift/MLX"
---

# set(memoryLimit:relaxed:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Set the memory limit.

> **Deprecated**: use Memory.memoryLimit property

## Declaration

```swift
static func set(memoryLimit: Int, relaxed: Bool = true)
```

## Discussion

Calls to malloc will wait on scheduled tasks if the limit is exceeded.

The memory limit defaults to 1.5 times the maximum recommended working set size reported by the device ([recommendedMaxWorkingSetSize](https://developer.apple.com/documentation/metal/mtldevice/recommendedmaxworkingsetsize)).

**Important**: This limit controls total MLX memory allocation. The cache limit (see [`cacheLimit`](../memory/cachelimit.md)) defaults to this value, so systems with large memory limits may cache many GB of buffers. Consider setting a lower cache limit for memory-constrained applications.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/set(memorylimit:relaxed:))*