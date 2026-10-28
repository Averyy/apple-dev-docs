---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/cachememory"
framework: "mlx-swift/MLX"
---

# cacheMemory

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Type Property

Get the cache size in bytes.

## Declaration

```swift
static var cacheMemory: Int { get }
```

## Discussion

The cache includes memory not currently used that has not been returned to the system allocator. This represents buffers from previous computations that are kept in a buffer pool for potential reuse.

During model inference, this can grow significantly as buffers of various sizes accumulate from intermediate computations.  See [`GPU`](../gpu.md) for more information on cache size and tuning.

The cache size is controlled by the cache limit (see [`cacheLimit`](../memory/cachelimit.md)). When the limit is exceeded, older cached buffers are freed on the next allocatioån.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/cachememory)*