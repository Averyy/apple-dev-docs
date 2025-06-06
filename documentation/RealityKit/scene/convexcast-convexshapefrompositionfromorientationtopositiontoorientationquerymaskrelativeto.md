# convexCast(convexShape:fromPosition:fromOrientation:toPosition:toOrientation:query:mask:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Performs a convex shape cast against all the geometry in the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func convexCast(convexShape: ShapeResource, fromPosition: SIMD3<Float>, fromOrientation: simd_quatf, toPosition: SIMD3<Float>, toOrientation: simd_quatf, query: CollisionCastQueryType = .all, mask: CollisionGroup = .all, relativeTo referenceEntity: Entity? = nil) -> [CollisionCastHit]
```

#### Return Value

An array of collision cast hit results. Each hit indicates where the convex shape, starting at a given point and traveling in a given direction, collides with entities in the scene. To retrieve the hit entity from a returned [`CollisionCastHit`](collisioncasthit.md), use the [`entity`](collisioncasthit/entity.md) property.

#### Discussion

For objects that intersect the convex shape at its starting position and orientation, the returned collision cast hit result’s [`position`](collisioncasthit/position.md) is `(0, 0, 0)` and the [`normal`](collisioncasthit/normal.md) points in the opposite direction of the sweep.

## Parameters

- `convexShape`: The convex shape to cast.
- `fromPosition`: The starting position of   relative to   .
- `fromOrientation`: The starting orientation of   relative to   .
- `toPosition`: The ending position of   relative to   .
- `toOrientation`: The ending orientation of   relative to   .
- `query`: The query type.
- `mask`: A collision mask that you can use to prevent collisions with   certain objects.
- `referenceEntity`: An entity that defines the frame of reference. The   method returns results relative to this entity. Set to   to use the   world space origin  .

## See Also

- [func raycast(origin: SIMD3<Float>, direction: SIMD3<Float>, length: Float, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](scene/raycast(origin:direction:length:query:mask:relativeto:).md)
  Performs a ray cast against all the geometry in the scene for a ray of a given origin, direction, and length.
- [func raycast(from: SIMD3<Float>, to: SIMD3<Float>, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](scene/raycast(from:to:query:mask:relativeto:).md)
  Performs a ray cast against all the geometry in the scene for a ray between two end points.
- [func pixelCast(from: SIMD3<Float>, to: SIMD3<Float>) async throws -> PixelCastHit?](scene/pixelcast(from:to:).md)
  Performs a ray cast against all the geometry in the scene for a ray between two end points.
- [func pixelCast(origin: SIMD3<Float>, direction: SIMD3<Float>, length: Float) async throws -> PixelCastHit?](scene/pixelcast(origin:direction:length:).md)
  Performs a ray cast against all the geometry in the scene for a ray of a given origin, direction, and length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/convexcast(convexshape:fromposition:fromorientation:toposition:toorientation:query:mask:relativeto:))*