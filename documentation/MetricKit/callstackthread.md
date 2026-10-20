# CallStackThread

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A single stack thread within a call stack tree.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct CallStackThread
```

## Mentions

- [Analyzing app performance with MetricKit](./analyzing-app-performance-with-metrickit.md)

## Topics

### Frames
- [let rootFrames: ContiguousArray<CallStackFrame>](./callstackthread/rootframes.md)
  Root frames for this call stack thread
- [let threadAttributed: Bool?](./callstackthread/threadattributed.md)
  Indicates whether this call stack is attributed to a specific thread.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Call stack data
- [struct CallStackTree](./callstacktree.md)
  A tree structure representing a collection of call stacks captured during a diagnostic event.
- [struct CallStackFrame](./callstackframe.md)
  A single frame within a call stack thread.
- [struct SignpostRecord](./signpostrecord.md)
  A record of a signpost event associated with a diagnostic report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstackthread)*