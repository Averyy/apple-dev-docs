# LowLevelTextureResource.Descriptor

**Framework**: RealityKit  
**Kind**: struct

The configuration for a new low-level texture resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Descriptor
```

#### Overview

This descriptor is analogous to `MTLTextureDescriptor`.

## Topics

### Creating a descriptor
- [init(textureType: MTLTextureType, pixelFormat: MTLPixelFormat, width: Int, height: Int, depth: Int, mipmapLevelCount: Int, arrayLength: Int, textureUsage: MTLTextureUsage, swizzle: MTLTextureSwizzleChannels)](lowleveltextureresource/descriptor-swift.struct/init(texturetype:pixelformat:width:height:depth:mipmaplevelcount:arraylength:textureusage:swizzle:).md)
  Creates a texture descriptor with the specified texture type, pixel format, dimensions, mipmap count, array length, usage flags, and swizzle pattern.
### Configuring texture usage
- [var textureUsage: MTLTextureUsage](lowleveltextureresource/descriptor-swift.struct/textureusage.md)
  The options that determine how the texture can be used.
- [var swizzle: MTLTextureSwizzleChannels](lowleveltextureresource/descriptor-swift.struct/swizzle.md)
  The channel swizzle pattern the GPU applies when sampling the texture.
### Instance Properties
- [var arrayLength: Int](lowleveltextureresource/descriptor-swift.struct/arraylength.md)
  The number of array elements for this texture.
- [var depth: Int](lowleveltextureresource/descriptor-swift.struct/depth.md)
  The depth of the texture image for the base mipmap level, in pixels.
- [var height: Int](lowleveltextureresource/descriptor-swift.struct/height.md)
  The height of the texture image for the base mipmap level, in pixels.
- [var mipmapLevelCount: Int](lowleveltextureresource/descriptor-swift.struct/mipmaplevelcount.md)
  The number of mipmap levels for the texture.
- [var pixelFormat: MTLPixelFormat](lowleveltextureresource/descriptor-swift.struct/pixelformat.md)
  The size and bit layout of all pixels in the texture.
- [var textureType: MTLTextureType](lowleveltextureresource/descriptor-swift.struct/texturetype.md)
  The dimension and arrangement of texture image data.
- [var width: Int](lowleveltextureresource/descriptor-swift.struct/width.md)
  The width of the texture image for the base mipmap level, in pixels.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var descriptor: LowLevelTextureResource.Descriptor](lowleveltextureresource/descriptor-swift.property.md)
  The descriptor used to create this texture resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltextureresource/descriptor-swift.struct)*