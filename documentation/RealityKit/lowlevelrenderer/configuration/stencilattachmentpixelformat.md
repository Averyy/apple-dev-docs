# stencilAttachmentPixelFormat

**Framework**: RealityKit  
**Kind**: property

The pixel format of the stencil attachment in the render pass the renderer encodes into.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var stencilAttachmentPixelFormat: MTLPixelFormat { get }
```

#### Discussion

Relevant when the render pass uses a separate stencil attachment rather than a packed depth-stencil format. Use this format when compiling your own `MTLRenderPipelineState` objects for draw calls issued inside the `render(using:_:)` callback.

## See Also

- [var colorAttachmentPixelFormats: [MTLPixelFormat]](lowlevelrenderer/configuration/colorattachmentpixelformats.md)
  The pixel formats of the color attachments in the render pass the renderer encodes into.
- [var depthAttachmentPixelFormat: MTLPixelFormat](lowlevelrenderer/configuration/depthattachmentpixelformat.md)
  The pixel format of the depth attachment in the render pass the renderer encodes into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/stencilattachmentpixelformat)*