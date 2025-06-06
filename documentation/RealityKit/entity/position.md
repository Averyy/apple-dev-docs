# position

**Framework**: RealityKit  
**Kind**: property

The position of the entity relative to its parent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var position: SIMD3<Float> { get set }
```

#### Discussion

This value is the entity’s position relative to its parent. To get the world-space position of the entity in the scene, use [`position(relativeTo:)`](hastransform/position(relativeto:).md), passing `nil` as the reference entity.

This is the same as the [`translation`](transform/translation.md) value on the [`transform`](hastransform/transform.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/position)*