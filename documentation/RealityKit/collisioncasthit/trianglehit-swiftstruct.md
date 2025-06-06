# CollisionCastHit.TriangleHit

**Framework**: RealityKit  
**Kind**: struct

Information returned when ray intersects a triangle mesh.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct TriangleHit
```

## Topics

### Operators
- [static func == (CollisionCastHit.TriangleHit, CollisionCastHit.TriangleHit) -> Bool](collisioncasthit/trianglehit-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var faceIndex: Int](collisioncasthit/trianglehit-swift.struct/faceindex.md)
  The face index for the mesh face that that the ray hit.
- [var uv: SIMD2<Float>](collisioncasthit/trianglehit-swift.struct/uv.md)
  The barycentric uv coordinate for where in the triangle the ray hit.
### Default Implementations
- [Equatable Implementations](collisioncasthit/trianglehit-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct CollisionCastHit](collisioncasthit.md)
  A hit result of a collision cast.
- [enum CollisionCastQueryType](collisioncastquerytype.md)
  The kinds of ray and convex shape cast queries that you can make.
- [struct PixelCastHit](pixelcasthit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncasthit/trianglehit-swift.struct)*