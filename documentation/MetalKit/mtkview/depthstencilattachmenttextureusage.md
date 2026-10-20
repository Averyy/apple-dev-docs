# depthStencilAttachmentTextureUsage

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The texture usage characteristics that the view uses when creating the depth and stencil textures.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var depthStencilAttachmentTextureUsage: MTLTextureUsage { get set }
```

```objc
@property (nonatomic) MTLTextureUsage depthStencilAttachmentTextureUsage;
```

#### Discussion

The default value is [`renderTarget`](../../Metal/mtltextureusage/rendertarget.md).

## See Also

### Configuring the Render Target Properties
- [var depthStencilPixelFormat: MTLPixelFormat](./depthstencilpixelformat.md)
  The format used to generate the [`depthStencilTexture`](./depthstenciltexture.md) object.
- [var clearDepth: Double](./cleardepth.md)
  The depth value to use to clear the depth target when creating a render pass descriptor.
- [var clearStencil: UInt32](./clearstencil.md)
  The stencil value to use to clear the stencil target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/depthstencilattachmenttextureusage)*