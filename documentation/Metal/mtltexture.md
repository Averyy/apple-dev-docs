# MTLTexture

**Framework**: Metal  
**Kind**: protocol

A resource that holds formatted image data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLTexture : MTLResource
```

## Mentions

- [Setting Resource Storage Modes](setting-resource-storage-modes.md)
- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)
- [Creating a Mipmapped Texture](creating-a-mipmapped-texture.md)
- [Choosing a Resource Storage Mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Overview

Don’t implement this protocol yourself; instead, use one of the following methods to create a [`MTLTexture`](mtltexture.md) instance:

- Create an [`MTLTextureDescriptor`](mtltexturedescriptor.md) instance to describe the texture’s properties and then call the [`makeTexture(descriptor:)`](mtldevice/maketexture(descriptor:).md) method of the [`MTLDevice`](mtldevice.md) protocol to create the texture.
- To create a texture that uses an existing [`IOSurface`](https://developer.apple.com/documentation/IOSurface/IOSurface) to hold the texture data, create an [`MTLTextureDescriptor`](mtltexturedescriptor.md) instance to describe the image data in the surface. Call the [`makeTexture(descriptor:iosurface:plane:)`](mtldevice/maketexture(descriptor:iosurface:plane:).md) method to create the texture.
- To create a texture that reinterprets another texture’s data as if it has a different format, call one of the following texture methods: - [`makeTextureView(pixelFormat:)`](mtltexture/maketextureview(pixelformat:).md)
- [`makeTextureView(pixelFormat:textureType:levels:slices:)`](mtltexture/maketextureview(pixelformat:texturetype:levels:slices:).md) (Swift)
- [`newTextureViewWithPixelFormat:textureType:levels:slices:`](mtltexture/newtextureviewwithpixelformat:texturetype:levels:slices:.md) (Objective-C) You need to choose a pixel format for the new texture compatible with the source texture’s pixel format. The new texture shares the same storage allocation as the source texture. If you make changes to the new texture, the source texture reflects those changes, and vice versa.
- To create a texture that uses an [`MTLBuffer`](mtlbuffer.md) instance’s contents to hold pixel data, create an [`MTLTextureDescriptor`](mtltexturedescriptor.md) object to describe the texture’s properties. Then call the [`makeTexture(descriptor:offset:bytesPerRow:)`](mtlbuffer/maketexture(descriptor:offset:bytesperrow:).md) method on the buffer object. The new texture object shares the storage allocation of the source buffer object. If you make changes to the texture, the buffer reflects those changes, and vice versa.

After you create a [`MTLTexture`](mtltexture.md) object, most of its characteristics, such as its size, type, and pixel format are all immutable. Only the texture’s pixel data is mutable.

To copy pixel data from system memory into the texture, call [`replace(region:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:)`](mtltexture/replace(region:mipmaplevel:slice:withbytes:bytesperrow:bytesperimage:).md) or [`replace(region:mipmapLevel:withBytes:bytesPerRow:)`](mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:).md).

To copy pixel data back to system memory, call [`getBytes(_:bytesPerRow:bytesPerImage:from:mipmapLevel:slice:)`](mtltexture/getbytes(_:bytesperrow:bytesperimage:from:mipmaplevel:slice:).md) or [`getBytes(_:bytesPerRow:from:mipmapLevel:)`](mtltexture/getbytes(_:bytesperrow:from:mipmaplevel:).md).

## Topics

### Copying Data into a Texture Image
- [func replace(region: MTLRegion, mipmapLevel: Int, slice: Int, withBytes: UnsafeRawPointer, bytesPerRow: Int, bytesPerImage: Int)](mtltexture/replace(region:mipmaplevel:slice:withbytes:bytesperrow:bytesperimage:).md)
  Copies pixel data into a section of a texture slice.
- [func replace(region: MTLRegion, mipmapLevel: Int, withBytes: UnsafeRawPointer, bytesPerRow: Int)](mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:).md)
  Copies a block of pixels into a section of texture slice 0.
### Copying Data from a Texture Image
- [func getBytes(UnsafeMutableRawPointer, bytesPerRow: Int, bytesPerImage: Int, from: MTLRegion, mipmapLevel: Int, slice: Int)](mtltexture/getbytes(_:bytesperrow:bytesperimage:from:mipmaplevel:slice:).md)
  Copies pixel data from the texture to a buffer in system memory.
- [func getBytes(UnsafeMutableRawPointer, bytesPerRow: Int, from: MTLRegion, mipmapLevel: Int)](mtltexture/getbytes(_:bytesperrow:from:mipmaplevel:).md)
  Copies pixel data from the first slice of the texture to a buffer in system memory.
### Creating Textures by Reinterpreting Existing Texture Data
- [func makeTextureView(pixelFormat: MTLPixelFormat) -> (any MTLTexture)?](mtltexture/maketextureview(pixelformat:).md)
  Creates a new view of the texture, reinterpreting its data using a different pixel format.
- [func makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels: Range<Int>, slices: Range<Int>) -> (any MTLTexture)?](mtltexture/maketextureview(pixelformat:texturetype:levels:slices:).md)
  Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.
- [func makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels: Range<Int>, slices: Range<Int>, swizzle: MTLTextureSwizzleChannels) -> (any MTLTexture)?](mtltexture/maketextureview(pixelformat:texturetype:levels:slices:swizzle:).md)
  Creates a new view of the texture, reinterpreting a subset of its data using a different type, pixel format, and swizzle pattern.
### Querying Texture Attributes
- [var textureType: MTLTextureType](mtltexture/texturetype.md)
  The dimension and arrangement of the texture image data.
- [var pixelFormat: MTLPixelFormat](mtltexture/pixelformat.md)
  The format of pixels in the texture.
- [var width: Int](mtltexture/width.md)
  The width of the texture image for the base level mipmap, in pixels.
- [var height: Int](mtltexture/height.md)
  The height of the texture image for the base level mipmap, in pixels.
- [var depth: Int](mtltexture/depth.md)
  The depth of the texture image for the base level mipmap, in pixels.
- [var mipmapLevelCount: Int](mtltexture/mipmaplevelcount.md)
  The number of mipmap levels in the texture.
- [var arrayLength: Int](mtltexture/arraylength.md)
  The number of slices in the texture array.
- [var sampleCount: Int](mtltexture/samplecount.md)
  The number of samples in each pixel.
- [var isFramebufferOnly: Bool](mtltexture/isframebufferonly.md)
  A Boolean value that indicates whether the texture can only be used as a render target.
- [var usage: MTLTextureUsage](mtltexture/usage.md)
  Options that determine how you can use the texture.
- [var allowGPUOptimizedContents: Bool](mtltexture/allowgpuoptimizedcontents.md)
  A Boolean value indicating whether the GPU is allowed to adjust the contents of the texture to improve GPU performance.
- [var isShareable: Bool](mtltexture/isshareable.md)
  A Boolean indicating whether this texture can be shared with other processes.
- [var swizzle: MTLTextureSwizzleChannels](mtltexture/swizzle.md)
  The pattern that the GPU applies to pixels when you read or sample pixels from the texture.
- [enum MTLTextureType](mtltexturetype.md)
  The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [struct MTLTextureUsage](mtltextureusage.md)
  An enumeration for the various options that determine how you can use a texture.
### Getting Information about the IOSurface the Texture Was Created From
- [var iosurface: IOSurfaceRef?](mtltexture/iosurface.md)
  A reference to the underlying surface instance for the texture, if applicable.
- [var iosurfacePlane: Int](mtltexture/iosurfaceplane.md)
  The number of a plane within the underlying surface instance for the texture, if applicable.
### Getting Information about Ancestor Resources
- [var parent: (any MTLTexture)?](mtltexture/parent.md)
  The parent texture used to create this texture, if any.
- [var parentRelativeLevel: Int](mtltexture/parentrelativelevel.md)
  The base level of the parent texture used to create this texture.
- [var parentRelativeSlice: Int](mtltexture/parentrelativeslice.md)
  The base slice of the parent texture used to create this texture.
- [var buffer: (any MTLBuffer)?](mtltexture/buffer.md)
  The source buffer used to create this texture, if any.
- [var bufferOffset: Int](mtltexture/bufferoffset.md)
  The offset in the source buffer where the texture’s data comes from.
- [var bufferBytesPerRow: Int](mtltexture/bufferbytesperrow.md)
  The number of bytes in each row of the texture’s source buffer.
- [var rootResource: (any MTLResource)?](mtltexture/rootresource.md)
  The resource that owns the storage for this texture.
### Creating a Shared Texture Handle
- [func makeSharedTextureHandle() -> MTLSharedTextureHandle?](mtltexture/makesharedtexturehandle.md)
  Creates a new texture handle from a shareable texture.
### Creating Views of Textures on Other GPUs
- [func makeRemoteTextureView(any MTLDevice) -> (any MTLTexture)?](mtltexture/makeremotetextureview(_:).md)
  Creates a remote texture view for another GPU in the same peer group.
- [var remoteStorageTexture: (any MTLTexture)?](mtltexture/remotestoragetexture.md)
  The texture on another GPU that the texture was created from, if any.
### Querying Sparse Properties
- [var isSparse: Bool](mtltexture/issparse.md)
  A Boolean value that indicates whether this is a sparse texture.
- [var firstMipmapInTail: Int](mtltexture/firstmipmapintail.md)
  The index of the first mipmap in the tail.
- [var tailSizeInBytes: Int](mtltexture/tailsizeinbytes.md)
  The size of the sparse texture tail, in bytes.
### Instance Properties
- [var compressionType: MTLTextureCompressionType](mtltexture/compressiontype.md)
- [var gpuResourceID: MTLResourceID](mtltexture/gpuresourceid.md)

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [MTLResource](mtlresource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Understanding Color-Renderable Pixel Format Sizes](understanding-color-renderable-pixel-format-sizes.md)
  Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing Texture Data](optimizing-texture-data.md)
  Optimize a texture’s data to improve GPU or CPU access.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture)*