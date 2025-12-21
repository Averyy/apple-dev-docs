# SpatialTypeProtocol

**Framework**: Spatial  
**Kind**: protocol

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
protocol SpatialTypeProtocol<Scalar> : Decodable, Encodable, Equatable
```

## Topics

### Associated Types
- [associatedtype AffineTransform : Transform3DProtocol](spatialtypeprotocol/affinetransform.md)
- [associatedtype AxisEnumeration](spatialtypeprotocol/axisenumeration.md)
- [associatedtype Point : Primitive3DProtocol](spatialtypeprotocol/point.md)
- [associatedtype Pose : Rotatable3DProtocol, Translatable3DProtocol](spatialtypeprotocol/pose.md)
- [associatedtype ProjectiveTransform : Transform3DProtocol](spatialtypeprotocol/projectivetransform.md)
- [associatedtype Quaternion](spatialtypeprotocol/quaternion.md)
- [associatedtype Rect : Primitive3DProtocol](spatialtypeprotocol/rect.md)
- [associatedtype Rotation : Rotatable3DProtocol](spatialtypeprotocol/rotation.md)
- [associatedtype Scalar : Numeric](spatialtypeprotocol/scalar.md)
- [associatedtype Size : Primitive3DProtocol](spatialtypeprotocol/size.md)
- [associatedtype Vector : Primitive3DProtocol](spatialtypeprotocol/vector.md)

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
### Inherited By
- [ClampableWithinRectProtocol](clampablewithinrectprotocol.md)
- [Primitive3DProtocol](primitive3dprotocol.md)
- [Rotatable3DProtocol](rotatable3dprotocol.md)
- [Scalable3DProtocol](scalable3dprotocol.md)
- [Shearable3DProtocol](shearable3dprotocol.md)
- [Transform3DProtocol](transform3dprotocol.md)
- [Translatable3DProtocol](translatable3dprotocol.md)
- [VolumetricProtocol](volumetricprotocol.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spatialtypeprotocol)*