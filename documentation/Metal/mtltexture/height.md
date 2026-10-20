# height

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The height of the texture image for the base level mipmap, in pixels.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var height: Int { get }
```

```objc
@property (readonly) NSUInteger height;
```

#### Discussion

For a 1D texture, the value is `1`.

## See Also

### Querying texture attributes
- [var textureType: MTLTextureType](./texturetype.md)
  The dimension and arrangement of the texture image data.
- [var pixelFormat: MTLPixelFormat](./pixelformat.md)
  The format of pixels in the texture.
- [var width: Int](./width.md)
  The width of the texture image for the base level mipmap, in pixels.
- [var depth: Int](./depth.md)
  The depth of the texture image for the base level mipmap, in pixels.
- [var mipmapLevelCount: Int](./mipmaplevelcount.md)
  The number of mipmap levels in the texture.
- [var arrayLength: Int](./arraylength.md)
  The number of slices in the texture array.
- [var sampleCount: Int](./samplecount.md)
  The number of samples in each pixel.
- [var isFramebufferOnly: Bool](./isframebufferonly.md)
  A Boolean value that indicates whether the texture can only be used as a render target.
- [var usage: MTLTextureUsage](./usage.md)
  Options that determine how you can use the texture.
- [var allowGPUOptimizedContents: Bool](./allowgpuoptimizedcontents.md)
  A Boolean value indicating whether the GPU is allowed to adjust the contents of the texture to improve GPU performance.
- [var isShareable: Bool](./isshareable.md)
  A Boolean indicating whether this texture can be shared with other processes.
- [var swizzle: MTLTextureSwizzleChannels](./swizzle.md)
  The pattern that the GPU applies to pixels when you read or sample pixels from the texture.
- [enum MTLTextureType](../mtltexturetype.md)
  The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [struct MTLTextureUsage](../mtltextureusage.md)
  An enumeration for the various options that determine how you can use a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/height)*