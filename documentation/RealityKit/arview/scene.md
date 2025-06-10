# scene

**Framework**: RealityKit  
**Kind**: property

The scene that the view renders and simulates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var scene: Scene { get }
```

#### Discussion

When you initialize a view, it comes with a single [`Scene`](scene.md) instance that you access through the view’s [`scene`](arview/scene.md) property. Add [`AnchorEntity`](anchorentity.md) instances to the scene’s [`anchors`](scene/anchors.md) collection to provide content for the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/scene)*