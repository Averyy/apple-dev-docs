# isDepth24Stencil8PixelFormatSupported

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.11+

## Declaration

```swift
var isDepth24Stencil8PixelFormatSupported: Bool { get }
```

#### Discussion

If the value is [`true`](https://developer.apple.com/documentation/swift/true), the device supports the [`MTLPixelFormat.depth24Unorm_stencil8`](mtlpixelformat/depth24unorm_stencil8.md) pixel format.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [var supports32BitFloatFiltering: Bool](mtldevice/supports32bitfloatfiltering.md)
  A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.
- [var supportsBCTextureCompression: Bool](mtldevice/supportsbctexturecompression.md)
  A Boolean value that indicates whether you can use textures that use BC compression.
- [var supportsQueryTextureLOD: Bool](mtldevice/supportsquerytexturelod.md)
  A Boolean value that indicates whether you can query the texture level of detail from within a shader.
- [var readWriteTextureSupport: MTLReadWriteTextureTier](mtldevice/readwritetexturesupport.md)
  The GPU device’s texture support tier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/isdepth24stencil8pixelformatsupported)*