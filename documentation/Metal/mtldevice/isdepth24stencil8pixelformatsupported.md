# isDepth24Stencil8PixelFormatSupported

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format.

**Availability**:
- Mac Catalyst 13.0+ - Deprecated in 27.0
- macOS 10.11+ - Deprecated in 27.0

> **Deprecated**: Never supported on Apple Silicon

## Declaration

```swift
var isDepth24Stencil8PixelFormatSupported: Bool { get }
```

```objc
@property (readonly, getter=isDepth24Stencil8PixelFormatSupported) BOOL depth24Stencil8PixelFormatSupported;
```

#### Discussion

If the value is [`true`](../../Swift/true.md), the device supports the [`MTLPixelFormat.depth24Unorm_stencil8`](../mtlpixelformat/depth24unorm_stencil8.md) pixel format.

## See Also

### Related Documentation
- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
### Checking texture and sampler support
- [var supports32BitFloatFiltering: Bool](./supports32bitfloatfiltering.md)
  A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.
- [var supportsBCTextureCompression: Bool](./supportsbctexturecompression.md)
  A Boolean value that indicates whether you can use textures that use BC compression.
- [var supportsQueryTextureLOD: Bool](./supportsquerytexturelod.md)
  A Boolean value that indicates whether you can query the texture level of detail from within a shader.
- [var readWriteTextureSupport: MTLReadWriteTextureTier](./readwritetexturesupport.md)
  The GPU device’s texture support tier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/isdepth24stencil8pixelformatsupported)*