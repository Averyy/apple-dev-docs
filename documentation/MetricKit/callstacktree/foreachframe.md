# forEachFrame(_:)

**Framework**: MetricKit  
**Kind**: method

Iterates all frames efficiently.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func forEachFrame(_ body: (CallStackFrame) throws -> Void) rethrows
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

Use this method for optimized traversal of the entire call stack tree.

## Parameters

- `body`: A closure that processes each frame

## See Also

- [let callStackThreads: ContiguousArray<CallStackThread>](callstacktree/callstackthreads.md)
  Array of call stack threads
- [let callStackPerThread: Bool](callstacktree/callstackperthread.md)
  Whether call stacks are organized per-thread


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstacktree/foreachframe(_:))*