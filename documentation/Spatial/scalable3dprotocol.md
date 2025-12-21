# Scalable3DProtocol

**Framework**: Spatial  
**Kind**: protocol

A set of methods that defines the interface for Spatial entities that can scale.

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
protocol Scalable3DProtocol<Scalar> : SpatialTypeProtocol
```

## Topics

### Instance Methods
- [func scale(by: Self.Size)](scalable3dprotocol/scale(by:).md)
  Scales the entity by the specified size.
- [func scaleBy(x: Self.Scalar, y: Self.Scalar, z: Self.Scalar)](scalable3dprotocol/scaleby(x:y:z:).md)
  Scales the entity by the specified values.
- [func scaled(by: Self.Size) -> Self](scalable3dprotocol/scaled(by:).md)
  Returns the entity scaled by the specified size.
- [func scaledBy(x: Self.Scalar, y: Self.Scalar, z: Self.Scalar) -> Self](scalable3dprotocol/scaledby(x:y:z:).md)
  Returns the entity scaled by the specified values.
- [func uniformlyScale(by: Self.Scalar)](scalable3dprotocol/uniformlyscale(by:).md)
  Uniformly scales the entity by the specified scalar value.
- [func uniformlyScaled(by: Self.Scalar) -> Self](scalable3dprotocol/uniformlyscaled(by:).md)
  Returns the entity uniformly scaled by the specified scalar value.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
### Conforming Types
- [AffineTransform3D](affinetransform3d.md)
- [AffineTransform3DFloat](affinetransform3dfloat.md)
- [ProjectiveTransform3D](projectivetransform3d.md)
- [ProjectiveTransform3DFloat](projectivetransform3dfloat.md)
- [Rect3D](rect3d.md)
- [Rect3DFloat](rect3dfloat.md)
- [Size3D](size3d.md)
- [Size3DFloat](size3dfloat.md)
- [Vector3D](vector3d.md)
- [Vector3DFloat](vector3dfloat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scalable3dprotocol)*