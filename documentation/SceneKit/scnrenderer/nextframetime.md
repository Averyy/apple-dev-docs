# nextFrameTime

**Framework**: SceneKit  
**Kind**: property

The timestamp for the next frame to be rendered.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var nextFrameTime: CFTimeInterval { get }
```

#### Discussion

If the renderer’s scene has any attached actions or animations, use this property to determine how long your app should wait before telling the renderer to draw another frame. If this property’s value matches that of the renderer’s [`currentTime`](scnscenerenderer/currenttime.md) property, the scene contains a continuous animation—schedule your next render at whatever time best maintains your app’s performance. If the value is infinite, the scene has no running actions or animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/nextframetime)*