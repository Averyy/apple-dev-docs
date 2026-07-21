# CallStackTree

**Framework**: MetricKit  
**Kind**: struct

A tree structure representing a collection of call stacks captured during a diagnostic event.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct CallStackTree
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

Each diagnostic struct — including [`CrashDiagnostic`](crashdiagnostic.md), [`HangDiagnostic`](hangdiagnostic.md), [`CPUExceptionDiagnostic`](cpuexceptiondiagnostic.md), [`DiskWriteExceptionDiagnostic`](diskwriteexceptiondiagnostic.md), [`AppLaunchDiagnostic`](applaunchdiagnostic.md), and [`MemoryExceptionDiagnostic`](memoryexceptiondiagnostic.md) — carries a `callStackTree` property of this type.

The tree is organized into threads via [`callStackThreads`](callstacktree/callstackthreads.md). Each [`CallStackThread`](callstackthread.md) contains root [`CallStackFrame`](callstackframe.md) values that form a tree of sub-frames. Binary metadata is deduplicated in [`binaryInfo`](callstacktree/binaryinfo-swift.property.md), keyed by UUID, so frames reference binaries by UUID rather than repeating the name.

Use [`forEachFrame(_:)`](callstacktree/foreachframe(_:).md) for an optimized iterative depth-first traversal of all frames across all threads:

```swift
callStackTree.forEachFrame { frame in
    if let name = frame.binaryName(from: callStackTree) {
        print(name, frame.offsetIntoBinaryTextSegment ?? 0)
    }
}
```

## Topics

### Threads and frames
- [let callStackThreads: ContiguousArray<CallStackThread>](callstacktree/callstackthreads.md)
  Array of call stack threads
- [let callStackPerThread: Bool](callstacktree/callstackperthread.md)
  Whether call stacks are organized per-thread
- [func forEachFrame((CallStackFrame) throws -> Void) rethrows](callstacktree/foreachframe(_:).md)
  Iterates all frames efficiently.
### Binary information
- [let binaryInfo: [UUID : CallStackTree.BinaryInfo]](callstacktree/binaryinfo-swift.property.md)
  Deduplicated binary information indexed by UUID
### Related types
- [struct CallStackThread](callstackthread.md)
  A single stack thread within a call stack tree.
- [struct CallStackFrame](callstackframe.md)
  A single frame within a call stack thread.
### Structures
- [CallStackTree.BinaryInfo](callstacktree/binaryinfo-swift.struct.md)
  Metadata for a binary referenced in a call stack tree.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CallStackThread](callstackthread.md)
  A single stack thread within a call stack tree.
- [struct CallStackFrame](callstackframe.md)
  A single frame within a call stack thread.
- [struct SignpostRecord](signpostrecord.md)
  A record of a signpost event associated with a diagnostic report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstacktree)*