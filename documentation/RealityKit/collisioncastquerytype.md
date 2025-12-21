# CollisionCastQueryType

**Framework**: RealityKit  
**Kind**: enum

The kinds of ray and convex shape cast queries that you can make.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
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