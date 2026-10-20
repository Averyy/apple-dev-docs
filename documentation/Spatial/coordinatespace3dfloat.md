# CoordinateSpace3DFloat

**Framework**: Spatial  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol CoordinateSpace3DFloat : CoordinateSpace3D where Self.AncestorCoordinateSpace : CoordinateSpace3DFloat
```

## Topics

### Instance Methods
- [func ancestorFromSpaceTransformFloat() throws -> ProjectiveTransform3DFloat](./coordinatespace3dfloat/ancestorfromspacetransformfloat%28%29.md)
- [func convert<T, Space>(value: T, from: Space) throws -> T](./coordinatespace3dfloat/convert%28value,from%29.md)
  Converts a value from a source coordinate space to this one.
- [func convert<T, Space>(value: T, to: Space) throws -> T](./coordinatespace3dfloat/convert%28value,to%29.md)
  Converts a value from this coordinate space to another.
- [func transformSpace((Self) -> ProjectiveTransform3DFloat) -> some CoordinateSpace3DFloat](./coordinatespace3dfloat/transformspace%28_%29.md)
  Returns a modified version of the coordinate space.

## Relationships

### Inherits From
- [CoordinateSpace3D](./coordinatespace3d.md)
### Conforming Types
- [WorldReferenceCoordinateSpace](./worldreferencecoordinatespace.md)

## See Also

### Converting between coordinate spaces
- [protocol CoordinateSpace3D](./coordinatespace3d.md)
  A type that represents a coordinate space which you can use to convert values to and from other coordinate spaces.
- [protocol CoordinateSpaceValue3D](./coordinatespacevalue3d.md)
  An opaque value which can be resolved to a concrete value in a `CoordinateSpace3D`
- [protocol ProjectiveTransformable3D](./projectivetransformable3d.md)
- [protocol ProjectiveTransformable3DFloat](./projectivetransformable3dfloat.md)
- [struct WorldReferenceCoordinateSpace](./worldreferencecoordinatespace.md)
  A coordinate space that represents a world reference point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespace3dfloat)*