# supports32BitFloatFiltering

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var supports32BitFloatFiltering: Bool { get }
```

## See Also

- [var supportsBCTextureCompression: Bool](mtldevice/supportsbctexturecompression.md)
  A Boolean value that indicates whether you can use textures that use BC compression.
- [var isDepth24Stencil8PixelFormatSupported: Bool](mtldevice/isdepth24stencil8pixelformatsupported.md)
  A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format.
- [var supportsQueryTextureLOD: Bool](mtldevice/supportsquerytexturelod.md)
  A Boolean value that indicates whether you can query the texture level of detail from within a shader.
- [var readWriteTextureSupport: MTLReadWriteTextureTier](mtldevice/readwritetexturesupport.md)
  The GPU device’s texture support tier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supports32bitfloatfiltering)*