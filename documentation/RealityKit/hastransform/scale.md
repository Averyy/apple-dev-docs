# scale

**Framework**: RealityKit  
**Kind**: property

The scale of the entity relative to its parent.

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
@preconcurrency var scale: SIMD3<Float> { get set }
```

#### Discussion

This value is the entity’s scale relative to its parent. To get the actual scale of the entity in the scene, use [`scale(relativeTo:)`](hastransform/scale(relativeto:).md), passing `nil` as the reference entity.

This is the same as the [`scale`](transform/scale.md) value on the [`transform`](hastransform/transform.md).

## See Also

- [func scale(relativeTo: Entity?) -> SIMD3<Float>](hastransform/scale(relativeto:).md)
  Gets the scale of an entity relative to the given entity.
- [func setScale(SIMD3<Float>, relativeTo: Entity?)](hastransform/setscale(_:relativeto:).md)
  Sets the scale factor of the entity relative to the given reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/scale)*