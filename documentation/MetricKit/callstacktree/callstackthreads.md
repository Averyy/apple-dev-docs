# callStackThreads

**Framework**: MetricKit  
**Kind**: property

Array of call stack threads

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let callStackThreads: ContiguousArray<CallStackThread>
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

## See Also

- [let callStackPerThread: Bool](callstacktree/callstackperthread.md)
  Whether call stacks are organized per-thread
- [func forEachFrame((CallStackFrame) throws -> Void) rethrows](callstacktree/foreachframe(_:).md)
  Iterates all frames efficiently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstacktree/callstackthreads)*