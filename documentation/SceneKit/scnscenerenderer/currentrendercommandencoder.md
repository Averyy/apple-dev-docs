# currentRenderCommandEncoder

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

The Metal render command encoder in use for the current SceneKit rendering pass.

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
var currentRenderCommandEncoder: (any MTLRenderCommandEncoder)? { get }
```

#### Discussion

Use this render command encoder to encode additional rendering commands before or after SceneKit draws its own content.

This property is valid only during the SceneKit rendering loop—that is, within one of the methods defined in the [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md) protocol. Accessing this property at any other time returns `nil`.

## See Also

- [var device: (any MTLDevice)?](scnscenerenderer/device.md)
  The Metal device this renderer uses for rendering.
- [var commandQueue: (any MTLCommandQueue)?](scnscenerenderer/commandqueue.md)
  The Metal command queue this renderer uses for rendering.
- [var colorPixelFormat: MTLPixelFormat](scnscenerenderer/colorpixelformat.md)
  The Metal pixel format for the renderer’s color output.
- [var depthPixelFormat: MTLPixelFormat](scnscenerenderer/depthpixelformat.md)
  The Metal pixel format for the renderer’s depth buffer.
- [var stencilPixelFormat: MTLPixelFormat](scnscenerenderer/stencilpixelformat.md)
  The Metal pixel format for the renderer’s stencil buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/currentrendercommandencoder)*