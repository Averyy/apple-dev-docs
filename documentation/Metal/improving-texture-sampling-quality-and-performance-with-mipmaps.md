# Improving Texture Sampling Quality and Performance with Mipmaps

**Framework**: Metal

Avoid texture-rendering artifacts and reduce the GPU’s workload by creating smaller versions of a texture.

#### Overview

 are progressively smaller versions of the same texture image, each of which provides a different level of detail (LOD) for the texture. A texture’s  is its complete set of mipmaps. Textures with mipmaps can help your app eliminate common visual problems, such as aliasing and moire patterns, while reducing the GPU’s memory bandwidth.

__The largest version of a texture is mipmap `0` and it’s at the top of the mipmap chain. The next largest version is mipmap `1`, which is one level lower in the chain.

![A diagram showing a texture’s mipmap chain that starts with the largest resolution image, labeled  Mipmap 0, on the left. The six images on the right, labeled 1 through 6, are progressively smaller versions of the original texture where each mipmap level is 25% the size of the previous one.](https://docs-assets.developer.apple.com/published/fb5952e55c7f2ef1e8fe970223dfe550/media-4144107%402x.png)

Each nonzero mipmap level is 25% of the area of the previous mipmap level in the chain. A texture’s smallest mipmap is at least 1 pixel in each dimension.

A mipmapped texture gives the GPU the option to sample from a mipmap size that’s closest to the size of the primitive it’s rendering to. A GPU’s texture-sampling hardware works best when a texture’s dimensions are similar to the output primitive’s dimensions. Without mipmaps, the GPU can sample only the full-size texture, including when an output primitive is much smaller than the texture. In that scenario, the hardware typically fetches a significant portion of the texture to properly filter for color.

For example, to filter a 256 x 256 texture to an 8 x 8 rendering, the GPU needs to blend 25% of the texture for each output pixel. Additionally, you can’t precisely control which pixels the GPU fetches from the texture and then blends to render to a relatively small primitive. That imprecision can produce an obviously incorrect image, especially when it spans multiple frames, such as during animations.

![A diagram showing a texture image that’s 256 by 256 pixels divided into four quadrants by two perpendicular dashed lines that intersect at the center of the texture. In the upper right quadrant, the diagram highlights a square sample of the texture that’s 32 by 32 pixels. An arrow points from that square sample to the right to a smaller square. The smaller square is an output rendering of the larger texture, and is 8 by 8 pixels.](https://docs-assets.developer.apple.com/published/c560b024fb30fca20aff692777c05f62/media-3374145%402x.png)

Mipmapped textures can also help improve your app’s performance because a GPU uses less memory bandwidth and memory cache by sampling from the smaller mipmaps.

You can create a mipmapped texture and initialize its mipmap chain by following the steps in [`Creating a Mipmapped Texture`](creating-a-mipmapped-texture.md) and [`Generating Mipmap Data`](generating-mipmap-data.md), respectively.

## See Also

- [Creating a Mipmapped Texture](creating-a-mipmapped-texture.md)
  Decide whether a texture that you’re creating needs mipmaps.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/improving-texture-sampling-quality-and-performance-with-mipmaps)*