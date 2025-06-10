# CoordinateSpaceValue3D

**Framework**: Spatial  
**Kind**: protocol

An opaque value which can be resolved to a concrete value in a `CoordinateSpace3D`

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
protocol CoordinateSpaceValue3D<Value>
```

## Topics

### Associated Types
- [associatedtype Value : ProjectiveTransformable3D](coordinatespacevalue3d/value.md)
### Instance Methods
- [func resolve<Space>(in: Space) throws -> Self.Value](coordinatespacevalue3d/resolve(in:).md)
  Resolves the associated value in the given coordinate space.

## See Also

- [protocol CoordinateSpace3D](coordinatespace3d.md)
  A type that represents a coordinate space which you can use to convert values to and from other coordinate spaces.
- [protocol CoordinateSpace3DFloat](coordinatespace3dfloat.md)
- [protocol ProjectiveTransformable3D](projectivetransformable3d.md)
- [protocol ProjectiveTransformable3DFloat](projectivetransformable3dfloat.md)
- [struct WorldReferenceCoordinateSpace](worldreferencecoordinatespace.md)
  A coordinate space that represents a world reference point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespacevalue3d)*