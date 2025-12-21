# position(relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Gets the position of an entity relative to the given entity.

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
@preconcurrency func position(relativeTo referenceEntity: Entity?) -> SIMD3<Float>
```

#### Return Value

The position of the entity relative to `referenceEntity`.

## Parameters

- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.

## See Also

- [var position: SIMD3<Float>](hastransform/position.md)
  The position of the entity relative to its parent.
- [func setPosition(SIMD3<Float>, relativeTo: Entity?)](hastransform/setposition(_:relativeto:).md)
  Sets the position of the entity relative to the given reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/position(relativeto:))*