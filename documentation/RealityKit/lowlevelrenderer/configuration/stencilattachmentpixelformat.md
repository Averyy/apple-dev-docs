# stencilAttachmentPixelFormat

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The pixel format of the stencil attachment in the render pass the renderer encodes into.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var stencilAttachmentPixelFormat: MTLPixelFormat { get }
```

## Discussion

Relevant when the render pass uses a separate stencil attachment rather than a packed depth-stencil format. Use this format when compiling your own `MTLRenderPipelineState` objects for draw calls issued inside the `render(using:_:)` callback.

## See Also

### Configuring pixel formats
- [var colorAttachmentPixelFormats: [MTLPixelFormat]](./colorattachmentpixelformats.md)
  The pixel formats of the color attachments in the render pass the renderer encodes into.
- [var depthAttachmentPixelFormat: MTLPixelFormat](./depthattachmentpixelformat.md)
  The pixel format of the depth attachment in the render pass the renderer encodes into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/stencilattachmentpixelformat)*