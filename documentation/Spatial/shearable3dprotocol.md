# Shearable3DProtocol

**Framework**: Spatial  
**Kind**: protocol

A set of methods that defines the interface for Spatial entities that can shear.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
protocol Shearable3DProtocol<Scalar> : SpatialTypeProtocol
```

## Topics

### Instance Methods
- [func shear(Self.AxisEnumeration)](shearable3dprotocol/shear(_:).md)
  Shears the entity.
- [func sheared(Self.AxisEnumeration) -> Self](shearable3dprotocol/sheared(_:).md)
  Returns a sheared entity.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/shearable3dprotocol)*