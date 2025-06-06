# orientation

**Framework**: RealityKit  
**Kind**: property

The rotation of the entity relative to its parent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var orientation: simd_quatf { get set }
```

#### Discussion

This value is the entity’s rotation relative to its parent. To get the world-space orientation of the entity, use [`orientation(relativeTo:)`](hastransform/orientation(relativeto:).md), passing `nil` as the reference entity.

This is the same as the [`rotation`](transform/rotation.md) value on the [`transform`](hastransform/transform.md).

## See Also

- [func orientation(relativeTo: Entity?) -> simd_quatf](hastransform/orientation(relativeto:).md)
  Gets the orientation of an entity relative to the given entity.
- [func setOrientation(simd_quatf, relativeTo: Entity?)](hastransform/setorientation(_:relativeto:).md)
  Sets the orientation of the entity relative to the given reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/orientation)*