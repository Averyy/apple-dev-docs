# setScale(_:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Sets the scale factor of the entity relative to the given reference entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func setScale(_ scale: SIMD3<Float>, relativeTo referenceEntity: Entity?)
```

## Parameters

- `scale`: A new scale factor, relative to  .
- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/setscale(_:relativeto:))*