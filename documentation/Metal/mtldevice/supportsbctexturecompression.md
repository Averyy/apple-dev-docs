# supportsBCTextureCompression

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether you can use textures that use BC compression.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 11.0+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
var supportsBCTextureCompression: Bool { get }
```

## See Also

- [var supports32BitFloatFiltering: Bool](mtldevice/supports32bitfloatfiltering.md)
  A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.
- [var isDepth24Stencil8PixelFormatSupported: Bool](mtldevice/isdepth24stencil8pixelformatsupported.md)
  A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format.
- [var supportsQueryTextureLOD: Bool](mtldevice/supportsquerytexturelod.md)
  A Boolean value that indicates whether you can query the texture level of detail from within a shader.
- [var readWriteTextureSupport: MTLReadWriteTextureTier](mtldevice/readwritetexturesupport.md)
  The GPU device’s texture support tier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportsbctexturecompression)*