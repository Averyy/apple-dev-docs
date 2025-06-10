# MTLTextureCompressionType

**Framework**: Metal  
**Kind**: enum

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.5+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLTextureCompressionType
```

## Topics

### Enumeration Cases
- [MTLTextureCompressionType.lossless](mtltexturecompressiontype/lossless.md)
- [MTLTextureCompressionType.lossy](mtltexturecompressiontype/lossy.md)
### Initializers
- [init?(rawValue: Int)](mtltexturecompressiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Understanding Color-Renderable Pixel Format Sizes](understanding-color-renderable-pixel-format-sizes.md)
  Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing Texture Data](optimizing-texture-data.md)
  Optimize a texture’s data to improve GPU or CPU access.
- [protocol MTLTexture](mtltexture.md)
  A resource that holds formatted image data.
- [class MTLTextureDescriptor](mtltexturedescriptor.md)
  An object that you use to configure new Metal texture objects.
- [class MTKTextureLoader](../MetalKit/MTKTextureLoader.md)
  An object that creates textures from existing data in common image formats.
- [class MTLSharedTextureHandle](mtlsharedtexturehandle.md)
  A texture handle that can be shared across process address space boundaries.
- [enum MTLPixelFormat](mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturecompressiontype)*