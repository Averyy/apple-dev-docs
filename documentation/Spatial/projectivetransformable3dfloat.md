# ProjectiveTransformable3DFloat

**Framework**: Spatial  
**Kind**: protocol

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
protocol ProjectiveTransformable3DFloat : ProjectiveTransformable3D
```

## Topics

### Instance Methods
- [func applying(ProjectiveTransform3DFloat) -> Self](projectivetransformable3dfloat/applying(_:).md)
  Returns a transformed copy of the value

## Relationships

### Inherits From
- [ProjectiveTransformable3D](projectivetransformable3d.md)
### Conforming Types
- [Point3DFloat](point3dfloat.md)
- [Ray3DFloat](ray3dfloat.md)
- [Rect3DFloat](rect3dfloat.md)
- [Vector3DFloat](vector3dfloat.md)

## See Also

- [protocol CoordinateSpace3D](coordinatespace3d.md)
  A type that represents a coordinate space which you can use to convert values to and from other coordinate spaces.
- [protocol CoordinateSpace3DFloat](coordinatespace3dfloat.md)
- [protocol CoordinateSpaceValue3D](coordinatespacevalue3d.md)
  An opaque value which can be resolved to a concrete value in a `CoordinateSpace3D`
- [protocol ProjectiveTransformable3D](projectivetransformable3d.md)
- [struct WorldReferenceCoordinateSpace](worldreferencecoordinatespace.md)
  A coordinate space that represents a world reference point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransformable3dfloat)*