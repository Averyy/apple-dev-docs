# commandQueue

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

The Metal command queue this renderer uses for rendering.

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
var commandQueue: (any MTLCommandQueue)? { get }
```

#### Discussion

Use this property to schedule additional command buffers for the Metal device to execute as part of the render cycle. For example, you can use a compute command encoder to modify the vertex data in a Metal buffer for use by a SCNGeometrySource object.

> **Note**:  This property is valid only for scene renderers whose [`renderingAPI`](scnscenerenderer/renderingapi.md) value is [`SCNRenderingAPI.metal`](scnrenderingapi/metal.md). You create a SceneKit view that renders using Metal with the [`preferredRenderingAPI`](scnview/option/preferredrenderingapi.md) initialization option or in Interface Builder, or an [`SCNRenderer`](scnrenderer.md) that uses Metal with the [`init(device:options:)`](scnrenderer/init(device:options:).md) method. For OpenGL-based scene renderers, this property’s value is always `nil`.

## See Also

- [var currentRenderCommandEncoder: (any MTLRenderCommandEncoder)?](scnscenerenderer/currentrendercommandencoder.md)
  The Metal render command encoder in use for the current SceneKit rendering pass.
- [var device: (any MTLDevice)?](scnscenerenderer/device.md)
  The Metal device this renderer uses for rendering.
- [var colorPixelFormat: MTLPixelFormat](scnscenerenderer/colorpixelformat.md)
  The Metal pixel format for the renderer’s color output.
- [var depthPixelFormat: MTLPixelFormat](scnscenerenderer/depthpixelformat.md)
  The Metal pixel format for the renderer’s depth buffer.
- [var stencilPixelFormat: MTLPixelFormat](scnscenerenderer/stencilpixelformat.md)
  The Metal pixel format for the renderer’s stencil buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/commandqueue)*