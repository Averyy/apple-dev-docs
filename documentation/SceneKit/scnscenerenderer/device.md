# device

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The Metal device this renderer uses for rendering.

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
var device: (any MTLDevice)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<MTLDevice> device;
```

## Discussion

Use this property to create or look up other Metal resources that use the same device as your SceneKit renderer.

> **Note**:  This property is valid only for scene renderers whose [`renderingAPI`](./renderingapi.md) value is [`SCNRenderingAPI.metal`](../scnrenderingapi/metal.md). You create a SceneKit view that renders using Metal with the [`preferredRenderingAPI`](../scnview/option/preferredrenderingapi.md) initialization option or in Interface Builder, or an [`SCNRenderer`](../scnrenderer.md) that uses Metal with the [`init(device:options:)`](../scnrenderer/init%28device,options%29.md) method. For OpenGL-based scene renderers, this property’s value is always `nil`.

## See Also

### Customizing Scene Rendering with Metal
- [var currentRenderCommandEncoder: (any MTLRenderCommandEncoder)?](./currentrendercommandencoder.md)
  The Metal render command encoder in use for the current SceneKit rendering pass.
- [var commandQueue: (any MTLCommandQueue)?](./commandqueue.md)
  The Metal command queue this renderer uses for rendering.
- [var colorPixelFormat: MTLPixelFormat](./colorpixelformat.md)
  The Metal pixel format for the renderer’s color output.
- [var depthPixelFormat: MTLPixelFormat](./depthpixelformat.md)
  The Metal pixel format for the renderer’s depth buffer.
- [var stencilPixelFormat: MTLPixelFormat](./stencilpixelformat.md)
  The Metal pixel format for the renderer’s stencil buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/device)*