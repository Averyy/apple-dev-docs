# pixelCast(from:to:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Performs a ray cast against all the geometry in the scene for a ray between two end points.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func pixelCast(from startPosition: SIMD3<Float>, to endPosition: SIMD3<Float>) async throws -> PixelCastHit?
```

#### Return Value

A `PixelCastHit`. The hit indicates where the ray, starting at `startPosition` and ending at `endPosition`, hit a particular entity in the scene.

#### Discussion

The method ignores entities that lack a [`ModelComponent`](../modelcomponent.md) with a valid mesh.

## Parameters

- `startPosition`: The start position of the ray relative to the scene.
- `endPosition`: The end position of the ray relative to the scene.

## See Also

### Detecting intersections
- [func raycast(origin: SIMD3<Float>, direction: SIMD3<Float>, length: Float, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](./raycast%28origin,direction,length,query,mask,relativeto%29.md)
  Performs a ray cast against all the geometry in the scene for a ray of a given origin, direction, and length.
- [func raycast(from: SIMD3<Float>, to: SIMD3<Float>, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](./raycast%28from,to,query,mask,relativeto%29.md)
  Performs a ray cast against all the geometry in the scene for a ray between two end points.
- [func convexCast(convexShape: ShapeResource, fromPosition: SIMD3<Float>, fromOrientation: simd_quatf, toPosition: SIMD3<Float>, toOrientation: simd_quatf, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](./convexcast%28convexshape,fromposition,fromorientation,toposition,toorientation,query,mask,relativeto%29.md)
  Performs a convex shape cast against all the geometry in the scene.
- [func pixelCast(origin: SIMD3<Float>, direction: SIMD3<Float>, length: Float) async throws -> PixelCastHit?](./pixelcast%28origin,direction,length%29.md)
  Performs a ray cast against all the geometry in the scene for a ray of a given origin, direction, and length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/pixelcast(from:to:))*