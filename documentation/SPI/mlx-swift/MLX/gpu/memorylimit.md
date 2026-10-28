---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/memorylimit"
framework: "mlx-swift/MLX"
---

# memoryLimit

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Type Property

Get the memory limit.

## Declaration

```swift
static var memoryLimit: Int { get }
```

## Discussion

Calls to malloc will wait on scheduled tasks if the limit is exceeded. The memory limit defaults to 1.5 times the maximum recommended working set size reported by the device.

### See Also

- [`memoryLimit`](../memory/memorylimit.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/memorylimit)*