# position

**Framework**: RealityKit  
**Kind**: property

The position of the hit.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var position: SIMD3<Float> { get }
```

#### Discussion

The frame of reference for this point depends on the reference entity used in the call to either the [`raycast(origin:direction:length:query:mask:relativeTo:)`](scene/raycast(origin:direction:length:query:mask:relativeto:).md) method or the [`convexCast(convexShape:fromPosition:fromOrientation:toPosition:toOrientation:query:mask:relativeTo:)`](scene/convexcast(convexshape:fromposition:fromorientation:toposition:toorientation:query:mask:relativeto:).md) method that generated the hit.

## See Also

- [var normal: SIMD3<Float>](collisioncasthit/normal.md)
  The normal of the hit.
- [var distance: Float](collisioncasthit/distance.md)
  The distance from the ray origin to the hit, or the convex shape travel distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncasthit/position)*