# position

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The position of the entity relative to its parent.

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
@preconcurrency var position: SIMD3<Float> { get set }
```

## Mentions

- [Automatically animating RealityKit entities](../automatically-animating-realitykit-entities.md)

## Discussion

This value is the entity’s position relative to its parent. To get the world-space position of the entity in the scene, use [`position(relativeTo:)`](./position%28relativeto%29.md), passing `nil` as the reference entity.

This is the same as the [`translation`](../transform/translation.md) value on the [`transform`](./transform.md).

## See Also

### Positioning an entity
- [func position(relativeTo: Entity?) -> SIMD3<Float>](./position%28relativeto%29.md)
  Gets the position of an entity relative to the given entity.
- [func setPosition(SIMD3<Float>, relativeTo: Entity?)](./setposition%28_,relativeto%29.md)
  Sets the position of the entity relative to the given reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/position)*