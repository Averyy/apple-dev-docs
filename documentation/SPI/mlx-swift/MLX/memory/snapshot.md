---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/snapshot"
framework: "mlx-swift/MLX"
---

# Memory.Snapshot

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Snapshot of memory stats.

## Declaration

```swift
struct Snapshot
```

#### Overview

[`activeMemory`](./snapshot/activememory.md) + [`cacheMemory`](./snapshot/cachememory.md) is the total memory allocated by MLX. [`activeMemory`](./snapshot/activememory.md) is in currently active [`MLXArray`](../mlxarray.md) and [`cacheMemory`](./snapshot/cachememory.md) is recently used memory that can be recycled.

See [`GPU`](../gpu.md) for a description of how the cache sizes grow and can be tuned.

Control the size of cache memory via [`cacheLimit`](./cachelimit.md) and the overall memory limit with [`memoryLimit`](./memorylimit.md).

This might be used to examine memory use over a run or sample it during a run:

```swift
// load model & weights
...

let startMemory = Memory.snapshot()

// work
...

let endMemory = Memory.snapshot()

// what stats are interesting to you?

print("=======")
print("Memory size: \(Memory.memoryLimit / 1024)K")
print("Cache size:  \(Memory.cacheLimit / 1024)K")

print("")
print("=======")
print("Starting memory")
print(startMemory.description)

print("")
print("=======")
print("Ending memory")
print(endMemory.description)

print("")
print("=======")
print("Growth")
print(startMemory.delta(endMemory).description)
```

##### See Also

- [`snapshot()`](./snapshot%28%29.md)
- [Running on iOS](../running-on-ios.md)

## Topics

### Initializers
- [init(from: any Decoder) throws](./snapshot/init%28from%29.md)
### Instance Properties
- [var activeMemory: Int](./snapshot/activememory.md)
  See [`activeMemory`](./activememory.md).
- [var cacheMemory: Int](./snapshot/cachememory.md)
  See [`cacheMemory`](./cachememory.md).
- [var description: String](./snapshot/description.md)
- [var peakMemory: Int](./snapshot/peakmemory.md)
  See [`peakMemory`](./peakmemory.md).
### Instance Methods
- [func delta(Memory.Snapshot) -> Memory.Snapshot](./snapshot/delta%28_%29.md)
  Compute the difference between two snapshots:

## Relationships

### Conforms To
- Swift.CustomStringConvertible
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/snapshot)*