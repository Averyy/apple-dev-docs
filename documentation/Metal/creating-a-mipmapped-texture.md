# Creating a Mipmapped Texture

**Framework**: Metal

Decide whether a texture that you’re creating needs mipmaps.

#### Overview

In Metal, the same [`MTLTexture`](mtltexture.md) object owns all of the mipmaps for a texture. When you create the texture descriptor for a new texture, you determine many of the texture’s fixed properties, including how many mipmaps it has. Set the [`mipmapLevelCount`](mtltexturedescriptor/mipmaplevelcount.md) property to the number of mipmap levels you want the texture to have. The default value is `1`, which means that Metal doesn’t create mipmaps.

The code below creates a texture with multiple mipmaps. It calculates the number of mipmaps needed for a full mipmap chain, from the original size down to a `1x1` texture, and sets that number as the mipmap count. Generating a full mipmap chain requires 33% more memory than if you just had the top image. You can choose to create a mipmap chain that has fewer mipmap levels.

When you create a texture, Metal doesn’t initialize mipmap levels. You need to provide data for any mipmap levels that the GPU accesses. Further, Metal doesn’t keep track of which mipmaps you’ve filled in, or which contain uninitialized or stale data. You’ll need to keep track of that information yourself.

##### Load a Mipmapped Texture Using Metalkit

If you use MetalKit to create a texture, and the source data includes multiple mipmaps, MetalKit automatically creates the texture with the correct number of mipmaps and copies the source data into the appropriate mipmap levels. If the source data doesn’t include mipmaps, MetalKit creates a texture with just one texture image.

You can override this behavior by providing an options dictionary with one of the following keys:

- The [`allocateMipmaps`](https://developer.apple.com/documentation/MetalKit/MTKTextureLoader/Option/allocateMipmaps) key with a value of [`true`](https://developer.apple.com/documentation/swift/true) allocates a full set of mipmap levels for the texture. After loading is complete, Metal fills mipmap `0` with the source data, and leaves the other mipmap contents uninitialized; you fill the other mipmaps with data. Similarly, if you provide this key with a value of [`false`](https://developer.apple.com/documentation/swift/false), Metal ignores any extra mipmap data and only loads the top mipmap.
- The [`generateMipmaps`](https://developer.apple.com/documentation/MetalKit/MTKTextureLoader/Option/generateMipmaps) key with a value of [`true`](https://developer.apple.com/documentation/swift/true) allocates a full set of mipmap levels for the texture. This key has the device object generate images for the lower-level mipmaps by filtering the provided source data.

## See Also

- [Improving Texture Sampling Quality and Performance with Mipmaps](improving-texture-sampling-quality-and-performance-with-mipmaps.md)
  Avoid texture-rendering artifacts and reduce the GPU’s workload by creating smaller versions of a texture.
- [Copying Data into or out of Mipmaps](copying-data-into-or-out-of-mipmaps.md)
  Specify which mipmaps that the data transfer affects.
- [Generating Mipmap Data](generating-mipmap-data.md)
  Create your mipmaps either when you author content or at runtime.
- [Adding Mipmap Filtering to Samplers](adding-mipmap-filtering-to-samplers.md)
  Specify how the GPU samples mipmaps in your textures.
- [Restricting Access to Specific Mipmaps](restricting-access-to-specific-mipmaps.md)
  Set the range of mipmap levels that a sampler can access.
- [Predicting Which Mips the GPU Samples with Level-of-Detail Queries](predicting-which-mips-the-gpu-samples-with-level-of-detail-queries.md)
  Determine in advance which mipmap levels the GPU requires to sample a texture.
- [Dynamically Adjusting Texture Level of Detail](dynamically-adjusting-texture-level-of-detail.md)
  Defer generating or loading larger mipmaps until that level of detail is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/creating-a-mipmapped-texture)*