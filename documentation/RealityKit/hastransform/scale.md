# scale

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The scale of the entity relative to its parent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency var scale: SIMD3<Float> { get set }
```

## Mentions

- [Automatically animating RealityKit entities](../automatically-animating-realitykit-entities.md)

## Discussion

This value is the entity’s scale relative to its parent. To get the actual scale of the entity in the scene, use [`scale(relativeTo:)`](./scale%28relativeto%29.md), passing `nil` as the reference entity.

This is the same as the [`scale`](../transform/scale.md) value on the [`transform`](./transform.md).

## See Also

### Scaling an entity
- [func scale(relativeTo: Entity?) -> SIMD3<Float>](./scale%28relativeto%29.md)
  Gets the scale of an entity relative to the given entity.
- [func setScale(SIMD3<Float>, relativeTo: Entity?)](./setscale%28_,relativeto%29.md)
  Sets the scale factor of the entity relative to the given reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/scale)*