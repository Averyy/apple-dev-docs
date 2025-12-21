# Rotatable3DProtocol

**Framework**: Spatial  
**Kind**: protocol

A set of methods that defines the interface for Spatial entities that can rotate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol Rotatable3DProtocol<Scalar> : SpatialTypeProtocol
```

## Topics

### Operators
- [static func * (Self.Rotation, Self) -> Self](rotatable3dprotocol/*(_:_:).md)
  Returns the `Rotatable3DFloat` entity rotated by the specified rotation.
### Instance Methods
- [func rotate(by: Self.Quaternion)](rotatable3dprotocol/rotate(by:)-66sot.md)
  Rotates the entity rotated by the specified quaternion around the origin.
- [func rotate(by: Self.Rotation)](rotatable3dprotocol/rotate(by:)-7waub.md)
  Rotates the entity rotated by the specified rotation around the origin.
- [func rotated(by: Self.Rotation) -> Self](rotatable3dprotocol/rotated(by:)-3xjsw.md)
  Returns the entity rotated by the specified rotation around the origin.
- [func rotated(by: Self.Quaternion) -> Self](rotatable3dprotocol/rotated(by:)-4mye4.md)
  Returns the entity rotated by the specified quaternion around the origin.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
### Inherited By
- [Primitive3DProtocol](primitive3dprotocol.md)
### Conforming Types
- [AffineTransform3D](affinetransform3d.md)
- [AffineTransform3DFloat](affinetransform3dfloat.md)
- [Point3D](point3d.md)
- [Point3DFloat](point3dfloat.md)
- [Pose3D](pose3d.md)
- [Pose3DFloat](pose3dfloat.md)
- [ProjectiveTransform3D](projectivetransform3d.md)
- [ProjectiveTransform3DFloat](projectivetransform3dfloat.md)
- [Ray3D](ray3d.md)
- [Ray3DFloat](ray3dfloat.md)
- [Rect3D](rect3d.md)
- [Rect3DFloat](rect3dfloat.md)
- [Rotation3D](rotation3d.md)
- [Rotation3DFloat](rotation3dfloat.md)
- [ScaledPose3D](scaledpose3d.md)
- [ScaledPose3DFloat](scaledpose3dfloat.md)
- [Size3D](size3d.md)
- [Size3DFloat](size3dfloat.md)
- [Vector3D](vector3d.md)
- [Vector3DFloat](vector3dfloat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotatable3dprotocol)*