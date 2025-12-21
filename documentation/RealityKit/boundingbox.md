# BoundingBox

**Framework**: RealityKit  
**Kind**: struct

An axis-aligned bounding box (AABB).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@frozen
struct BoundingBox
```

## Topics

### Creating a bounding box
- [init()](boundingbox/init.md)
  Creates an empty bounding box.
- [init(min: SIMD3<Float>, max: SIMD3<Float>)](boundingbox/init(min:max:).md)
  Creates a bounding box with the given settings.
### Getting an empty box
- [static let empty: BoundingBox](boundingbox/empty.md)
  An empty bounding box.
- [var isEmpty: Bool](boundingbox/isempty.md)
  A Boolean that indicates whether the bounding box is empty.
### Getting the box characteristics
- [var max: SIMD3<Float>](boundingbox/max.md)
  The position of the maximum corner of the box.
- [var min: SIMD3<Float>](boundingbox/min.md)
  The position of the minimum corner of the box.
- [var center: SIMD3<Float>](boundingbox/center.md)
  The center of the bounding box.
- [var extents: SIMD3<Float>](boundingbox/extents.md)
  The extents of the bounding box.
- [var boundingRadius: Float](boundingbox/boundingradius.md)
  The radius of a bounding sphere that encompasses the bounding box.
### Expanding boxes
- [func union(BoundingBox) -> BoundingBox](boundingbox/union(_:)-1y8hw.md)
  Creates a bounding box containing the current bounds and the specified bounds.
- [func formUnion(BoundingBox)](boundingbox/formunion(_:)-5iy03.md)
  Expands the bounding box to contain the specified bounds.
- [func union(SIMD3<Float>) -> BoundingBox](boundingbox/union(_:)-g4th.md)
  Creates a bounding box containing the current bounds and the specified point.
- [func formUnion(SIMD3<Float>)](boundingbox/formunion(_:)-6itj9.md)
  Expands the bounding box to contain the specified point.
### Checking for overlap
- [func contains(BoundingBox) -> Bool](boundingbox/contains(_:)-5ux4h.md)
  Checks whether the bounding box contains the specified bounds.
- [func contains(SIMD3<Float>) -> Bool](boundingbox/contains(_:)-92ap6.md)
  Checks whether the bounding box contains the specified point.
- [func intersects(BoundingBox) -> Bool](boundingbox/intersects(_:).md)
  Checks whether the bounding box intersects the specified bounds.
### Checking for separation
- [func distanceSquared(toPoint: SIMD3<Float>) -> Float](boundingbox/distancesquared(topoint:).md)
  Calculates the distance from a point to the bounding box.
### Transforming a bounding box
- [func transform(by: float4x4)](boundingbox/transform(by:).md)
  Transforms the bounding box.
- [func transformed(by: float4x4) -> BoundingBox](boundingbox/transformed(by:).md)
  Transforms the bounding box and finds the bounds of the result.
### Comparing bounding boxes
- [static func == (BoundingBox, BoundingBox) -> Bool](boundingbox/==(_:_:).md)
  Indicates whether two bounding boxes are equal.
- [func hash(into: inout Hasher)](boundingbox/hash(into:).md)
  Hashes the essential components of the bounding box by feeding them into the given hash function.
### Initializers
- [init(Rect3D)](boundingbox/init(_:).md)
### Instance Methods
- [func contains(_:)](boundingbox/contains(_:).md)
  Checks whether the bounding box contains the specified bounds.
- [func formUnion(_:)](boundingbox/formunion(_:).md)
  Expands the bounding box to contain the specified bounds.
- [func union(_:)](boundingbox/union(_:).md)
  Creates a bounding box containing the current bounds and the specified bounds.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct OrientedBoundingBox](orientedboundingbox.md)
  Representation for an oriented bounding box. Uses a combination of an axis-aligned bounding box and a rotation vector around the centroid of the said axis-aligned bounding box to represent an oriented bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox)*