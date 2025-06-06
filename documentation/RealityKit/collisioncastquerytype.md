# CollisionCastQueryType

**Framework**: RealityKit  
**Kind**: enum

The kinds of ray and convex shape cast queries that you can make.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
enum CollisionCastQueryType
```

## Topics

### Collision cast queries
- [CollisionCastQueryType.nearest](collisioncastquerytype/nearest.md)
  Report the closest hit.
- [CollisionCastQueryType.all](collisioncastquerytype/all.md)
  Report all hits sorted in ascending order by distance from the cast origin.
- [CollisionCastQueryType.any](collisioncastquerytype/any.md)
  Report one hit.
### Comparing collision cast queries
- [static func == (CollisionCastQueryType, CollisionCastQueryType) -> Bool](collisioncastquerytype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](collisioncastquerytype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](collisioncastquerytype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](collisioncastquerytype/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](collisioncastquerytype/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct CollisionCastHit](collisioncasthit.md)
  A hit result of a collision cast.
- [CollisionCastHit.TriangleHit](collisioncasthit/trianglehit-swift.struct.md)
  Information returned when ray intersects a triangle mesh.
- [struct PixelCastHit](pixelcasthit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncastquerytype)*