# StripOrientation

**Framework**: Compute Graph  
**Kind**: enum

An enumeration that specifies how a strip should be oriented.

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

- [enum CoordinateSpace](coordinatespace.md)
  Simulation coordinate space, controlling how positions and orientations are stored.
- [struct Viewpoint](viewpoint-swift.struct.md)
  Camera viewpoint parameters in 3D space.
- [struct MouseParams](mouseparams.md)
  Parameters describing mouse interaction in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/striporientation)*