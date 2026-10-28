# position(relativeTo:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Gets the position of an entity relative to the given entity.

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
@preconcurrency func position(relativeTo referenceEntity: Entity?) -> SIMD3<Float>
```

## Return Value

The position of the entity relative to `referenceEntity`.

## Parameters

- `referenceEntity`: The entity that defines a frame of reference. Set this to `nil` to indicate world space.

## See Also

### Positioning an entity
- [var position: SIMD3<Float>](./position.md)
  The position of the entity relative to its parent.
- [func setPosition(SIMD3<Float>, relativeTo: Entity?)](./setposition%28_,relativeto%29.md)
  Sets the position of the entity relative to the given reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/position(relativeto:))*