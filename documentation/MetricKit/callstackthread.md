# CallStackThread

**Framework**: MetricKit  
**Kind**: struct

A single stack thread within a call stack tree.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct CallStackThread
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

## Topics

### Frames
- [let rootFrames: ContiguousArray<CallStackFrame>](callstackthread/rootframes.md)
  Root frames for this call stack thread
- [let threadAttributed: Bool?](callstackthread/threadattributed.md)
  Indicates whether this call stack is attributed to a specific thread.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CallStackTree](callstacktree.md)
  A tree structure representing a collection of call stacks captured during a diagnostic event.
- [struct CallStackFrame](callstackframe.md)
  A single frame within a call stack thread.
- [struct SignpostRecord](signpostrecord.md)
  A record of a signpost event associated with a diagnostic report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstackthread)*