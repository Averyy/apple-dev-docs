# Translatable3DProtocol

**Framework**: Spatial  
**Kind**: protocol

A set of methods that defines the interface for Spatial entities that can translate.

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
protocol Translatable3DProtocol<Scalar> : SpatialTypeProtocol
```

## Topics

### Instance Methods
- [func translate(by: Self.Vector)](translatable3dprotocol/translate(by:).md)
  Translates the entity by the specified vector.
- [func translated(by: Self.Vector) -> Self](translatable3dprotocol/translated(by:).md)
  Returns the entity translated by the specified vector.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
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
- [ScaledPose3D](scaledpose3d.md)
- [ScaledPose3DFloat](scaledpose3dfloat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/translatable3dprotocol)*