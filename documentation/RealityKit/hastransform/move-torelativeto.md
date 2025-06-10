# move(to:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Moves an entity instantly to a new location given by a transform.

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
@preconcurrency func move(to transform: Transform, relativeTo referenceEntity: Entity?)
```

## Parameters

- `transform`: A   instance that indicates the new location.
- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/move(to:relativeto:))*