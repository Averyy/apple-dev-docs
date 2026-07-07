# ComputeNodeGraph.Topology

**Framework**: Compute Graph  
**Kind**: enum

The primitive topology used to assemble output geometry for an output stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
enum Topology
```

#### Overview

Set on an output stage via the `topology` property. The output’s topology determines how the compute graph emits vertex data for each element and how that data is consumed by the render pipeline.

## Topics

### Enumeration Cases
- [ComputeNodeGraph.Topology.instances](computenodegraph/topology/instances.md)
  Elements are rendered as instanced meshes.
- [ComputeNodeGraph.Topology.octagon](computenodegraph/topology/octagon.md)
  Each element emits eight vertices, rendered as an octagon.
- [ComputeNodeGraph.Topology.point](computenodegraph/topology/point.md)
  Each element emits a single vertex.
- [ComputeNodeGraph.Topology.quad](computenodegraph/topology/quad.md)
  Each element emits four vertices, rendered as a quad (two triangles).
- [ComputeNodeGraph.Topology.strip](computenodegraph/topology/strip.md)
  Elements share vertices in a triangle-strip winding order. Requires a simulation with a grouping of `strips`.
- [ComputeNodeGraph.Topology.triangle](computenodegraph/topology/triangle.md)
  Each element emits three vertices, rendered as an independent triangle.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/topology)*