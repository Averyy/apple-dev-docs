---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory"
framework: "mlx-swift/MLX"
---

# Memory

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

Properties to control the the memory allocation and buffer reuse.

## Declaration

```swift
enum Memory
```

## Mentions

- [Running on iOS](./running-on-ios.md)

## Overview

[`activeMemory`](./memory/activememory.md) + [`cacheMemory`](./memory/cachememory.md) is the total memory allocated by MLX. [`activeMemory`](./memory/activememory.md) is in currently active [`MLXArray`](./mlxarray.md) and [`cacheMemory`](./memory/cachememory.md) is recently used memory that can be recycled.

## Memory Management and Buffer Recycling

MLX uses a buffer recycling system to optimize performance. When MLXArrays are no longer needed (such as intermediate computation results), their buffers are not immediately deallocated. Instead, they are placed in a buffer pool where they can be reused by later computations of similar size.

This recycling strategy is particularly important during model inference:

- Initial model weights might use ~500MB
- Inference (e.g. token generation in an LLM) creates intermediate buffers (e.g., ~1MB for the first token)
- These buffer might be intermediates used during computation of the graph – if they are fixed size then they will be reused on the next token – exactly what we want!
- If the buffer sizes grow during inference, e.g. if not using a KVCache in LLMs or other scenarios where there might be a “context” then these buffers might not be reused
- By the end of a long inference run, you may see several GB of cached memory from accumulated buffers of various sizes if cache memory is unconstrained.

This memory is observable in various system tools as *footprint* or *RSIZE*, but these tools can’t discern the use of the memory.  See [`snapshot()`](./memory/snapshot%28%29.md) and the next section for more information.

The buffer pool policy is based on Metal’s `recommendedMaxWorkingSetSize`, which scales with available physical memory. Systems with more RAM will cache more buffers.

## Cache Size Optimization

The optimal cache size varies significantly by workload. While unconstrained cache can grow to several GB, developers often find that relatively small cache sizes (e.g., 2MB) perform just as well for their specific use cases. The best approach is to experiment with different cache limits and measure performance for your particular workload.

Adjusting the cache limit is especially advantageous on devices with memory limits (e.g. iOS devices where jetsam limits apply).

Control the size of cache memory via [`cacheLimit`](./memory/cachelimit.md) and the overall memory limit with [`memoryLimit`](./memory/memorylimit.md).

Examine memory use over time with [`snapshot()`](./memory/snapshot%28%29.md) and [`Memory.Snapshot`](./memory/snapshot.md).

**Note**: The cache limit will go into effect on the next deallocation. Because of that you may observe the cache size temporarily exceeding the requested limit. To immediately clear the cache, use [`clearCache()`](./memory/clearcache%28%29.md).

### See Also

- [Running on iOS](./running-on-ios.md)
- [`cacheLimit`](./memory/cachelimit.md)
- [`memoryLimit`](./memory/memorylimit.md)
- [`snapshot()`](./memory/snapshot%28%29.md)

## Topics

### Structures
- [Memory.Snapshot](./memory/snapshot.md)
  Snapshot of memory stats.
### Type Properties
- [static var activeMemory: Int](./memory/activememory.md)
  Get the actively used memory in bytes.
- [static var cacheLimit: Int](./memory/cachelimit.md)
  Get or set the free cache limit.
- [static var cacheMemory: Int](./memory/cachememory.md)
  Get the cache size in bytes.
- [static var memoryLimit: Int](./memory/memorylimit.md)
  Get or set the memory limit.
- [static var peakMemory: Int](./memory/peakmemory.md)
  Get the peak amount of active memory in bytes.
### Type Methods
- [static func clearCache()](./memory/clearcache%28%29.md)
  Cause all cached buffers to be deallocated.
- [static func snapshot() -> Memory.Snapshot](./memory/snapshot%28%29.md)
  Return a snapshot of memory stats – see [`Memory.Snapshot`](./memory/snapshot.md) for more details.
- [static func withWiredLimit<R>(Int, () async throws -> R) async rethrows -> R](./memory/withwiredlimit%28_,_%29-3bu56.md)
  Perform the block with a temporarily altered wired memory limit.
- [static func withWiredLimit<R>(Int, () throws -> R) rethrows -> R](./memory/withwiredlimit%28_,_%29-94v.md)
  Perform the block with a temporarily altered wired memory limit.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory)*