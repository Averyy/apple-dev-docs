# falloffStart

**Framework**: RealityKit  
**Kind**: property

The depth (in meters) inside the volume at which the total force starts to linearly fall off.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var falloffStart: Float { get set }
```

#### Discussion

For particles whose depth is greater than or equal to `falloffStart`, the full force is applied. For shallower particles, the force ramps linearly from zero at the volume surface to the full force at `falloffStart`. Must be non-negative; negative values are clamped to zero. Zero by default, which means the total force is fully applied to all intersecting particles.

## See Also

- [var shape: ClothVolumeShape](clothforcevolumecomponent/shape.md)
  The shape of the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothforcevolumecomponent/falloffstart)*