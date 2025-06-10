# setPosition(_:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Sets the position of the entity relative to the given reference entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func setPosition(_ position: SIMD3<Float>, relativeTo referenceEntity: Entity?)
```

## Parameters

- `position`: A new position, relative to  .
- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.

## See Also

- [var position: SIMD3<Float>](hastransform/position.md)
  The position of the entity relative to its parent.
- [func position(relativeTo: Entity?) -> SIMD3<Float>](hastransform/position(relativeto:).md)
  Gets the position of an entity relative to the given entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/setposition(_:relativeto:))*