# Volumetric

**Framework**: Spatial  
**Kind**: protocol

A set of methods for working with Spatial primitives with volume.

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
protocol Volumetric
```

## Topics

### Instance properties
- [var size: Size3D](volumetric/size.md)
  The size of the volume.
### Instance methods
- [func contains(Self) -> Bool](volumetric/contains(_:).md)
  Returns a Boolean value that indicates whether the entity contains the specified volumetric entity.
- [func contains(point: Point3D) -> Bool](volumetric/contains(point:).md)
  Returns a Boolean value that indicates whether this volume contains the specified point.
- [func contains(anyOf: [Point3D]) -> Bool](volumetric/contains(anyof:).md)
  Returns a Boolean value that indicates whether this volume contains any of the specified points.
- [func formIntersection(Self)](volumetric/formintersection(_:).md)
  Sets the primitive to the intersection of itself and the specified primitive.
- [func formUnion(Self)](volumetric/formunion(_:).md)
  Sets the primitive to the union of itself and the specified primitive.
- [func intersection(Self) -> Self?](volumetric/intersection(_:).md)
  Returns the intersection of two volumetric entities.
- [func union(Self) -> Self](volumetric/union(_:).md)
  Returns the smallest volumetric entity that contains the two source entities.
### Deprecated methods
- [func containsAny(of: [Point3D]) -> Bool](volumetric/containsany(of:).md)
  Returns a Boolean value that indicates whether this volume contains any of the specified points.

## Relationships

### Conforming Types
- [Rect3D](rect3d.md)
- [Size3D](size3d.md)

## See Also

- [protocol Primitive3D](primitive3d.md)
  A set of methods common to Spatial primitives.
- [protocol Rotatable3D](rotatable3d.md)
  A set of methods that defines the interface to rotate Spatial entities.
- [protocol Scalable3D](scalable3d.md)
  A set of methods that defines the interface to scale Spatial entities.
- [protocol Shearable3D](shearable3d.md)
  A set of methods that defines the interface to shear Spatial entities.
- [protocol Translatable3D](translatable3d.md)
  A set of methods that defines the interface to translate Spatial entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/volumetric)*