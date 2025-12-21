# VolumetricProtocol

**Framework**: Spatial  
**Kind**: protocol

A set of methods for working with Spatial primitives with volume.

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
protocol VolumetricProtocol<Scalar> : SpatialTypeProtocol
```

## Topics

### Instance Properties
- [var size: Self.Size](volumetricprotocol/size.md)
  The size of the volume.
### Instance Methods
- [func contains(Self) -> Bool](volumetricprotocol/contains(_:).md)
  Returns a Boolean value that indicates whether the entity contains the specified volumetric entity.
- [func contains(anyOf: [Self.Point]) -> Bool](volumetricprotocol/contains(anyof:).md)
  Returns a Boolean value that indicates whether this volume contains any of the specified points.
- [func contains(point: Self.Point) -> Bool](volumetricprotocol/contains(point:).md)
  Returns a Boolean value that indicates whether this volume contains the specified point.
- [func formIntersection(Self)](volumetricprotocol/formintersection(_:).md)
  Sets the primitive to the intersection of itself and the specified primitive.
- [func formUnion(Self)](volumetricprotocol/formunion(_:).md)
  Sets the primitive to the union of itself and the specified primitive.
- [func intersection(Self) -> Self?](volumetricprotocol/intersection(_:).md)
  Returns the intersection of two volumetric entities.
- [func union(Self) -> Self](volumetricprotocol/union(_:).md)
  Returns the smallest volumetric entity that contains the two source entities.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
### Conforming Types
- [Rect3D](rect3d.md)
- [Rect3DFloat](rect3dfloat.md)
- [Size3D](size3d.md)
- [Size3DFloat](size3dfloat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/volumetricprotocol)*