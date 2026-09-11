# CoordinateSpace

**Framework**: Compute Graph  
**Kind**: enum

Simulation coordinate space, controlling how positions and orientations are stored.

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
enum CoordinateSpace
```

## Topics

### Enumeration Cases
- [CoordinateSpace.local](coordinatespace/local.md)
  Positions and orientations are stored in relative to the Entity
- [CoordinateSpace.world](coordinatespace/world.md)
  Positions and orientations are stored in relative to the Scene.

## Relationships

### Conforms To
- [CaseIterable](../swift/caseiterable.md)
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum StripOrientation](striporientation.md)
  An enumeration that specifies how a strip should be oriented.
- [struct Viewpoint](viewpoint-swift.struct.md)
  Camera viewpoint parameters in 3D space.
- [struct MouseParams](mouseparams.md)
  Parameters describing mouse interaction in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/coordinatespace)*