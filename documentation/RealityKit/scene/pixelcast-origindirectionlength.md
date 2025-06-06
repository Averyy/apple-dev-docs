# pixelCast(origin:direction:length:)

**Framework**: RealityKit  
**Kind**: method

Performs a ray cast against all the geometry in the scene for a ray of a given origin, direction, and length.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
@MainActor
@preconcurrency func pixelCast(origin: SIMD3<Float>, direction: SIMD3<Float>, length: Float = 100) async throws -> PixelCastHit?
```

#### Return Value

A `PixelCastHit`. The hit indicates where the ray, starting at a given point and traveling in a given direction, hit a particular entity in the scene.

#### Discussion

The method ignores entities that lack a [`ModelComponent`](modelcomponent.md) with a valid mesh.

## Parameters

- `origin`: The origin of the ray relative to the scene.
- `direction`: The direction of the ray relative to the scene.
- `length`: The length of the ray relative to the scene.

## See Also

- [func raycast(origin: SIMD3<Float>, direction: SIMD3<Float>, length: Float, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](scene/raycast(origin:direction:length:query:mask:relativeto:).md)
  Performs a ray cast against all the geometry in the scene for a ray of a given origin, direction, and length.
- [func raycast(from: SIMD3<Float>, to: SIMD3<Float>, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](scene/raycast(from:to:query:mask:relativeto:).md)
  Performs a ray cast against all the geometry in the scene for a ray between two end points.
- [func convexCast(convexShape: ShapeResource, fromPosition: SIMD3<Float>, fromOrientation: simd_quatf, toPosition: SIMD3<Float>, toOrientation: simd_quatf, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](scene/convexcast(convexshape:fromposition:fromorientation:toposition:toorientation:query:mask:relativeto:).md)
  Performs a convex shape cast against all the geometry in the scene.
- [func pixelCast(from: SIMD3<Float>, to: SIMD3<Float>) async throws -> PixelCastHit?](scene/pixelcast(from:to:).md)
  Performs a ray cast against all the geometry in the scene for a ray between two end points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/pixelcast(origin:direction:length:))*