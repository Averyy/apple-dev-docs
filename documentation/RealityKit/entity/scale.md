# scale

**Framework**: RealityKit  
**Kind**: property

The scale of the entity relative to its parent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var scale: SIMD3<Float> { get set }
```

#### Discussion

This value is the entity’s scale relative to its parent. To get the actual scale of the entity in the scene, use [`scale(relativeTo:)`](hastransform/scale(relativeto:).md), passing `nil` as the reference entity.

This is the same as the [`scale`](transform/scale.md) value on the [`transform`](hastransform/transform.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/scale)*