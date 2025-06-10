# CoordinateSpace3D

**Framework**: Spatial  
**Kind**: protocol

A type that represents a coordinate space which you can use to convert values to and from other coordinate spaces.

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
protocol CoordinateSpace3D
```

## Topics

### Associated Types
- [associatedtype AncestorCoordinateSpace : CoordinateSpace3D](coordinatespace3d/ancestorcoordinatespace.md)
### Instance Properties
- [var ancestorSpace: Self.AncestorCoordinateSpace?](coordinatespace3d/ancestorspace.md)
  An ancestor coordinate space.
- [var coordinateSpaceID: String?](coordinatespace3d/coordinatespaceid.md)
  The identifier for this space.
### Instance Methods
- [func ancestorFromSpaceTransform() throws -> ProjectiveTransform3D](coordinatespace3d/ancestorfromspacetransform.md)
  This space’s transform relative to its ancestor.
- [func convert<T>(value: T, from: Self) throws -> T](coordinatespace3d/convert(value:from:)-3zi9f.md)
  Converts a value from a source coordinate space to this one.
- [func convert<T, Space>(value: T, from: Space) throws -> T](coordinatespace3d/convert(value:from:)-7og5p.md)
  Converts a value from a source coordinate space to this one.
- [func convert<T, Space>(value: T, to: Space) throws -> T](coordinatespace3d/convert(value:to:)-2i668.md)
  Converts a value from this coordinate space to another.
- [func convert<T>(value: T, to: Self) throws -> T](coordinatespace3d/convert(value:to:)-u2a0.md)
  Converts a value from this coordinate space to another.
- [func transform(from: Self) throws -> ProjectiveTransform3D](coordinatespace3d/transform(from:).md)
  Returns a transform of this coordinate space from the target coordinate space.
- [func transformSpace((Self) -> ProjectiveTransform3D) -> some CoordinateSpace3D](coordinatespace3d/transformspace(_:).md)
  Returns a modified version of the coordinate space.
### Type Properties
- [static var worldReference: WorldReferenceCoordinateSpace](coordinatespace3d/worldreference.md)
  A coordinate space that represents the world root for all other coordinate spaces.

## Relationships

### Inherited By
- [CoordinateSpace3DFloat](coordinatespace3dfloat.md)
### Conforming Types
- [WorldReferenceCoordinateSpace](worldreferencecoordinatespace.md)

## See Also

- [protocol CoordinateSpace3DFloat](coordinatespace3dfloat.md)
- [protocol CoordinateSpaceValue3D](coordinatespacevalue3d.md)
  An opaque value which can be resolved to a concrete value in a `CoordinateSpace3D`
- [protocol ProjectiveTransformable3D](projectivetransformable3d.md)
- [protocol ProjectiveTransformable3DFloat](projectivetransformable3dfloat.md)
- [struct WorldReferenceCoordinateSpace](worldreferencecoordinatespace.md)
  A coordinate space that represents a world reference point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespace3d)*