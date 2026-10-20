# MPSImage

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A texture that may have more than four channels for use in convolutional neural networks.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImage
```

```objc
@interface MPSImage : NSObject
```

#### Overview

Some image types, such as those found in convolutional neural networks (CNN), differ from a standard texture in that they may have more than 4 channels per pixel. While the channels could hold RGBA data, they will more commonly hold a number of structural permutations upon an RGBA image as the neural network progresses. It is not uncommon for each pixel to have 32 or 64 channels in it.

Since a standard [`MTLTexture`](../Metal/mtltexture.md) object cannot have more than 4 channels, the additional channels are stored in slices of a 2D texture array (i.e. a texture of type [`MTLTextureType.type2DArray`](../Metal/mtltexturetype/type2darray.md)) such that 4 consecutive channels are stored in each slice of this array. If the number of feature channels is `N`, the number of array slices needed is `(N+3)/4`. For example, a 9-channel CNN image with a width of 3 and a height of 2 will be stored as follows:

![](https://developer.apple.com/tutorials/images/com.apple.metalperformanceshaders/media-2556907@2x.png)

Thus, the width and height of the underlying 2D texture array is the same as the width and height of the [`MPSImage`](./mpsimage.md) object and the array length is equal to  `(` [`featureChannels`](./mpsimagedescriptor/featurechannels.md) `+3)/4`. (Channels marked with a `?` are just for padding and should not contain `NaN` or `INF` values.)

An [`MPSImage`](./mpsimage.md) object can contain multiple CNN images for batch processing. In order to create an [`MPSImage`](./mpsimage.md) object that contains `N` images, create an [`MPSImageDescriptor`](./mpsimagedescriptor.md) object with the [`numberOfImages`](./mpsimagedescriptor/numberofimages.md) property set to `N`. The length of the 2D texture array (i.e. the number of slices) will be equal to `((` [`featureChannels`](./mpsimagedescriptor/featurechannels.md) `+3)/4)*` [`numberOfImages`](./mpsimagedescriptor/numberofimages.md), where consecutive `(featureChannels+3)/4` slices of this array represent one image.

Although an [`MPSImage`](./mpsimage.md) object can contain more than one image, the actual number of images among these processed by an [`MPSCNNKernel`](./mpscnnkernel.md) object is controlled by the `z` dimension of the [`clipRect`](./mpscnnkernel/cliprect.md) property. (A kernel processes `n=clipRect.size.depth` images from this collection.)

The starting index of the image to process from the source [`MPSImage`](./mpsimage.md) object is given by `offset.z`. The starting index of the image in the destination [`MPSImage`](./mpsimage.md) object where this processed image is written to is given by `clipRect.origin.z`. Thus, an [`MPSCNNKernel`](./mpscnnkernel.md) object takes the `n=clipRect.size.depth` image from the source at indices `[offset.z, offset.z+n]`, processes each independently, and stores the result in the destination at indices `[clipRect.origin.z, clipRect.origin.z+n]` respectively. Thus, `offset.z+n` should be `<=[source numberOfImages]`, `clipRect.origin.z+n` should be `<=[destination numberOfImages]`, and `offset.z` must be `>=0`.

For example, suppose an [`MPSCNNConvolution`](./mpscnnconvolution.md) object takes an input image with 16 channels and outputs an image with 32 channels. The number of slices needed in the source 2D texture array is 4 and the number of slices needed in the destination 2D texture array is 8. Suppose the source batch size is 5 and the destination batch size is 4. Thus, the number of source slices will be `4*5=20` and the number of destination slices will be `8*4=32`. If you want to process image 2 and 3 of the source and store the result at index 1 and 2 in the destination, you can achieve this by setting `offset.z=2`, `clipRect.origin.z=1`, and `clipRect.size.depth=2`. The [`MPSCNNConvolution`](./mpscnnconvolution.md) object will take, in this case, slices 4 and 5 of the source and produce slices 4 to 7 of the destination. Similarly, slices 6 and 7 will be used to produce slices 8 to 11 of the destination.

All [`MPSCNNKernel`](./mpscnnkernel.md) objects process images in the batch independently. That is, calling a [`MPSCNNKernel`](./mpscnnkernel.md) object on a batch is formally the same as calling it on each image in the batch sequentially. Computational and GPU work submission overhead will be amortized over more work if batch processing is used. This is especially important for better performance on small images.

If `featureChannels<=4` and `numberOfImages=1` (i.e. only one slice is needed to represent the image), the underlying metal texture type is chosen to be [`MTLTextureType.type2D`](../Metal/mtltexturetype/type2d.md) rather than [`MTLTextureType.type2DArray`](../Metal/mtltexturetype/type2darray.md) as explained above.

The framework also provides [`MPSTemporaryImage`](./mpstemporaryimage.md) objects, intended for very short-lived image data that is produced and consumed immediately in the same [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) object. They are a useful way to minimize CPU-side texture allocation costs and greatly reduce the amount of memory used by your image pipeline.

Creation of the underlying texture may occur lazily in some cases. In general, you should avoid calling the [`texture`](./mpsimage/texture.md) property to avoid materializing memory for longer than necessary. When possible, use the other [`MPSImage`](./mpsimage.md) properties to get information about the object instead.

##### The MPSImage Class

[`MTLBuffer`](../Metal/mtlbuffer.md) and [`MTLTexture`](../Metal/mtltexture.md) objects are commonly used in Metal apps and are used directly by the Metal Performance Shaders framework when possible. In apps that use CNN, kernels may need more than the four data channels that a [`MTLTexture`](../Metal/mtltexture.md) object can provide. In these cases, an [`MPSImage`](./mpsimage.md) object is used instead as an abstraction layer on top of a [`MTLTexture`](../Metal/mtltexture.md) object. When more than 4 channels are needed, additional textures in the 2D texture array are added to hold additional channels in sets of four. An [`MPSImage`](./mpsimage.md) object tracks this information as the number of *feature channels* in an image.

##### CNN Images

[`MPSCNNKernel`](./mpscnnkernel.md) objects operate on [`MPSImage`](./mpsimage.md) objects. [`MPSImage`](./mpsimage.md) objects are at their core [`MTLTexture`](../Metal/mtltexture.md) objects; however, whereas [`MTLTexture`](../Metal/mtltexture.md) objects commonly represent image or texel data, an [`MPSImage`](./mpsimage.md) object is a more abstract representation of image features. The channels within an [`MPSImage`](./mpsimage.md) do not necessarily correspond to colors in a color space (although they can, if necessary). As a result, there can be many more than four of them. Having 32 or 64 channels per pixel is not uncommon in CNN. This is achieved on the [`MTLTexture`](../Metal/mtltexture.md) object abstraction by inserting extra RGBA pixels to handle the additional feature channels (if any) beyond 4. These extra pixels are stored as multiple slices of a 2D image array. Thus, each CNN pixel in a 32-channel image is represented as 8 array slices, with 4-channels stored per-pixel in each slice. The width and height of the [`MTLTexture`](../Metal/mtltexture.md) object is the same as the width and height of the [`MPSImage`](./mpsimage.md) object. The number of slices in the [`MTLTexture`](../Metal/mtltexture.md) object is given by the number of feature channels rounded up to a multiple of 4.

[`MPSImage`](./mpsimage.md) objects can be created from existing [`MTLTexture`](../Metal/mtltexture.md) objects. They may also be created anew from an [`MPSImageDescriptor`](./mpsimagedescriptor.md) and backed with either standard texture memory, or as [`MPSTemporaryImage`](./mpstemporaryimage.md) objects using memory drawn from the framework’s internal cached texture backing store. [`MPSTemporaryImage`](./mpstemporaryimage.md) objects can provide great memory usage and CPU time savings, but come with significant restrictions that should be understood before using them. For example, their contents are only valid during the GPU-side execution of a single [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) object and can not be read from or written to by the CPU. They are provided as an efficient way to hold CNN computations that are used immediately within the scope of the same [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) object and then discarded. Concatenation is also supported by allowing you to define from which destination feature channel to start writing the output of the current layer. In this way, your app can make a large [`MPSImage`](./mpsimage.md) or [`MPSTemporaryImage`](./mpstemporaryimage.md) object and fill in parts of it with multiple layers (as long as the destination feature channel offset is a multiple of 4).

##### Supported Pixel Formats

The following table shows pixel formats supported by [`MPSImage`](./mpsimage.md).

| [`MTLPixelFormat.r8Unorm`](../Metal/mtlpixelformat/r8unorm.md) | [`MTLPixelFormat.rg8Unorm`](../Metal/mtlpixelformat/rg8unorm.md) | [`MTLPixelFormat.rgba8Unorm`](../Metal/mtlpixelformat/rgba8unorm.md) | [`MTLPixelFormat.bgra8Unorm`](../Metal/mtlpixelformat/bgra8unorm.md) |
| --- | --- | --- | --- |
| [`MTLPixelFormat.r8Unorm_srgb`](../Metal/mtlpixelformat/r8unorm_srgb.md) | [`MTLPixelFormat.rg8Unorm_srgb`](../Metal/mtlpixelformat/rg8unorm_srgb.md) | [`MTLPixelFormat.rgba8Unorm_srgb`](../Metal/mtlpixelformat/rgba8unorm_srgb.md) | [`MTLPixelFormat.bgra8Unorm_srgb`](../Metal/mtlpixelformat/bgra8unorm_srgb.md) |
| [`MTLPixelFormat.r16Unorm`](../Metal/mtlpixelformat/r16unorm.md) | [`MTLPixelFormat.rg16Unorm`](../Metal/mtlpixelformat/rg16unorm.md) | [`MTLPixelFormat.rgba16Unorm`](../Metal/mtlpixelformat/rgba16unorm.md) |  |
| [`MTLPixelFormat.r16Float`](../Metal/mtlpixelformat/r16float.md) | [`MTLPixelFormat.rg16Float`](../Metal/mtlpixelformat/rg16float.md) | [`MTLPixelFormat.rgba16Float`](../Metal/mtlpixelformat/rgba16float.md) |  |
| [`MTLPixelFormat.r32Float`](../Metal/mtlpixelformat/r32float.md) | [`MTLPixelFormat.rg32Float`](../Metal/mtlpixelformat/rg32float.md) | [`MTLPixelFormat.rgba32Float`](../Metal/mtlpixelformat/rgba32float.md) |  |

## Topics

### Initializers
- [convenience init(device: any MTLDevice, imageDescriptor: MPSImageDescriptor)](./mpsimage/init%28device,imagedescriptor%29.md)
  Initializes an empty image.
- [class MPSImageDescriptor](./mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](./mpsimage.md).
- [convenience init(texture: any MTLTexture, featureChannels: Int)](./mpsimage/init%28texture,featurechannels%29.md)
  Initializes an image from a texture. The user-allocated texture has been created for a specific number of feature channels and number of images.
- [init(parentImage: MPSImage, sliceRange: NSRange, featureChannels: Int)](./mpsimage/init%28parentimage,slicerange,featurechannels%29.md)
### Methods
- [func setPurgeableState(MPSPurgeableState) -> MPSPurgeableState](./mpsimage/setpurgeablestate%28_%29.md)
  Set (or query) the purgeable state of the image’s underlying texture.
- [enum MPSPurgeableState](./mpspurgeablestate.md)
  The purgeable state of an image’s underlying texture.
### Methods to Read and Write Raw Data
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](./mpsimage/readbytes%28_,datalayout,bytesperrow,region,featurechannelinfo,imageindex%29.md)
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](./mpsimage/readbytes%28_,datalayout,imageindex%29.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](./mpsimage/writebytes%28_,datalayout,bytesperrow,region,featurechannelinfo,imageindex%29.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](./mpsimage/writebytes%28_,datalayout,imageindex%29.md)
- [struct MPSImageReadWriteParams](./mpsimagereadwriteparams.md)
  Parameters that control reading and writing of a particular set of feature channels.
- [enum MPSDataLayout](./mpsdatalayout.md)
  Options that define how buffer data is arranged.
### Methods to Get an Image Allocator
- [class func defaultAllocator() -> any MPSImageAllocator](./mpsimage/defaultallocator%28%29.md)
- [protocol MPSImageAllocator](./mpsimageallocator.md)
### Properties
- [var device: any MTLDevice](./mpsimage/device.md)
  The device on which the image will be used.
- [var width: Int](./mpsimage/width.md)
  The formal width of the image, in pixels.
- [var height: Int](./mpsimage/height.md)
  The formal height of the image, in pixels.
- [var featureChannels: Int](./mpsimage/featurechannels.md)
  The number of feature channels per pixel.
- [var numberOfImages: Int](./mpsimage/numberofimages.md)
  The number of images for batch processing.
- [var textureType: MTLTextureType](./mpsimage/texturetype.md)
  The type of the underlying texture.
- [enum MTLTextureType](../Metal/mtltexturetype.md)
  The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [var pixelFormat: MTLPixelFormat](./mpsimage/pixelformat.md)
  The pixel format of the underlying texture.
- [enum MTLPixelFormat](../Metal/mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.
- [var precision: Int](./mpsimage/precision.md)
  The number of bits of numeric precision available for each feature channel.
- [var usage: MTLTextureUsage](./mpsimage/usage.md)
  The intended usage of the underlying texture.
- [struct MTLTextureUsage](../Metal/mtltextureusage.md)
  An enumeration for the various options that determine how you can use a texture.
- [var pixelSize: Int](./mpsimage/pixelsize.md)
  The number of bytes from the first byte of one pixel to the first byte of the next pixel, in storage order. (Includes padding.)
- [var texture: any MTLTexture](./mpsimage/texture.md)
  The underlying texture.
- [protocol MTLTexture](../Metal/mtltexture.md)
  A resource that holds formatted image data.
- [var label: String?](./mpsimage/label.md)
  A string to help identify this object.
### Instance Properties
- [var featureChannelFormat: MPSImageFeatureChannelFormat](./mpsimage/featurechannelformat.md)
- [var parent: MPSImage?](./mpsimage/parent.md)
### Instance Methods
- [func batchRepresentation() -> [MPSImage]](./mpsimage/batchrepresentation%28%29.md)
- [func batchRepresentation(withSubRange: NSRange) -> [MPSImage]](./mpsimage/batchrepresentation%28withsubrange%29.md)
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, bytesPerImage: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](./mpsimage/readbytes%28_,datalayout,bytesperrow,bytesperimage,region,featurechannelinfo,imageindex%29.md)
- [func resourceSize() -> Int](./mpsimage/resourcesize%28%29.md)
- [func subImage(withFeatureChannelRange: NSRange) -> MPSImage](./mpsimage/subimage%28withfeaturechannelrange%29.md)
- [func synchronize(on: any MTLCommandBuffer)](./mpsimage/synchronize%28on%29.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerColumn: Int, bytesPerRow: Int, bytesPerImage: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](./mpsimage/writebytes%28_,datalayout,bytespercolumn,bytesperrow,bytesperimage,region,featurechannelinfo,imageindex%29.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, bytesPerImage: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](./mpsimage/writebytes%28_,datalayout,bytesperrow,bytesperimage,region,featurechannelinfo,imageindex%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MPSTemporaryImage](./mpstemporaryimage.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Neural Networks
- [Training a Neural Network with Metal Performance Shaders](./training-a-neural-network-with-metal-performance-shaders.md)
  Use an MPS neural network graph to train a simple neural network digit classifier.
- [class MPSTemporaryImage](./mpstemporaryimage.md)
  A texture for use in convolutional neural networks that stores transient data to be used and discarded promptly.
- [Objects that Simplify the Creation of Neural Networks](./objects-that-simplify-the-creation-of-neural-networks.md)
  Simplify the creation of neural networks using networks of filter, image, and state nodes.
- [Convolutional Neural Network Kernels](./convolutional-neural-network-kernels.md)
  Build neural networks with layers.
- [Recurrent Neural Networks](./recurrent-neural-networks.md)
  Create recurrent neural networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage)*