# ComputeNodeGraph.Format

**Framework**: Compute Graph  
**Kind**: enum  
**Role**: Enumeration

A serialization format used to encode a compute node graph.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
enum Format
```

## Overview

Use a value of this type with [`data(using:)`](./data%28using%29.md) to choose how the graph is written. Both formats round-trip through [`init(data:)`](./init%28data%29.md), which detects the format automatically when reading.

Choose [`ComputeNodeGraph.Format.json`](./format/json.md) when you want a human-readable representation that is easy to inspect, diff, or edit by hand. Choose [`ComputeNodeGraph.Format.propertyList`](./format/propertylist.md) when you want a compact binary representation that is faster to read and write and produces smaller files.

## Topics

### Enumeration Cases
- [ComputeNodeGraph.Format.json](./format/json.md)
  A human-readable JSON representation.
- [ComputeNodeGraph.Format.propertyList](./format/propertylist.md)
  A compact binary property list representation.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/format)*