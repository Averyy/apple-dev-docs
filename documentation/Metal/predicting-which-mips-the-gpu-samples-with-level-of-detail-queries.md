# Predicting Which Mips the GPU Samples with Level-of-Detail Queries

**Framework**: Metal

Determine in advance which mipmap levels the GPU requires to sample a texture.

#### Overview

When you sample a texture, the GPU automatically chooses which mipmaps to access and fetches pixels from them. Each mipmap represents a different level-of-detail (LOD).

Sometimes, you want to know which mipmaps the GPU would read from. For example, if only some of your mipmaps have data, you might use a clamp operation to limit the range of mipmaps the GPU can sample from, but want to know when the GPU requires sampling higher mipmaps. Metal Shading Language provides texture functions that you can use to determine which mipmaps your shader would access if it were to sample the texture.

##### Check for Level of Detail Support

Before loading any shaders that use LOD queries, make sure the GPU supports them by checking if it supports one of the following:

- The [`MTLGPUFamily.mac2`](mtlgpufamily/mac2.md) feature set.
- The [`MTLGPUFamily.apple7`](mtlgpufamily/apple7.md) feature set.

##### Determine Level of Detail

In your shader, the functions that return LOD information have signatures that are similar to those of functions used to sample textures. There are two kinds of these functions: clamped and unclamped. The clamped kind restricts LOD selection by applying the sampler’s range of permitted values, the range of mipmaps provided in the texture, and the sampler’s anisotropy settings. The unclamped kind returns the raw calculation.

```metal
float clampedLOD = texture.calculate_clamped_lod(mySampler, coords);
float unclampedLOD = texture.calculate_unclamped_lod(mySampler, coords);
```

A fractional part in a returned value indicates that the value is between two mipmaps. The fractional part of the number is the blending weight between the two mipmaps if you’ve specified linear mipmap blending.

##### Determine Level of Detail When Shader Support Is Unavailable

Alternatively, you can get the LOD by performing the calculation yourself, based on the size of the model object and its distance from the camera. For an example of this technique, see [`Using Function Specialization to Build Pipeline Variants`](using-function-specialization-to-build-pipeline-variants.md).

## See Also

- [Improving Texture Sampling Quality and Performance with Mipmaps](improving-texture-sampling-quality-and-performance-with-mipmaps.md)
  Avoid texture-rendering artifacts and reduce the GPU’s workload by creating smaller versions of a texture.
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
- [Dynamically Adjusting Texture Level of Detail](dynamically-adjusting-texture-level-of-detail.md)
  Defer generating or loading larger mipmaps until that level of detail is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/predicting-which-mips-the-gpu-samples-with-level-of-detail-queries)*