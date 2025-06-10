# raycast(from:to:query:mask:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Performs a ray cast against all the geometry in the scene for a ray between two end points.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func raycast(from startPosition: SIMD3<Float>, to endPosition: SIMD3<Float>, query: CollisionCastQueryType = .all, mask: CollisionGroup = .all, relativeTo referenceEntity: Entity? = nil) -> [CollisionCastHit]
```

#### Return Value

An array of collision cast hit results. Each hit indicates where the ray, starting at `startPosition` and ending at `endPosition`, hit a particular entity in the scene.

#### Discussion

The method ignores entities that lack a [`CollisionComponent`](collisioncomponent.md).

The [`normal`](collisioncasthit/normal.md) property on returned result objects contains the surface normal at the point of intersection with the entity’s collision shape.

The following are some details to keep in mind.

- The ray needs to fully intersect a primitive for a hit to be detected. In particular, it is not enough for the ray to precisely tangent or end at the primitive’s surface. This becomes especially important when ray casting against primitives that are far away from the ray origin.
- Due to numerical imprecision, it may be necessary to use a slightly longer ray length than your desired maximum distance in order to ensure that a full intersection occurs with your target primitive. Moreover, the length of the ray needs to be a positive finite number that is smaller than `greatestFiniteMagnitude`.

## Parameters

- `startPosition`: The start position of the ray relative to   .
- `endPosition`: The end position of the ray relative to   .
- `query`: A query type.
- `mask`: A collision mask that you can use to prevent collisions with   certain objects.
- `referenceEntity`: An entity that defines the frame of reference. The   method returns results relative to this entity. Set to   to use the   world space origin  .

## See Also

- [func raycast(origin: SIMD3<Float>, direction: SIMD3<Float>, length: Float, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](scene/raycast(origin:direction:length:query:mask:relativeto:).md)
  Performs a ray cast against all the geometry in the scene for a ray of a given origin, direction, and length.
- [func convexCast(convexShape: ShapeResource, fromPosition: SIMD3<Float>, fromOrientation: simd_quatf, toPosition: SIMD3<Float>, toOrientation: simd_quatf, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](scene/convexcast(convexshape:fromposition:fromorientation:toposition:toorientation:query:mask:relativeto:).md)
  Performs a convex shape cast against all the geometry in the scene.
- [func pixelCast(from:to:)](scene/pixelcast(from:to:).md)
  Performs a ray cast against all the geometry in the scene for a ray between two end points.
- [func pixelCast(origin:direction:length:)](scene/pixelcast(origin:direction:length:).md)
  Performs a ray cast against all the geometry in the scene for a ray of a given origin, direction, and length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/raycast(from:to:query:mask:relativeto:))*