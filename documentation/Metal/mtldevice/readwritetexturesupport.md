# readWriteTextureSupport

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The GPU device’s texture support tier.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var readWriteTextureSupport: MTLReadWriteTextureTier { get }
```

## Topics

### Read-write texture tiers
- [enum MTLReadWriteTextureTier](mtlreadwritetexturetier.md)
  The support level for read-write texture formats.

## See Also

- [var supports32BitFloatFiltering: Bool](mtldevice/supports32bitfloatfiltering.md)
  A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.
- [var supportsBCTextureCompression: Bool](mtldevice/supportsbctexturecompression.md)
  A Boolean value that indicates whether you can use textures that use BC compression.
- [var isDepth24Stencil8PixelFormatSupported: Bool](mtldevice/isdepth24stencil8pixelformatsupported.md)
  A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format.
- [var supportsQueryTextureLOD: Bool](mtldevice/supportsquerytexturelod.md)
  A Boolean value that indicates whether you can query the texture level of detail from within a shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/readwritetexturesupport)*