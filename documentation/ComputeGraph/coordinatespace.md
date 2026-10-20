# CoordinateSpace

**Framework**: Compute Graph  
**Kind**: enum  
**Role**: Enumeration

Simulation coordinate space, controlling how positions and orientations are stored.

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
enum CoordinateSpace
```

## Topics

### Enumeration Cases
- [CoordinateSpace.local](./coordinatespace/local.md)
  Positions and orientations are stored in relative to the Entity
- [CoordinateSpace.world](./coordinatespace/world.md)
  Positions and orientations are stored in relative to the Scene.

## Relationships

### Conforms To
- [CaseIterable](../Swift/caseiterable.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Geometry and simulation inputs
- [ComputeNodeGraph.Topology](./computenodegraph/topology.md)
  The primitive topology used to assemble output geometry for an output stage.
- [ComputeNodeGraph.StructureLayout](./computenodegraph/structurelayout.md)
- [enum StripOrientation](./striporientation.md)
  An enumeration that specifies how a strip should be oriented.
- [struct Viewpoint](./viewpoint-swift.struct.md)
  Camera viewpoint parameters in 3D space.
- [struct MouseParams](./mouseparams.md)
  Parameters describing mouse interaction in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/coordinatespace)*