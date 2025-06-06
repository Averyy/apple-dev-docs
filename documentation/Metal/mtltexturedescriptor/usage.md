# usage

**Framework**: Metal  
**Kind**: property

Options that determine how you can use the texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var usage: MTLTextureUsage { get set }
```

## Mentions

- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)

#### Discussion

The default value for this property is [`shaderRead`](mtltextureusage/shaderread.md). If the given texture has multiple uses in your app, you can combine multiple usage options for that texture. After you set a texture’s usage options, you can use it only in the ways that you specified.

Metal can optimize operations for a given texture, based on its intended use. Set explicit usage options for a texture, if you know them in advance, before you use the texture. Only set usage options that correspond to a texture’s intended use.

In iOS devices with GPU family 5, Metal doesn’t apply lossless compression to a given texture if you set any of these options:

- [`unknown`](mtltextureusage/unknown.md)
- [`shaderWrite`](mtltextureusage/shaderwrite.md)
- [`pixelFormatView`](mtltextureusage/pixelformatview.md)

## See Also

- [var textureType: MTLTextureType](mtltexturedescriptor/texturetype.md)
  The dimension and arrangement of texture image data.
- [var pixelFormat: MTLPixelFormat](mtltexturedescriptor/pixelformat.md)
  The size and bit layout of all pixels in the texture.
- [var width: Int](mtltexturedescriptor/width.md)
  The width of the texture image for the base level mipmap, in pixels.
- [var height: Int](mtltexturedescriptor/height.md)
  The height of the texture image for the base level mipmap, in pixels.
- [var depth: Int](mtltexturedescriptor/depth.md)
  The depth of the texture image for the base level mipmap, in pixels.
- [var mipmapLevelCount: Int](mtltexturedescriptor/mipmaplevelcount.md)
  The number of mipmap levels for this texture.
- [var sampleCount: Int](mtltexturedescriptor/samplecount.md)
  The number of samples in each fragment.
- [var arrayLength: Int](mtltexturedescriptor/arraylength.md)
  The number of array elements for this texture.
- [var resourceOptions: MTLResourceOptions](mtltexturedescriptor/resourceoptions.md)
  The behavior of a new memory allocation.
- [var cpuCacheMode: MTLCPUCacheMode](mtltexturedescriptor/cpucachemode.md)
  The CPU cache mode used for the CPU mapping of the texture.
- [var storageMode: MTLStorageMode](mtltexturedescriptor/storagemode.md)
  The location and access permissions of the texture.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtltexturedescriptor/hazardtrackingmode.md)
  The texture’s hazard tracking mode.
- [var allowGPUOptimizedContents: Bool](mtltexturedescriptor/allowgpuoptimizedcontents.md)
  A Boolean value indicating whether the GPU is allowed to adjust the texture’s contents to improve GPU performance.
- [var swizzle: MTLTextureSwizzleChannels](mtltexturedescriptor/swizzle.md)
  The pattern you want the GPU to apply to pixels when you read or sample pixels from the texture.
- [struct MTLTextureSwizzleChannels](mtltextureswizzlechannels.md)
  A pattern that modifies the data read or sampled from a texture by rearranging or duplicating the elements of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturedescriptor/usage)*