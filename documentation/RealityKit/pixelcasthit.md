# PixelCastHit

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
struct PixelCastHit
```

## Topics

### Instance Properties
- [var barycentric: SIMD3<Float>?](pixelcasthit/barycentric.md)
  The barycentric coordinate of the primitive. See the discussion of [[barycentric_coord]] in Section “5.2.3.4 Fragment Function Input Attributes” of Metal Shading Language Specification
- [var entity: Entity](pixelcasthit/entity.md)
  The entity that was hit.
- [var instance: UInt32](pixelcasthit/instance.md)
  The instance within the MeshResource of the intersection. This can be used to index into MeshResource.contents.instances
- [var meshPart: UInt64](pixelcasthit/meshpart.md)
  The mesh part id of the entity that was selected by the hit.
- [var normal: SIMD3<Float>](pixelcasthit/normal.md)
  The surface normal at the point of intersection, in scene space.
- [var position: SIMD3<Float>](pixelcasthit/position.md)
  The surface position at the point of intersection, in scene space.
- [var primitive: UInt32](pixelcasthit/primitive.md)
  The per-primitive identifier used with barycentric coordinates.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct QueryPredicate](querypredicate.md)
  An object that defines the criteria for an entity query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/pixelcasthit)*