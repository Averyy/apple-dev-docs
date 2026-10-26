---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/memorylimit"
framework: "mlx-swift/MLX"
---

# memoryLimit

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Type Property

Get or set the memory limit.

## Declaration

```swift
static var memoryLimit: Int { get set }
```

#### Discussion

Calls to malloc will wait on scheduled tasks if the limit is exceeded. The memory limit defaults to 1.5 times the maximum recommended working set size reported by the device.

Calls to malloc will wait on scheduled tasks if the limit is exceeded.

Note: `cacheLimit` may be more convenient to manipulate.

##### See Also

- [`cacheLimit`](./cachelimit.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/memorylimit)*