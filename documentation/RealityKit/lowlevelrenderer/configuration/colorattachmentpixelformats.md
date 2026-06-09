# colorAttachmentPixelFormats

**Framework**: RealityKit  
**Kind**: property

The pixel formats of the color attachments in the render pass the renderer encodes into.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var colorAttachmentPixelFormats: [MTLPixelFormat] { get }
```

#### Discussion

Use these formats when compiling your own `MTLRenderPipelineState` objects for draw calls issued inside the `render(using:_:)` callback.

## See Also

- [var depthAttachmentPixelFormat: MTLPixelFormat](lowlevelrenderer/configuration/depthattachmentpixelformat.md)
  The pixel format of the depth attachment in the render pass the renderer encodes into.
- [var stencilAttachmentPixelFormat: MTLPixelFormat](lowlevelrenderer/configuration/stencilattachmentpixelformat.md)
  The pixel format of the stencil attachment in the render pass the renderer encodes into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/colorattachmentpixelformats)*