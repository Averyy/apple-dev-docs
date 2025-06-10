# MTLTextureDescriptor

**Framework**: Metal  
**Kind**: class

An object that you use to configure new Metal texture objects.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLTextureDescriptor
```

## Mentions

- [Choosing a Resource Storage Mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)
- [Setting Resource Storage Modes](setting-resource-storage-modes.md)
- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)

#### Overview

To create a new texture, first create a [`MTLTextureDescriptor`](mtltexturedescriptor.md) object and set its property values. Then, call either the [`makeTexture(descriptor:)`](mtldevice/maketexture(descriptor:).md) or [`makeTexture(descriptor:iosurface:plane:)`](mtldevice/maketexture(descriptor:iosurface:plane:).md) method of a [`MTLDevice`](mtldevice.md) object, or the [`makeTexture(descriptor:offset:bytesPerRow:)`](mtlbuffer/maketexture(descriptor:offset:bytesperrow:).md) method of a [`MTLBuffer`](mtlbuffer.md) object.

When you create a texture, Metal copies property values from the descriptor into the new texture. You can reuse a [`MTLTextureDescriptor`](mtltexturedescriptor.md) object, modifying its property values as needed, to create more [`MTLTexture`](mtltexture.md) objects, without affecting any textures you already created.

## Topics

### Creating Texture Descriptors
- [class func texture2DDescriptor(pixelFormat: MTLPixelFormat, width: Int, height: Int, mipmapped: Bool) -> MTLTextureDescriptor](mtltexturedescriptor/texture2ddescriptor(pixelformat:width:height:mipmapped:).md)
  Creates a texture descriptor object for a 2D texture.
- [class func textureCubeDescriptor(pixelFormat: MTLPixelFormat, size: Int, mipmapped: Bool) -> MTLTextureDescriptor](mtltexturedescriptor/texturecubedescriptor(pixelformat:size:mipmapped:).md)
  Creates a texture descriptor object for a cube texture.
- [class func textureBufferDescriptor(with: MTLPixelFormat, width: Int, resourceOptions: MTLResourceOptions, usage: MTLTextureUsage) -> MTLTextureDescriptor](mtltexturedescriptor/texturebufferdescriptor(with:width:resourceoptions:usage:).md)
  Creates a texture descriptor object for a texture buffer.
### Specifying Texture Attributes
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
- [var usage: MTLTextureUsage](mtltexturedescriptor/usage.md)
  Options that determine how you can use the texture.
- [var swizzle: MTLTextureSwizzleChannels](mtltexturedescriptor/swizzle.md)
  The pattern you want the GPU to apply to pixels when you read or sample pixels from the texture.
- [struct MTLTextureSwizzleChannels](mtltextureswizzlechannels.md)
  A pattern that modifies the data read or sampled from a texture by rearranging or duplicating the elements of a vector.
- [enum MTLTextureSwizzle](mtltextureswizzle.md)
  A set of options to choose from when creating a texture swizzle pattern.
- [enum MTLTextureType](mtltexturetype.md)
  The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [struct MTLTextureUsage](mtltextureusage.md)
  An enumeration for the various options that determine how you can use a texture.
### Instance Properties
- [var compressionType: MTLTextureCompressionType](mtltexturedescriptor/compressiontype.md)
- [var placementSparsePageSize: MTLSparsePageSize](mtltexturedescriptor/placementsparsepagesize.md)
  Determines the page size for a placement sparse texture.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Understanding Color-Renderable Pixel Format Sizes](understanding-color-renderable-pixel-format-sizes.md)
  Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing Texture Data](optimizing-texture-data.md)
  Optimize a texture’s data to improve GPU or CPU access.
- [protocol MTLTexture](mtltexture.md)
  A resource that holds formatted image data.
- [enum MTLTextureCompressionType](mtltexturecompressiontype.md)
- [class MTKTextureLoader](../MetalKit/MTKTextureLoader.md)
  An object that creates textures from existing data in common image formats.
- [class MTLSharedTextureHandle](mtlsharedtexturehandle.md)
  A texture handle that can be shared across process address space boundaries.
- [enum MTLPixelFormat](mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturedescriptor)*