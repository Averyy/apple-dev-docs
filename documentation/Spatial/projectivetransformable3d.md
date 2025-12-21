# ProjectiveTransformable3D

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
protocol ProjectiveTransformable3D
```

## Topics

### Instance Methods
- [func applying(ProjectiveTransform3D) -> Self](projectivetransformable3d/applying(_:).md)
  Returns a transformed copy of the value.

## Relationships

### Inherited By
- [ProjectiveTransformable3DFloat](projectivetransformable3dfloat.md)
### Conforming Types
- [Point3D](point3d.md)
- [Point3DFloat](point3dfloat.md)
- [Ray3D](ray3d.md)
- [Ray3DFloat](ray3dfloat.md)
- [Rect3D](rect3d.md)
- [Rect3DFloat](rect3dfloat.md)
- [Vector3D](vector3d.md)
- [Vector3DFloat](vector3dfloat.md)

## See Also

- [protocol CoordinateSpace3D](coordinatespace3d.md)
  A type that represents a coordinate space which you can use to convert values to and from other coordinate spaces.
- [protocol CoordinateSpace3DFloat](coordinatespace3dfloat.md)
- [protocol CoordinateSpaceValue3D](coordinatespacevalue3d.md)
  An opaque value which can be resolved to a concrete value in a `CoordinateSpace3D`
- [protocol ProjectiveTransformable3DFloat](projectivetransformable3dfloat.md)
- [struct WorldReferenceCoordinateSpace](worldreferencecoordinatespace.md)
  A coordinate space that represents a world reference point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransformable3d)*