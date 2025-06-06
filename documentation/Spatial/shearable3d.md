# Shearable3D

**Framework**: Spatial  
**Kind**: protocol

A set of methods that defines the interface to shear Spatial entities.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol Shearable3D
```

## Topics

### Instance methods
- [func shear(AxisWithFactors)](shearable3d/shear(_:).md)
  Shears the entity by the specified axis and shear factors.
- [func sheared(AxisWithFactors) -> Self](shearable3d/sheared(_:).md)
  Returns the entity that results from shearing with the specified axis and shear factors.

## Relationships

### Conforming Types
- [AffineTransform3D](affinetransform3d.md)
- [ProjectiveTransform3D](projectivetransform3d.md)
- [Rect3D](rect3d.md)
- [Size3D](size3d.md)
- [Vector3D](vector3d.md)

## See Also

- [protocol Primitive3D](primitive3d.md)
  A set of methods common to Spatial primitives.
- [protocol Rotatable3D](rotatable3d.md)
  A set of methods that defines the interface to rotate Spatial entities.
- [protocol Scalable3D](scalable3d.md)
  A set of methods that defines the interface to scale Spatial entities.
- [protocol Translatable3D](translatable3d.md)
  A set of methods that defines the interface to translate Spatial entities.
- [protocol Volumetric](volumetric.md)
  A set of methods for working with Spatial primitives with volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/shearable3d)*