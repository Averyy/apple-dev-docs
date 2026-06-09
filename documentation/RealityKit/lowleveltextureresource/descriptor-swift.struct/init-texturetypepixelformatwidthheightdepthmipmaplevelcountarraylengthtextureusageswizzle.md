# init(textureType:pixelFormat:width:height:depth:mipmapLevelCount:arrayLength:textureUsage:swizzle:)

**Framework**: RealityKit  
**Kind**: init

Creates a texture descriptor with the specified texture type, pixel format, dimensions, mipmap count, array length, usage flags, and swizzle pattern.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(textureType: MTLTextureType = .type2D, pixelFormat: MTLPixelFormat = .invalid, width: Int = 0, height: Int = 0, depth: Int = 1, mipmapLevelCount: Int = 1, arrayLength: Int = 1, textureUsage: MTLTextureUsage = .unknown, swizzle: MTLTextureSwizzleChannels = .init(red: .red, green: .green, blue: .blue, alpha: .alpha))
```

## Parameters

- `textureType`: The dimension and arrangement of texture image data. Defaults to `.type2D`.
- `pixelFormat`: The size and bit layout of all pixels in the texture. Defaults to `.invalid`.
- `width`: The width of the texture image for the base mipmap level, in pixels. Defaults to `0`.
- `height`: The height of the texture image for the base mipmap level, in pixels. Defaults to `0`.
- `depth`: The depth of the texture image for the base mipmap level, in pixels. Defaults to `1`.
- `mipmapLevelCount`: The number of mipmap levels for the texture. Defaults to `1`.
- `arrayLength`: The number of array elements for this texture. Defaults to `1`.
- `textureUsage`: The options that determine how the texture can be used. Defaults to `.unknown`.
- `swizzle`: The channel swizzle pattern the GPU applies when sampling the texture. Defaults to identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltextureresource/descriptor-swift.struct/init(texturetype:pixelformat:width:height:depth:mipmaplevelcount:arraylength:textureusage:swizzle:))*