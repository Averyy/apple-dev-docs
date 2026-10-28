# nextFrameTime

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The timestamp for the next frame to be rendered.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var nextFrameTime: CFTimeInterval { get }
```

```objc
@property (nonatomic, readonly) CFTimeInterval nextFrameTime;
```

## Discussion

If the renderer’s scene has any attached actions or animations, use this property to determine how long your app should wait before telling the renderer to draw another frame. If this property’s value matches that of the renderer’s [`currentTime`](../scnscenerenderer/currenttime.md) property, the scene contains a continuous animation—schedule your next render at whatever time best maintains your app’s performance. If the value is infinite, the scene has no running actions or animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/nextframetime)*