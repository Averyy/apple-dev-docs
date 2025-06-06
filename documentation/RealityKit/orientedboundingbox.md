# OrientedBoundingBox

**Framework**: RealityKit  
**Kind**: struct

Representation for an oriented bounding box. Uses a combination of an axis-aligned bounding box and a rotation vector around the centroid of the said axis-aligned bounding box to represent an oriented bounding box.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
struct OrientedBoundingBox
```

## Topics

### Operators
- [static func == (OrientedBoundingBox, OrientedBoundingBox) -> Bool](orientedboundingbox/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(orientation: simd_quatf, boundingBox: BoundingBox)](orientedboundingbox/init(orientation:boundingbox:).md)
### Instance Properties
- [var boundingBox: BoundingBox](orientedboundingbox/boundingbox.md)
  Axis aligned bounding box
- [var hashValue: Int](orientedboundingbox/hashvalue.md)
  The hash value.
- [var orientation: simd_quatf](orientedboundingbox/orientation.md)
  Orientation (rotation) of the bounding box
### Instance Methods
- [func hash(into: inout Hasher)](orientedboundingbox/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](orientedboundingbox/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct BoundingBox](boundingbox.md)
  An axis-aligned bounding box (AABB).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orientedboundingbox)*