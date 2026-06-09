# Topology

**Framework**: ComputeGraph  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
enum Topology
```

## Topics

### Enumeration Cases
- [Topology.instances](topology/instances.md)
- [Topology.octagon](topology/octagon.md)
- [Topology.point](topology/point.md)
- [Topology.quad](topology/quad.md)
- [Topology.strip](topology/strip.md)
- [Topology.triangle](topology/triangle.md)
### Initializers
- [init(ComputeNodeGraph.Topology)](topology/init(_:).md)
### Instance Properties
- [var indicesPerElement: Int](topology/indicesperelement.md)
- [var verticesPerElement: Int](topology/verticesperelement.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum CoordinateSpace](coordinatespace.md)
  Simulation coordinate space, controlling how positions and orientations are stored.
- [enum StripOrientation](striporientation.md)
  An enumeration that specifies how a strip should be oriented.
- [struct Viewpoint](viewpoint-swift.struct.md)
  Camera viewpoint parameters in 3D space.
- [struct MouseParams](mouseparams.md)
  Parameters describing mouse interaction in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/topology)*