---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu"
framework: "mlx-swift/MLX"
---

# GPU

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

API for controlling GPU related features.

## Declaration

```swift
enum GPU
```

## Overview

Note: previously this also had properties that managed the buffer use – those are now found in [`Memory`](./memory.md) but remain here as deprecated.

### See Also

- [Running on iOS](./running-on-ios.md)
- [`Memory`](./memory.md)

## Topics

### Structures
- [struct DeviceInfo](./gpu/deviceinfo.md)
### Type Aliases
- [typealias Snapshot](./gpu/snapshot.md)
### Type Properties
- [static var activeMemory: Int](./gpu/activememory.md)
  Get the actively used memory in bytes.
- [static var cacheLimit: Int](./gpu/cachelimit.md)
  Get the free cache limit.
- [static var cacheMemory: Int](./gpu/cachememory.md)
  Get the cache size in bytes.
- [static var memoryLimit: Int](./gpu/memorylimit.md)
  Get the memory limit.
- [static var metallib: URL?](./gpu/metallib.md)
  The metallib override path.  This can be set early in the process to override or provide the metallib load path.
- [static var peakMemory: Int](./gpu/peakmemory.md)
  Get the peak amount of active memory in bytes.
### Type Methods
- [static func clearCache()](./gpu/clearcache%28%29.md)
  Cause all cached metal buffers to be deallocated.
- [static func deviceInfo() -> GPU.DeviceInfo](./gpu/deviceinfo%28%29.md)
  Get information about the GPU device and system settings
- [static func maxRecommendedWorkingSetBytes() -> Int?](./gpu/maxrecommendedworkingsetbytes%28%29.md)
  Returns Metal’s recommended working set size in bytes as an `Int`.
- [static func resetPeakMemory()](./gpu/resetpeakmemory%28%29.md)
  Reset the peak memory to zero.
- [static func set(cacheLimit: Int)](./gpu/set%28cachelimit%29.md)
  Set the free cache limit.
- [static func set(memoryLimit: Int, relaxed: Bool)](./gpu/set%28memorylimit,relaxed%29.md)
  Set the memory limit.
- [static func snapshot() -> GPU.Snapshot](./gpu/snapshot%28%29.md)
  Return a snapshot of memory stats – see [`Memory.Snapshot`](./memory/snapshot.md) for more details.
- [static func startCapture(url: URL)](./gpu/startcapture%28url%29.md)
  Start capturing a metal trace into the given file.
- [static func stopCapture(url: URL)](./gpu/stopcapture%28url%29.md)
  Stop the metal capture.
- [static func withWiredLimit<R>(Int, () throws -> R) rethrows -> R](./gpu/withwiredlimit%28_,_%29-6fm65.md)
  Perform the block with a temporarily altered wired memory limit.
- [static func withWiredLimit<R>(Int, () async throws -> R) async rethrows -> R](./gpu/withwiredlimit%28_,_%29-8nory.md)
  Perform the block with a temporarily altered wired memory limit.

## See Also

### Memory
- [actor WiredMemoryManager](./wiredmemorymanager.md)
  Central coordinator for process-wide wired memory limits.
- [struct WiredMemoryTicket](./wiredmemoryticket.md)
  Handle for coordinating wired memory changes across concurrent work.
- [protocol WiredMemoryPolicy](./wiredmemorypolicy.md)
  Policy for computing a process-global wired memory limit.
- [struct WiredMemoryEvent](./wiredmemoryevent.md)
  Debug event emitted by [`WiredMemoryManager`](./wiredmemorymanager.md) when coordinating wired memory changes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu)*