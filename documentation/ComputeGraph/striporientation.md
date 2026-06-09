# StripOrientation

**Framework**: ComputeGraph  
**Kind**: enum

An enumeration that specifies how a strip should be oriented.

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
enum StripOrientation
```

## Topics

### Enumeration Cases
- [StripOrientation.auto](striporientation/auto.md)
  Automatically derive the orientation of the strip via neighbors and any provided axisY or axisZ values.
- [StripOrientation.deriveFromYAxis](striporientation/derivefromyaxis.md)
  Derive the strip’s orientation from neighboring points and `axisY` float3 parameter
- [StripOrientation.deriveFromZAxis](striporientation/derivefromzaxis.md)
  Derive the strip’s orientation from neighboring points and `axisZ` float3 parameter
- [StripOrientation.frenet](striporientation/frenet.md)
  Use strip’s frenet frame for orientation
- [StripOrientation.planar](striporientation/planar.md)
- [StripOrientation.useZAxis](striporientation/usezaxis.md)
  Use the `axisZ` float3 parameter without re-orienting. Derive Y-axis from neighboring points and `axisZ`.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum Topology](topology.md)
- [enum CoordinateSpace](coordinatespace.md)
  Simulation coordinate space, controlling how positions and orientations are stored.
- [struct Viewpoint](viewpoint-swift.struct.md)
  Camera viewpoint parameters in 3D space.
- [struct MouseParams](mouseparams.md)
  Parameters describing mouse interaction in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/striporientation)*