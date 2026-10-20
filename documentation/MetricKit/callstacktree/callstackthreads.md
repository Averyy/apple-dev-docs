# callStackThreads

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

Array of call stack threads

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let callStackThreads: ContiguousArray<CallStackThread>
```

## Mentions

- [Analyzing app performance with MetricKit](../analyzing-app-performance-with-metrickit.md)

## See Also

### Threads and frames
- [let callStackPerThread: Bool](./callstackperthread.md)
  Whether call stacks are organized per-thread
- [func forEachFrame((CallStackFrame) throws -> Void) rethrows](./foreachframe%28_%29.md)
  Iterates all frames efficiently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstacktree/callstackthreads)*