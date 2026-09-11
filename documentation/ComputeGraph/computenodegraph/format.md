# ComputeNodeGraph.Format

**Framework**: Compute Graph  
**Kind**: enum

A serialization format used to encode a compute node graph.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
enum Format
```

#### Overview

Use a value of this type with [`data(using:)`](computenodegraph/data(using:).md) to choose how the graph is written. Both formats round-trip through [`init(data:)`](computenodegraph/init(data:).md), which detects the format automatically when reading.

Choose [`ComputeNodeGraph.Format.json`](computenodegraph/format/json.md) when you want a human-readable representation that is easy to inspect, diff, or edit by hand. Choose [`ComputeNodeGraph.Format.propertyList`](computenodegraph/format/propertylist.md) when you want a compact binary representation that is faster to read and write and produces smaller files.

## Topics

### Enumeration Cases
- [ComputeNodeGraph.Format.json](computenodegraph/format/json.md)
  A human-readable JSON representation.
- [ComputeNodeGraph.Format.propertyList](computenodegraph/format/propertylist.md)
  A compact binary property list representation.

## Relationships

### Conforms To
- [CaseIterable](../swift/caseiterable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/format)*