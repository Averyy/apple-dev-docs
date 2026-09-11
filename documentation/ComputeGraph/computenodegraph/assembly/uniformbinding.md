# ComputeNodeGraph.Assembly.UniformBinding

**Framework**: Compute Graph  
**Kind**: struct

Describes how a uniform value is located within the graph’s uniform buffer.

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
struct UniformBinding
```

#### Overview

A uniform binding combines a `Relocation_v1` (the byte offset and size within the uniform buffer) with a [`ComputeNodeGraph.StateType`](computenodegraph/statetype.md) describing the data layout at that location.

## Topics

### Initializers
- [init(location: ComputeNodeGraph.Assembly.Location, type: ComputeNodeGraph.StateType)](computenodegraph/assembly/uniformbinding/init(location:type:).md)
### Instance Properties
- [var location: ComputeNodeGraph.Assembly.Location](computenodegraph/assembly/uniformbinding/location.md)
  The location of this uniform within the uniform buffer.
- [var type: ComputeNodeGraph.StateType](computenodegraph/assembly/uniformbinding/type.md)
  The data type stored at this location.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly/uniformbinding)*