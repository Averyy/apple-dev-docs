---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/cachelimit"
framework: "mlx-swift/MLX"
---

# cacheLimit

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Type Property

Get the free cache limit.

## Declaration

```swift
static var cacheLimit: Int { get }
```

## Discussion

If using more than the given limit, free memory will be reclaimed from the cache on the next allocation. The cache limit defaults to the memory limit.

### See Also

- [`cacheLimit`](../memory/cachelimit.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/cachelimit)*