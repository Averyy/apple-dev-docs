# LowLevelTextureResource.Descriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The configuration for a new low-level texture resource.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Descriptor
```

## Overview

This descriptor is analogous to `MTLTextureDescriptor`.

## Topics

### Creating a descriptor
- [init(textureType: MTLTextureType, pixelFormat: MTLPixelFormat, width: Int, height: Int, depth: Int, mipmapLevelCount: Int, arrayLength: Int, textureUsage: MTLTextureUsage, swizzle: MTLTextureSwizzleChannels)](./descriptor-swift.struct/init%28texturetype,pixelformat,width,height,depth,mipmaplevelcount,arraylength,textureusage,swizzle%29.md)
  Creates a texture descriptor with the specified texture type, pixel format, dimensions, mipmap count, array length, usage flags, and swizzle pattern.
### Configuring texture usage
- [var textureUsage: MTLTextureUsage](./descriptor-swift.struct/textureusage.md)
  The options that determine how the texture can be used.
- [var swizzle: MTLTextureSwizzleChannels](./descriptor-swift.struct/swizzle.md)
  The channel swizzle pattern the GPU applies when sampling the texture.
### Instance Properties
- [var arrayLength: Int](./descriptor-swift.struct/arraylength.md)
  The number of array elements for this texture.
- [var depth: Int](./descriptor-swift.struct/depth.md)
  The depth of the texture image for the base mipmap level, in pixels.
- [var height: Int](./descriptor-swift.struct/height.md)
  The height of the texture image for the base mipmap level, in pixels.
- [var mipmapLevelCount: Int](./descriptor-swift.struct/mipmaplevelcount.md)
  The number of mipmap levels for the texture.
- [var pixelFormat: MTLPixelFormat](./descriptor-swift.struct/pixelformat.md)
  The size and bit layout of all pixels in the texture.
- [var textureType: MTLTextureType](./descriptor-swift.struct/texturetype.md)
  The dimension and arrangement of texture image data.
- [var width: Int](./descriptor-swift.struct/width.md)
  The width of the texture image for the base mipmap level, in pixels.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the descriptor
- [var descriptor: LowLevelTextureResource.Descriptor](./descriptor-swift.property.md)
  The descriptor used to create this texture resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltextureresource/descriptor-swift.struct)*