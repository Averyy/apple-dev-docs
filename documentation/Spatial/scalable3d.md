# Scalable3D

**Framework**: Spatial  
**Kind**: protocol

A set of methods that defines the interface to scale Spatial entities.

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
protocol Scalable3D
```

## Topics

### Instance methods
- [func scale(by: Size3D)](scalable3d/scale(by:).md)
  Scales the entity by the specified size.
- [func scaleBy(x: Double, y: Double, z: Double)](scalable3d/scaleby(x:y:z:).md)
  Scales the entity by the specified values.
- [func scaled(by: Size3D) -> Self](scalable3d/scaled(by:).md)
  Returns the entity that results from scaling with the specified size.
- [func scaledBy(x: Double, y: Double, z: Double) -> Self](scalable3d/scaledby(x:y:z:).md)
  Returns the entity that results from scaling with the specified values.
- [func uniformlyScale(by: Double)](scalable3d/uniformlyscale(by:).md)
  Uniformly scales the entity by the specified scalar value.
- [func uniformlyScaled(by: Double) -> Self](scalable3d/uniformlyscaled(by:).md)
  Returns the entity that results from uniformly scaling with the specified scalar value.

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
- [protocol Shearable3D](shearable3d.md)
  A set of methods that defines the interface to shear Spatial entities.
- [protocol Translatable3D](translatable3d.md)
  A set of methods that defines the interface to translate Spatial entities.
- [protocol Volumetric](volumetric.md)
  A set of methods for working with Spatial primitives with volume.
- [protocol ClampableWithinRectProtocol](clampablewithinrectprotocol.md)
  A set of methods that defines the interface for Spatial entities that can be clamped to a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scalable3d)*