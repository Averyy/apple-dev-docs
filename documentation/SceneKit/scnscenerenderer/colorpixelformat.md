# colorPixelFormat

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

The Metal pixel format for the renderer’s color output.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var colorPixelFormat: MTLPixelFormat { get }
```

#### Discussion

Use this property, along with the [`depthPixelFormat`](scnscenerenderer/depthpixelformat.md) and [`stencilPixelFormat`](scnscenerenderer/stencilpixelformat.md) properties, if you perform custom drawing with Metal (see the [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md) and [`SCNNodeRendererDelegate`](scnnoderendererdelegate.md) classes) and need to create a new [`MTLRenderPipelineState`](https://developer.apple.com/documentation/Metal/MTLRenderPipelineState) object to change the GPU state as part of your rendering.

> **Note**:  This property is valid only for scene renderers whose [`renderingAPI`](scnscenerenderer/renderingapi.md) value is [`SCNRenderingAPI.metal`](scnrenderingapi/metal.md). You create a SceneKit view that renders using Metal with the [`preferredRenderingAPI`](scnview/option/preferredrenderingapi.md) initialization option or in Interface Builder, or an [`SCNRenderer`](scnrenderer.md) that uses Metal with the [`init(device:options:)`](scnrenderer/init(device:options:).md) method. For OpenGL-based scene renderers, this property’s value is always `nil`.

 This property is valid only for scene renderers whose [`renderingAPI`](scnscenerenderer/renderingapi.md) value is [`SCNRenderingAPI.metal`](scnrenderingapi/metal.md). You create a SceneKit view that renders using Metal with the [`preferredRenderingAPI`](scnview/option/preferredrenderingapi.md) initialization option or in Interface Builder, or an [`SCNRenderer`](scnrenderer.md) that uses Metal with the [`init(device:options:)`](scnrenderer/init(device:options:).md) method. For OpenGL-based scene renderers, this property’s value is always `nil`.

## See Also

- [var currentRenderCommandEncoder: (any MTLRenderCommandEncoder)?](scnscenerenderer/currentrendercommandencoder.md)
  The Metal render command encoder in use for the current SceneKit rendering pass.
- [var device: (any MTLDevice)?](scnscenerenderer/device.md)
  The Metal device this renderer uses for rendering.
- [var commandQueue: (any MTLCommandQueue)?](scnscenerenderer/commandqueue.md)
  The Metal command queue this renderer uses for rendering.
- [var depthPixelFormat: MTLPixelFormat](scnscenerenderer/depthpixelformat.md)
  The Metal pixel format for the renderer’s depth buffer.
- [var stencilPixelFormat: MTLPixelFormat](scnscenerenderer/stencilpixelformat.md)
  The Metal pixel format for the renderer’s stencil buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/colorpixelformat)*