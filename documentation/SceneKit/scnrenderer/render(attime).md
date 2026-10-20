# render(atTime:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Renders the scene’s contents at the specified system time in the renderer’s OpenGL context.

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
func render(atTime time: CFTimeInterval)
```

```objc
- (void) renderAtTime:(CFTimeInterval) time;
```

#### Discussion

This method can be used only with an [`SCNRenderer`](../scnrenderer.md) object created with the [`SCNRenderer`](../scnrenderer.md) initializer. Call this method to tell SceneKit to draw the renderer’s scene into the OpenGL context you created the renderer with.

When you call this method, SceneKit updates its hierarchy of presentation nodes based on the specified timestamp, and then draws the scene.

> **Note**:  By default, the playback timing of actions and animations in a scene is based on the system time, not the scene time. Before using this method to control the playback of animations, set the [`usesSceneTimeBase`](../../QuartzCore/caanimation/usesscenetimebase.md) property of each animation to [`true`](../../Swift/true.md), or specify the [`playUsingSceneTimeBase`](../scnscenesource/animationimportpolicy/playusingscenetimebase.md) option when loading a scene file that contains animations.

## Parameters

- `time`: The timestamp, in seconds, at which to render the scene.

## See Also

### Rendering a Scene Using OpenGL
- [func render()](./render%28%29.md)
  Renders the scene’s contents in the renderer’s OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/render(attime:))*