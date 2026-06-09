# CallStackFrame

**Framework**: MetricKit  
**Kind**: struct

A single frame within a call stack thread.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct CallStackFrame
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

Each frame may have sub-frames that form a call tree. The [`binaryUUID`](callstackframe/binaryuuid.md) references binary metadata in the parent [`binaryInfo`](callstacktree/binaryinfo-swift.property.md) dictionary. Use [`binaryName(from:)`](callstackframe/binaryname(from:).md) to look up the binary name for a given frame:

```swift
if let name = frame.binaryName(from: tree) {
    print(name)
}
```

## Topics

### Frame details
- [let binaryUUID: UUID?](callstackframe/binaryuuid.md)
  Binary UUID (references CallStackTree.binaryInfo)
- [let address: UInt64?](callstackframe/address.md)
  Absolute address
- [let offsetIntoBinaryTextSegment: UInt64?](callstackframe/offsetintobinarytextsegment.md)
  Offset into binary text segment
- [let sampleCount: Int?](callstackframe/samplecount.md)
  Sample count (for sampled stack traces)
### Tree navigation
- [let subFrames: ContiguousArray<CallStackFrame>](callstackframe/subframes.md)
  Sub-frames (children in the call tree)
- [func binaryName(from: CallStackTree) -> String?](callstackframe/binaryname(from:).md)
  Binary name - look up from tree

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
- [struct CallStackThread](callstackthread.md)
  A single stack thread within a call stack tree.
- [struct SignpostRecord](signpostrecord.md)
  A record of a signpost event associated with a diagnostic report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstackframe)*