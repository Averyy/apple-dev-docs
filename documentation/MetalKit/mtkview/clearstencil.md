# clearStencil

**Framework**: MetalKit  
**Kind**: property

The stencil value to use to clear the stencil target when creating a render pass descriptor.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var clearStencil: UInt32 { get set }
```

#### Discussion

If you specified that you want a stencil texture, the view configures any render passes to use the stencil texture, with a load action of [`MTLLoadAction.clear`](https://developer.apple.com/documentation/Metal/MTLLoadAction/clear) and the value of this property as the value to clear it to. The default value is `0`.

## See Also

- [var depthStencilPixelFormat: MTLPixelFormat](mtkview/depthstencilpixelformat.md)
  The format used to generate the [`depthStencilTexture`](mtkview/depthstenciltexture.md) object.
- [var depthStencilAttachmentTextureUsage: MTLTextureUsage](mtkview/depthstencilattachmenttextureusage.md)
  The texture usage characteristics that the view uses when creating the depth and stencil textures.
- [var clearDepth: Double](mtkview/cleardepth.md)
  The depth value to use to clear the depth target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/clearstencil)*