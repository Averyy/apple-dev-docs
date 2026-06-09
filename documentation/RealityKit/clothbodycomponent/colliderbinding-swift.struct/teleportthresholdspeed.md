# teleportThresholdSpeed

**Framework**: RealityKit  
**Kind**: property

The instantaneous collider speed (in m/s) over which the source collider will be considered to have teleported.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var teleportThresholdSpeed: Float { get set }
```

#### Discussion

If enabled, the distance limits will temporarily be overridden to 0 during the detection of a teleportation. This will effectively teleport the body together with the mesh collider. Particularly useful when resetting or looping an animation. Also helps the binding stay intact if the collider were to suddenly make a big jump due to a severe lag spike.

Only works if the mesh collider is animated by a visual mesh that has a skeleton. Must be non-negative; negative values are clamped to zero. The default value is `Float.infinity`, which disables teleport detection.

## See Also

- [var distanceLimits: PerClothVertexData<Float>](clothbodycomponent/colliderbinding-swift.struct/distancelimits.md)
  Distance limits (in meters) for how much each particle is allowed to deviate from its perfectly-bound position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/colliderbinding-swift.struct/teleportthresholdspeed)*