# CollisionCastHit

**Framework**: RealityKit  
**Kind**: struct

A hit result of a collision cast.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct CollisionCastHit
```

#### Overview

You get a collection of collision cast hits from either the [`raycast(origin:direction:length:query:mask:relativeTo:)`](scene/raycast(origin:direction:length:query:mask:relativeto:).md) method, or the [`convexCast(convexShape:fromPosition:fromOrientation:toPosition:toOrientation:query:mask:relativeTo:)`](scene/convexcast(convexshape:fromposition:fromorientation:toposition:toorientation:query:mask:relativeto:).md) method. Each hit indicates where the ray or the convex shape, starting at a given point and traveling in a given direction, hit a particular entity in the scene.

The frame of reference for the position and normal of the hit depends on the reference entity parameter passed to the method that generated the hit. Pass `nil` as the reference to use world space.

## Topics

### Getting the entity
- [var entity: Entity](collisioncasthit/entity.md)
  The entity that was hit.
### Characterizing the collision cast hit
- [var position: SIMD3<Float>](collisioncasthit/position.md)
  The position of the hit.
- [var normal: SIMD3<Float>](collisioncasthit/normal.md)
  The normal of the hit.
- [var distance: Float](collisioncasthit/distance.md)
  The distance from the ray origin to the hit, or the convex shape travel distance.
### Comparing collision cast hits
- [static func == (CollisionCastHit, CollisionCastHit) -> Bool](collisioncasthit/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](collisioncasthit/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Structures
- [CollisionCastHit.TriangleHit](collisioncasthit/trianglehit-swift.struct.md)
  Information returned when ray intersects a triangle mesh.
### Instance Properties
- [var shapeIndex: Int](collisioncasthit/shapeindex.md)
  The index of the shape that was hit.
- [var triangleHit: CollisionCastHit.TriangleHit?](collisioncasthit/trianglehit-swift.property.md)
  Information the system provides when a ray touches or intersects a triangle mesh.
### Default Implementations
- [Equatable Implementations](collisioncasthit/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [CollisionCastHit.TriangleHit](collisioncasthit/trianglehit-swift.struct.md)
  Information returned when ray intersects a triangle mesh.
- [enum CollisionCastQueryType](collisioncastquerytype.md)
  The kinds of ray and convex shape cast queries that you can make.
- [struct PixelCastHit](pixelcasthit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncasthit)*