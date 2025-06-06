# render(atTime:)

**Framework**: SceneKit  
**Kind**: method

Renders the scene’s contents at the specified system time in the renderer’s OpenGL context.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func render(atTime time: CFTimeInterval)
```

#### Discussion

This method can be used only with an [`SCNRenderer`](scnrenderer.md) object created with the [`SCNRenderer`](scnrenderer.md) initializer. Call this method to tell SceneKit to draw the renderer’s scene into the OpenGL context you created the renderer with.

When you call this method, SceneKit updates its hierarchy of presentation nodes based on the specified timestamp, and then draws the scene.

> **Note**:  By default, the playback timing of actions and animations in a scene is based on the system time, not the scene time. Before using this method to control the playback of animations, set the [`usesSceneTimeBase`](https://developer.apple.com/documentation/QuartzCore/CAAnimation/usesSceneTimeBase) property of each animation to [`true`](https://developer.apple.com/documentation/swift/true), or specify the [`playUsingSceneTimeBase`](scnscenesource/animationimportpolicy/playusingscenetimebase.md) option when loading a scene file that contains animations.

 By default, the playback timing of actions and animations in a scene is based on the system time, not the scene time. Before using this method to control the playback of animations, set the [`usesSceneTimeBase`](https://developer.apple.com/documentation/QuartzCore/CAAnimation/usesSceneTimeBase) property of each animation to [`true`](https://developer.apple.com/documentation/swift/true), or specify the [`playUsingSceneTimeBase`](scnscenesource/animationimportpolicy/playusingscenetimebase.md) option when loading a scene file that contains animations.

## Parameters

- `time`: The timestamp, in seconds, at which to render the scene.

## See Also

- [func render()](scnrenderer/render.md)
  Renders the scene’s contents in the renderer’s OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/render(attime:))*