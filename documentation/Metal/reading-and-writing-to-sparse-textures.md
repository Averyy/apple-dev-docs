# Reading and writing to sparse textures

**Framework**: Metal

Decide how to handle access to unmapped texture regions.

#### Overview

You don’t need to rewrite your shaders to work with sparse textures. You can treat sparse textures just like any other textures. However, they work differently if you access an unmapped region in the texture:

- If you read or sample from an unmapped region, Metal returns a vector of zero values to your shader.
- If you write to an unmapped region, Metal discards the write value.

If this default behavior is insufficient for your app, update your shaders to handle memory operations to unmapped regions.

##### Test for Unmapped Regions in Your Shader

When you sample a texture, you can explicitly test to see whether that action accessed an unmapped region. Instead of calling the `sample` method, call `sparse_sample`. The `sparse_sample` methods return a `sparse_color<T>` object, which provides methods you can call to determine whether you sampled a mapped region in the texture, and to get the sampled data.

The following example code uses the `sparse_sample` method to implement a fallback mechanism. The texture being sampled always has the mipmap tail mapped into memory. One of the shader arguments specifies the first mipmap in the tail. The fragment shader performs the following steps:

1. It samples the texture by calling the `sparse_sample` method.
2. If the sampler read data from a mapped region, the fragment shader returns the sampled value.
3. If the sampler accessed an unmapped region, the shader samples the texture again using the `min_lod_clamp` modifier to restrict access to the mapped part of the texture. Because this part of the mipmap chain is always mapped, the second request uses the regular `sample` method.

```metal
fragment float4 fragmentShader(
    ColorInOut in [[stage_in]],
    constant Uniforms & uniforms  [[ buffer(BufferIndexUniforms) ]],
    texture2d<float> colorMap  [[ texture(TextureIndexColor) ]],
    constant float & firstTailMip  [[ buffer(BufferIndexMipmap) ]])
{
    constexpr sampler colorSampler(mip_filter::linear,
                                   mag_filter::linear,
                                   min_filter::linear);

    sparse_color<float4> sparseSample = colorMap.sparse_sample(colorSampler, in.texCoord.xy);

    if (sparseSample.resident())
    {
        return sparseSample.value();
    }
    else
    {
        return colorMap.sample(colorSampler,
                               in.texCoord.xy,
                               min_lod_clamp(firstTailMip));
    }
}
```

For more information about the other methods for sampling or reading from sparse textures, see [`Metal Shading Language Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364) and [`Restricting access to specific mipmaps`](restricting-access-to-specific-mipmaps.md).

##### Track Residency Information

A more advanced way to create fallback behavior is to track residency information in a . A residency map is another texture with a pixel for every tile region in your main texture. You use a residency map to maintain per-tile information about your texture.

For example, you might use a residency map to determine whether a region is currently mapped. Remember that the GPU maps and unmaps sparse tiles, and this happens asynchronously. Further, if the heap runs out of memory, the GPU doesn’t return an error. If you need to know whether a region was successfully mapped, use a residency map to store this information. Execute a shader that samples one pixel (using `sparse_sample`) from each region. Determine whether the sample was resident and write the result into the residency map. Once the map data is complete, you can sample the texture or copy it to a buffer that your app can access.

Another way to use a residency map is to store the best level of detail that you’ve mapped for each region in your texture. If you attempt to sample the texture and the requested region isn’t mapped, instead of sampling the tail mipmaps, you can look up the best level of detail that is mapped and sample the texture again.

## See Also

- [Managing sparse texture memory](managing-sparse-texture-memory.md)
  Take direct control of memory allocation for texture data by using sparse textures.
- [Creating sparse heaps and sparse textures](creating-sparse-heaps-and-sparse-textures.md)
  Allocate memory for sparse textures by creating a sparse heap.
- [Converting between pixel regions and sparse tile regions](converting-between-pixel-regions-and-sparse-tile-regions.md)
  Learn how a sparse texture’s contents are organized in memory.
- [Assigning memory to sparse textures](assigning-memory-to-sparse-textures.md)
  Use a resource state encoder to allocate and deallocate sparse tiles for a sparse texture.
- [Estimating how often a texture region is accessed](estimating-how-often-a-texture-region-is-accessed.md)
  Use texture access patterns to determine when you need to map a texture region.
- [class MTLResourceStatePassDescriptor](mtlresourcestatepassdescriptor.md)
  A configuration for a resource state pass, used to create a resource state command encoder.
- [class MTLResourceStatePassSampleBufferAttachmentDescriptor](mtlresourcestatepasssamplebufferattachmentdescriptor.md)
  A description of where to store GPU counter information at the start and end of a resource state pass.
- [class MTLResourceStatePassSampleBufferAttachmentDescriptorArray](mtlresourcestatepasssamplebufferattachmentdescriptorarray.md)
  An array of sample buffer attachments for a resource state pass.
- [protocol MTLResourceStateCommandEncoder](mtlresourcestatecommandencoder.md)
  An encoder that encodes commands that modify resource configurations.
- [struct MTLMapIndirectArguments](mtlmapindirectarguments.md)
  The data layout for mapping sparse texture regions when using indirect commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/reading-and-writing-to-sparse-textures)*