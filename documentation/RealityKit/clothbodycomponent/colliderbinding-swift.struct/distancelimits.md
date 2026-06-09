# distanceLimits

**Framework**: RealityKit  
**Kind**: property

Distance limits (in meters) for how much each particle is allowed to deviate from its perfectly-bound position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var distanceLimits: PerClothVertexData<Float>
```

#### Discussion

Each value must be non-negative. A value of 0 makes the particle fully bound to its assigned triangle in the source collider. A value of `Float.infinity` allows the particle to move completely free, as if no binding was happening.

## See Also

- [var teleportThresholdSpeed: Float](clothbodycomponent/colliderbinding-swift.struct/teleportthresholdspeed.md)
  The instantaneous collider speed (in m/s) over which the source collider will be considered to have teleported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/colliderbinding-swift.struct/distancelimits)*