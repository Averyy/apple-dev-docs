# render(atTime:viewport:commandBuffer:passDescriptor:)

**Framework**: SceneKit  
**Kind**: method

Renders the scene’s contents at the specified system time in the specified Metal command buffer.

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
func render(atTime time: CFTimeInterval, viewport: CGRect, commandBuffer: any MTLCommandBuffer, passDescriptor renderPassDescriptor: MTLRenderPassDescriptor)
```

#### Discussion

This method can be used only with an [`SCNRenderer`](scnrenderer.md) object created with the [`SCNRenderer`](scnrenderer.md) initializer. Call this method to tell SceneKit to draw the renderer’s scene into the render target described by the `renderPassDescriptor` parameter, by encoding render commands into the `commandBuffer` parameter.

When you call this method, SceneKit updates its hierarchy of presentation nodes based on the specified timestamp, and then draws the scene using the specified Metal objects.

> **Note**:  By default, the playback timing of actions and animations in a scene is based on the system time, not the scene time. Before using this method to control the playback of animations, set the [`usesSceneTimeBase`](https://developer.apple.com/documentation/QuartzCore/CAAnimation/usesSceneTimeBase) property of each animation to [`true`](https://developer.apple.com/documentation/swift/true), or specify the [`playUsingSceneTimeBase`](scnscenesource/animationimportpolicy/playusingscenetimebase.md) option when loading a scene file that contains animations.

## Parameters

- `time`: The timestamp, in seconds, at which to render the scene.
- `viewport`: The pixel dimensions in which to render.
- `commandBuffer`: The Metal command buffer in which SceneKit should schedule rendering commands.
- `renderPassDescriptor`: The Metal render pass descriptor describing the rendering target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/render(attime:viewport:commandbuffer:passdescriptor:))*