# MTLTextureCompressionType

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MTLTextureCompressionType : NSInteger;
```

## Topics

### Enumeration Cases
- [MTLTextureCompressionType.lossless](./mtltexturecompressiontype/lossless.md)
- [MTLTextureCompressionType.lossy](./mtltexturecompressiontype/lossy.md)
### Initializers
- [init?(rawValue: Int)](./mtltexturecompressiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Texture basics
- [Understanding color-renderable pixel format sizes](./understanding-color-renderable-pixel-format-sizes.md)
  Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing texture data](./optimizing-texture-data.md)
  Optimize a texture’s data to improve GPU or CPU access.
- [protocol MTLTexture](./mtltexture.md)
  A resource that holds formatted image data.
- [class MTLTextureDescriptor](./mtltexturedescriptor.md)
  An instance that you use to configure new Metal texture instances.
- [class MTKTextureLoader](../MetalKit/mtktextureloader.md)
  An object that creates textures from existing data in common image formats.
- [class MTLSharedTextureHandle](./mtlsharedtexturehandle.md)
  A texture handle that can be shared across process address space boundaries.
- [enum MTLPixelFormat](./mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturecompressiontype)*