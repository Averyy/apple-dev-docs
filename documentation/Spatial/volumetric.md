# Volumetric

**Framework**: Spatial  
**Kind**: protocol  
**Role**: Protocol

A set of methods for working with Spatial primitives with volume.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
protocol Volumetric
```

## Topics

### Instance properties
- [var size: Size3D](./volumetric/size.md)
  The size of the volume.
### Instance methods
- [func contains(Self) -> Bool](./volumetric/contains%28_%29.md)
  Returns a Boolean value that indicates whether the entity contains the specified volumetric entity.
- [func contains(point: Point3D) -> Bool](./volumetric/contains%28point%29.md)
  Returns a Boolean value that indicates whether this volume contains the specified point.
- [func contains(anyOf: [Point3D]) -> Bool](./volumetric/contains%28anyof%29.md)
  Returns a Boolean value that indicates whether this volume contains any of the specified points.
- [func formIntersection(Self)](./volumetric/formintersection%28_%29.md)
  Sets the primitive to the intersection of itself and the specified primitive.
- [func formUnion(Self)](./volumetric/formunion%28_%29.md)
  Sets the primitive to the union of itself and the specified primitive.
- [func intersection(Self) -> Self?](./volumetric/intersection%28_%29.md)
  Returns the intersection of two volumetric entities.
- [func union(Self) -> Self](./volumetric/union%28_%29.md)
  Returns the smallest volumetric entity that contains the two source entities.
### Deprecated methods
- [func containsAny(of: [Point3D]) -> Bool](./volumetric/containsany%28of%29.md)
  Returns a Boolean value that indicates whether this volume contains any of the specified points.

## Relationships

### Conforming Types
- [Rect3D](./rect3d.md)
- [Size3D](./size3d.md)

## See Also

### Protocols
- [protocol Primitive3D](./primitive3d.md)
  A set of methods common to Spatial primitives.
- [protocol Rotatable3D](./rotatable3d.md)
  A set of methods that defines the interface to rotate Spatial entities.
- [protocol Scalable3D](./scalable3d.md)
  A set of methods that defines the interface to scale Spatial entities.
- [protocol Shearable3D](./shearable3d.md)
  A set of methods that defines the interface to shear Spatial entities.
- [protocol Translatable3D](./translatable3d.md)
  A set of methods that defines the interface to translate Spatial entities.
- [protocol ClampableWithinRectProtocol](./clampablewithinrectprotocol.md)
  A set of methods that defines the interface for Spatial entities that can be clamped to a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/volumetric)*