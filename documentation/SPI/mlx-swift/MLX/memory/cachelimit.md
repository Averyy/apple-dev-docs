---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/cachelimit"
framework: "mlx-swift/MLX"
---

# cacheLimit

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Type Property

Get or set the free cache limit.

## Declaration

```swift
static var cacheLimit: Int { get set }
```

#### Discussion

If using more than the given limit, free memory will be reclaimed from the cache on the next allocation.

The cache limit defaults to the memory limit, which may allow very large cache sizes on systems with abundant RAM. For memory-constrained applications or to prevent excessive memory growth during long inference runs, consider setting a much lower cache limit.

To disable the cache, set the limit to 0.

#### Performance Optimization

The optimal cache size varies by workload. Many developers find that relatively small cache sizes (e.g., 2MB) perform just as well as unconstrained cache sizes for their specific use cases. Experiment with different values and measure performance to find the best setting for your workload.

See [`Memory`](../memory.md) for more information on cache sizing and tuning.

##### See Also

- [`memoryLimit`](./memorylimit.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/cachelimit)*