# Adding Mipmap Filtering to Samplers

**Framework**: Metal

Specify how the GPU samples mipmaps in your textures.

#### Overview

By default, samplers sample data only from mipmap `0`. If your texture contains more than one mipmap, and you want it to sample the lower-level mipmaps, you need to specify this behavior when you create the texture sampler.

##### Create the Sampler in Your App

If you’re creating a [`MTLSamplerState`](mtlsamplerstate.md) object, create the [`MTLSamplerDescriptor`](mtlsamplerdescriptor.md) object and set its [`mipFilter`](mtlsamplerdescriptor/mipfilter.md) property. The following code uses linear filtering for the minification and magnification filter, and uses linear filtering for mipmaps. This combination is usually called . With this configuration, the GPU chooses the two mipmaps nearest in size and generates a sample by linearly filtering four pixels from each mipmap. Then it blends those two values with a linear interpolation to generate the final sample.

Alternatively, any of these filters could filter from the nearest pixel, instead of a linear filter, resulting in fewer sampled pixels but lower quality. Ultimately, you need to decide the right tradeoffs between sampling performance and quality for your app.

##### Create the Sampler in Your Shader

If you prefer to create samplers in your shader, specify the mipmap filtering there instead of in your app:

```metal
constexpr sampler s(filter::linear, mip_filter::linear)
```

## See Also

- [Improving Texture Sampling Quality and Performance with Mipmaps](improving-texture-sampling-quality-and-performance-with-mipmaps.md)
  Avoid texture-rendering artifacts and reduce the GPU’s workload by creating smaller versions of a texture.
- [Creating a Mipmapped Texture](creating-a-mipmapped-texture.md)
  Decide whether a texture that you’re creating needs mipmaps.
- [Copying Data into or out of Mipmaps](copying-data-into-or-out-of-mipmaps.md)
  Specify which mipmaps that the data transfer affects.
- [Generating Mipmap Data](generating-mipmap-data.md)
  Create your mipmaps either when you author content or at runtime.
- [Restricting Access to Specific Mipmaps](restricting-access-to-specific-mipmaps.md)
  Set the range of mipmap levels that a sampler can access.
- [Predicting Which Mips the GPU Samples with Level-of-Detail Queries](predicting-which-mips-the-gpu-samples-with-level-of-detail-queries.md)
  Determine in advance which mipmap levels the GPU requires to sample a texture.
- [Dynamically Adjusting Texture Level of Detail](dynamically-adjusting-texture-level-of-detail.md)
  Defer generating or loading larger mipmaps until that level of detail is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/adding-mipmap-filtering-to-samplers)*