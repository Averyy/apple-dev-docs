# position

**Framework**: RealityKit  
**Kind**: property

The position of the entity relative to its parent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var position: SIMD3<Float> { get set }
```

#### Discussion

This value is the entity’s position relative to its parent. To get the world-space position of the entity in the scene, use [`position(relativeTo:)`](hastransform/position(relativeto:).md), passing `nil` as the reference entity.

This is the same as the [`translation`](transform/translation.md) value on the [`transform`](hastransform/transform.md).

## See Also

- [func position(relativeTo: Entity?) -> SIMD3<Float>](hastransform/position(relativeto:).md)
  Gets the position of an entity relative to the given entity.
- [func setPosition(SIMD3<Float>, relativeTo: Entity?)](hastransform/setposition(_:relativeto:).md)
  Sets the position of the entity relative to the given reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/position)*