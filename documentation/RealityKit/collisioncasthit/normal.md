# normal

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The normal of the hit.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var normal: SIMD3<Float> { get }
```

## Discussion

The frame of reference for this point depends on the reference entity used in the call to either the [`raycast(origin:direction:length:query:mask:relativeTo:)`](../scene/raycast%28origin,direction,length,query,mask,relativeto%29.md) method or the [`convexCast(convexShape:fromPosition:fromOrientation:toPosition:toOrientation:query:mask:relativeTo:)`](../scene/convexcast%28convexshape,fromposition,fromorientation,toposition,toorientation,query,mask,relativeto%29.md) method that generated the hit.

## See Also

### Characterizing the collision cast hit
- [var position: SIMD3<Float>](./position.md)
  The position of the hit.
- [var distance: Float](./distance.md)
  The distance from the ray origin to the hit, or the convex shape travel distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncasthit/normal)*