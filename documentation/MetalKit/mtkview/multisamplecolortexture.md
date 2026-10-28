# multisampleColorTexture

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The multisample color sample texture to render into.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var multisampleColorTexture: (any MTLTexture)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<MTLTexture> multisampleColorTexture;
```

## Discussion

The format of this texture is determined by the value of the [`colorPixelFormat`](./colorpixelformat.md) and [`sampleCount`](./samplecount.md) properties.

The default value is `nil`. This value is also `nil` if the specified pixel format is [`MTLPixelFormat.invalid`](../../Metal/mtlpixelformat/invalid.md), or if [`sampleCount`](./samplecount.md) is less than or equal to 1.

## See Also

### Retrieving Render Target Information
- [var currentRenderPassDescriptor: MTLRenderPassDescriptor?](./currentrenderpassdescriptor.md)
  A render pass descriptor to draw into the current drawable.
- [var currentDrawable: (any CAMetalDrawable)?](./currentdrawable.md)
  The drawable to use for the current frame.
- [var depthStencilTexture: (any MTLTexture)?](./depthstenciltexture.md)
  A packed depth and stencil texture associated with the current drawable object’s texture.
- [var depthStencilStorageMode: MTLStorageMode](./depthstencilstoragemode.md)
  The storage mode that the packed depth and stencil texture use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/multisamplecolortexture)*