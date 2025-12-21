# init(scene:)

**Framework**: RealityKit  
**Kind**: init  
**Required**: Yes

Creates a new system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init(scene: Scene)
```

## Mentions

- [Implementing systems for entities in a scene](implementing-systems-for-entities-in-a-scene.md)

#### Discussion

There’s no need to instantiate your own systems, so don’t call this method. Instead, register your system with RealityKit by calling [`registerSystem()`](system/registersystem().md). RealityKit automatically creates an instance of every registered system for every scene.

## Parameters

- `scene`: The scene this system affects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/system/init(scene:))*