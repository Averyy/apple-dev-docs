# threadAttributed

**Framework**: MetricKit  
**Kind**: property

Indicates whether this call stack is attributed to a specific thread.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let threadAttributed: Bool?
```

#### Discussion

This field is only present when `CallStackTree.callStackPerThread` is `true`.

## See Also

- [let rootFrames: ContiguousArray<CallStackFrame>](callstackthread/rootframes.md)
  Root frames for this call stack thread


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstackthread/threadattributed)*