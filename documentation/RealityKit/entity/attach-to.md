# attach(_:to:)

**Framework**: RealityKit  
**Kind**: method

Attach an entity to a target pin owned by another entity with an optional specified source pin This utility function has the same effect of adding an AttachedTransformComponent created with the same parameter to the entity you are calling upon

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
func attach(_ source: GeometricPin? = nil, to target: GeometricPin)
```

## Parameters

- `source`: The optional source pin existed on the current entity
- `target`: The target pin existed on the target entity


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/attach(_:to:))*