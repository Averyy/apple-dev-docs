# clearStencil

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

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
var clearStencil: UInt32 { get set }
```

```objc
@property (nonatomic) uint32_t clearStencil;
```

#### Discussion

If you specified that you want a stencil texture, the view configures any render passes to use the stencil texture, with a load action of [`MTLLoadAction.clear`](../../Metal/mtlloadaction/clear.md) and the value of this property as the value to clear it to. The default value is `0`.

## See Also

### Configuring the Render Target Properties
- [var depthStencilPixelFormat: MTLPixelFormat](./depthstencilpixelformat.md)
  The format used to generate the [`depthStencilTexture`](./depthstenciltexture.md) object.
- [var depthStencilAttachmentTextureUsage: MTLTextureUsage](./depthstencilattachmenttextureusage.md)
  The texture usage characteristics that the view uses when creating the depth and stencil textures.
- [var clearDepth: Double](./cleardepth.md)
  The depth value to use to clear the depth target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/clearstencil)*