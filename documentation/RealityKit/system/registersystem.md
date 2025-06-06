# registerSystem()

**Framework**: RealityKit  
**Kind**: method

Registers a system with RealityKit.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func registerSystem()
```

## Mentions

- [Implementing systems for entities in a scene](implementing-systems-for-entities-in-a-scene.md)

#### Discussion

Calling this method informs RealityKit of a system of defined behavior for its scenes. RealityKit automatically creates an instance of all registered systems for every scene and calls every registered system’s [`update(context:)`](system/update(context:)-3d0qz.md) method on every scene update.

If you call [`registerSystem()`](system/registersystem().md) multiple times, RealityKit ignores additional calls after the first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/system/registersystem())*