# ComputeNodeGraph.Assembly.UniformBinding

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

Describes how a uniform value is located within the graph’s uniform buffer.

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
struct UniformBinding
```

## Overview

A uniform binding combines a `Relocation_v1` (the byte offset and size within the uniform buffer) with a [`ComputeNodeGraph.StateType`](../statetype.md) describing the data layout at that location.

## Topics

### Initializers
- [init(location: ComputeNodeGraph.Assembly.Location, type: ComputeNodeGraph.StateType)](./uniformbinding/init%28location,type%29.md)
### Instance Properties
- [var location: ComputeNodeGraph.Assembly.Location](./uniformbinding/location.md)
  The location of this uniform within the uniform buffer.
- [var type: ComputeNodeGraph.StateType](./uniformbinding/type.md)
  The data type stored at this location.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly/uniformbinding)*