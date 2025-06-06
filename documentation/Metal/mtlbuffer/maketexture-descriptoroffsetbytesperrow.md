# makeTexture(descriptor:offset:bytesPerRow:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a texture that shares its storage with the buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeTexture(descriptor: MTLTextureDescriptor, offset: Int, bytesPerRow: Int) -> (any MTLTexture)?
```

## Mentions

- [Optimizing Texture Data](optimizing-texture-data.md)
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)

#### Return Value

A new texture that shares the buffer’s underlying storage.

#### Discussion

This method creates a new [`MTLTexture`](mtltexture.md) instance that uses the same data as the buffer’s. Modifying the buffer also modifies the new texture because they share the same underlying memory.

> **Note**:  Metal may not be able to optimize a texture that shares memory with a buffer.

The texture’s resource data is coherent between multiple render passes. However, data accesses within a single render pass may not be coherent due to caching at runtime. For example, a texture from this method may not be able to immediately access new values from a render or kernel function that modifies this buffer.

If this buffer’s [`storageMode`](mtltexturedescriptor/storagemode.md) is [`MTLStorageMode.managed`](mtlstoragemode/managed.md), and a render or kernel function modifies it, the CPU can access the new values through a texture after calling the [`synchronize(resource:)`](mtlblitcommandencoder/synchronize(resource:).md) method. CPU accesses are only coherent between command buffer boundaries. GPU barriers guard a GPU’s accesses to buffers and textures so that each access finishes running before the next one begins.

You can create multiple, nonoverlapping textures that use the same buffer; however, the GPU serializes accesses to those textures.

> 💡 **Tip**:  You can avoid the GPU’s texture access serialization by creating multiple buffers and then creating a texture from each buffer with this method.

To create a linear texture, you need to:

- Align the `offset` and `bytesPerRow` parameters to the value that the [`minimumLinearTextureAlignment(for:)`](mtldevice/minimumlineartexturealignment(for:).md) method returns.
- Set the `bytesPerRow` parameter to a value greater than or equal to the number of bytes in one row of pixels — the product of the row’s width, in pixels, and the size of one pixel, in bytes.

Additionally, creating a linear texture from this method adds the following restrictions for the `descriptor` parameter’s properties:

| Property | Acceptable values for a linear texture |
| --- | --- |
| [`textureType`](mtltexturedescriptor/texturetype.md) | [`MTLTextureType.type2D`](mtltexturetype/type2d.md) or [`MTLTextureType.typeTextureBuffer`](mtltexturetype/typetexturebuffer.md) |
| [`depth`](mtltexturedescriptor/depth.md) | `1` |
| [`arrayLength`](mtltexturedescriptor/arraylength.md) | `1` |
| [`mipmapLevelCount`](mtltexturedescriptor/mipmaplevelcount.md) | `1` |
| [`sampleCount`](mtltexturedescriptor/samplecount.md) | `1` |
| [`usage`](mtltexturedescriptor/usage.md) | The [`renderTarget`](mtltextureusage/rendertarget.md) value if the [`MTLDevice`](mtldevice.md) instance supports [`MTLGPUFamily.apple1`](mtlgpufamily/apple1.md) (see [`supportsFamily(_:)`](mtldevice/supportsfamily(_:).md)), or any other [`MTLTextureUsage`](mtltextureusage.md) value |
| [`storageMode`](mtltexturedescriptor/storagemode.md) | The same value as this buffer’s [`storageMode`](mtlresource/storagemode.md) property (see [`Resource Fundamentals`](resource-fundamentals.md)) |
| [`pixelFormat`](mtltexturedescriptor/pixelformat.md) | Any ordinary or packed color [`MTLPixelFormat`](mtlpixelformat.md), except [`MTLPixelFormat.gbgr422`](mtlpixelformat/gbgr422.md) and [`MTLPixelFormat.bgrg422`](mtlpixelformat/bgrg422.md) |

Samplers can use any [`MTLSamplerAddressMode`](mtlsampleraddressmode.md) to sample linear textures from this method on any device that supports the [`MTLGPUFamily.apple2`](mtlgpufamily/apple2.md) feature family or later.

> **Note**:  For devices that support only the [`MTLGPUFamily.apple1`](mtlgpufamily/apple1.md) feature family, samplers can only use [`MTLSamplerAddressMode.clampToEdge`](mtlsampleraddressmode/clamptoedge.md) to sample a linear texture.

## Parameters

- `descriptor`: The descriptor that contains the properties of the texture.
- `offset`: The offset, in bytes, from the base address for the first row of texture data.
- `bytesPerRow`: The stride, in bytes, from one row of texture data to the next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/maketexture(descriptor:offset:bytesperrow:))*