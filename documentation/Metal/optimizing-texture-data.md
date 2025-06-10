# Optimizing Texture Data

**Framework**: Metal

Optimize a texture’s data to improve GPU or CPU access.

#### Overview

By default, Metal attempts to optimize a texture’s data for both GPU or CPU accesses based on the texture’s storage mode and usage options. You can improve a texture’s performance on the GPU or CPU by specifically optimizing the texture’s data for either use case. You can also opt out of optimization altogether. Optimizing a texture’s performance for one use can decrease that texture’s performance for another.

Before optimizing texture data, carefully consider the storage modes and usage options for your textures. For guidance on resource storage modes, see [`Setting Resource Storage Modes`](setting-resource-storage-modes.md). For guidance on texture usage options, see [`MTLTextureUsage`](mtltextureusage.md).

> **Note**:  Metal may not be able to optimize some textures for specific hardware and ignores optimization API calls for those textures.

##### Optimize Texture Data for Gpu Access

By default, Metal attempts to optimize texture data for GPU access if it meets any of these conditions:

- You create the texture with an [`MTLStorageMode.private`](mtlstoragemode/private.md) mode.
- You create the texture with an [`renderTarget`](mtltextureusage/rendertarget.md) option.

If the texture doesn’t meet any of these conditions, you can optimize your texture data explicitly. After you create your texture and populate its contents, encode and commit an [`optimizeContentsForGPUAccess(texture:)`](mtlblitcommandencoder/optimizecontentsforgpuaccess(texture:).md) or [`optimizeContentsForGPUAccess(texture:slice:level:)`](mtlblitcommandencoder/optimizecontentsforgpuaccess(texture:slice:level:).md) command.

To optimize a drawable from an [`MTKView`](https://developer.apple.com/documentation/MetalKit/MTKView) for GPU access, set the view’s [`framebufferOnly`](https://developer.apple.com/documentation/MetalKit/MTKView/framebufferOnly) property to [`true`](https://developer.apple.com/documentation/swift/true). This property configures the texture exclusively as a render target and displayable resource.

##### Optimize Texture Data for Cpu Access

By default, Metal attempts to optimize texture data for CPU access if it meets both of these conditions:

- You create the texture with an [`MTLStorageMode.shared`](mtlstoragemode/shared.md) or [`MTLStorageMode.managed`](mtlstoragemode/managed.md) mode.
- You write to the texture with the [`replace(region:mipmapLevel:withBytes:bytesPerRow:)`](mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:).md) or [`replace(region:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:)`](mtltexture/replace(region:mipmaplevel:slice:withbytes:bytesperrow:bytesperimage:).md) method.

If you don’t meet both of these conditions, you can optimize your texture data explicitly. After you create your texture and populate its contents, encode and commit an [`optimizeContentsForCPUAccess(texture:)`](mtlblitcommandencoder/optimizecontentsforcpuaccess(texture:).md) or [`optimizeContentsForCPUAccess(texture:slice:level:)`](mtlblitcommandencoder/optimizecontentsforcpuaccess(texture:slice:level:).md) command.

##### Apply Lossless Compression to a Texture on Apple Gpus

Lossless compression is a specific form of GPU optimization that Metal can apply to texture data. Lossless compression reduces a texture’s memory size without discarding any of its data. On devices that support [`MTLGPUFamily.apple5`](mtlgpufamily/apple5.md), Metal attempts to apply lossless compression to a texture if it meets all of these conditions:

- You don’t create the texture with a block-compressed pixel format, such as PVRTC, ASTC, or BC.
- You don’t create the texture with an [`unknown`](mtltextureusage/unknown.md), [`shaderWrite`](mtltextureusage/shaderwrite.md), or [`pixelFormatView`](mtltextureusage/pixelformatview.md) option.
- You don’t create the texture from a buffer with the [`makeTexture(descriptor:offset:bytesPerRow:)`](mtlbuffer/maketexture(descriptor:offset:bytesperrow:).md) method.

Additionally, if you meet both of the following conditions, you can optimize your texture data explicitly so Metal can apply lossless compression:

- You create the texture with an [`MTLStorageMode.shared`](mtlstoragemode/shared.md) mode.
- You write to the texture with the [`replace(region:mipmapLevel:withBytes:bytesPerRow:)`](mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:).md) or [`replace(region:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:)`](mtltexture/replace(region:mipmaplevel:slice:withbytes:bytesperrow:bytesperimage:).md) method.

For guidance, see [`Optimize Texture Data for GPU Access`](optimizing-texture-data#Optimize-Texture-Data-for-GPU-Access.md).

##### Opt Out of Texture Data Optimization for Gpu Access

In some cases, your texture data may benefit from opting out of optimization for GPU access, for example, when optimization has regressed your app’s performance (particularly for render target read-backs on the CPU).

First, create a texture descriptor and set its [`allowGPUOptimizedContents`](mtltexturedescriptor/allowgpuoptimizedcontents.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

Then, set the texture descriptor’s [`storageMode`](mtltexturedescriptor/storagemode.md) property to [`MTLStorageMode.shared`](mtlstoragemode/shared.md) or [`MTLStorageMode.managed`](mtlstoragemode/managed.md).

Finally, create a texture from the texture descriptor.

## See Also

- [Understanding Color-Renderable Pixel Format Sizes](understanding-color-renderable-pixel-format-sizes.md)
  Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [protocol MTLTexture](mtltexture.md)
  A resource that holds formatted image data.
- [enum MTLTextureCompressionType](mtltexturecompressiontype.md)
- [class MTLTextureDescriptor](mtltexturedescriptor.md)
  An object that you use to configure new Metal texture objects.
- [class MTKTextureLoader](../MetalKit/MTKTextureLoader.md)
  An object that creates textures from existing data in common image formats.
- [class MTLSharedTextureHandle](mtlsharedtexturehandle.md)
  A texture handle that can be shared across process address space boundaries.
- [enum MTLPixelFormat](mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/optimizing-texture-data)*