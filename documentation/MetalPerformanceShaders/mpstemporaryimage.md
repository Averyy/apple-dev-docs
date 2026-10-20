# MPSTemporaryImage

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A texture for use in convolutional neural networks that stores transient data to be used and discarded promptly.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSTemporaryImage
```

```objc
@interface MPSTemporaryImage : MPSImage
```

#### Overview

[`MPSTemporaryImage`](./mpstemporaryimage.md) objects can provide a profound reduction in the aggregate texture memory and associated CPU-side allocation cost in your app. Metal Performance Shaders achieves this by automatically identifying [`MPSTemporaryImage`](./mpstemporaryimage.md) objects that do not overlap in time over the course of a [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) object’s lifetime and can therefore reuse the same memory. [`MPSTemporaryImage`](./mpstemporaryimage.md) objects leverage an internal cache of preallocated reusable memory to hold pixel data to avoid typical memory allocation performance penalties common to ordinary [`MPSImage`](./mpsimage.md) and [`MTLTexture`](../Metal/mtltexture.md) objects.

To avoid data corruption due to aliasing, [`MPSTemporaryImage`](./mpstemporaryimage.md) objects impose some important restrictions:

- The underlying texture storage mode is [`MTLStorageMode.private`](../Metal/mtlstoragemode/private.md). You cannot, for example, use the [`getBytes(_:bytesPerRow:from:mipmapLevel:)`](../Metal/mtltexture/getbytes%28_,bytesperrow,from,mipmaplevel%29.md) or [`replace(region:mipmapLevel:withBytes:bytesPerRow:)`](../Metal/mtltexture/replace%28region,mipmaplevel,withbytes,bytesperrow%29.md) methods with them. Temporary images are strictly read and written by the GPU.
- The temporary image may be used only on a single [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) object. This limits the chronology to a single linear time stream.
- The [`readCount`](./mpstemporaryimage/readcount.md) property must be managed correctly.
- Temporary images must also adhere to the general pixel format restrictions for [`MPSImage`](./mpsimage.md) objects.

Since temporary images can only be used with a single command buffer, and can not be used off the GPU, they generally should not be kept around past the completion of their associated command buffer. The lifetime of a temporary image is typically expected to be extremely short, perhaps spanning only a few lines of code.

To keep the lifetime of the underlying texture allocation as short as possible, the texture is not allocated until the first time the [`MPSTemporaryImage`](./mpstemporaryimage.md) object is used by an [`MPSCNNKernel`](./mpscnnkernel.md) object or until the first time the [`texture`](./mpsimage/texture.md) property is read. The [`readCount`](./mpstemporaryimage/readcount.md) property serves to limit the lifetime of the texture on deallocation.

You may use the [`texture`](./mpsimage/texture.md) property with the `encode` methods of an [`MPSUnaryImageKernel`](./mpsunaryimagekernel.md) subclass, if `featureChannels<=4` and the texture conforms to the requirements of the given kernel. In such cases, the [`readCount`](./mpstemporaryimage/readcount.md) property is not modified, since the enclosing object is not available. There is no locking mechanism provided to prevent a [`MTLTexture`](../Metal/mtltexture.md) object returned from the [`texture`](./mpsimage/texture.md) property from becoming invalid when the value of the [`readCount`](./mpstemporaryimage/readcount.md) property reaches 0.

[`MPSTemporaryImage`](./mpstemporaryimage.md) objects can otherwise be used wherever [`MPSImage`](./mpsimage.md) objects are used.

##### The MPSTemporaryImage Class

The [`MPSTemporaryImage`](./mpstemporaryimage.md) class extends the [`MPSImage`](./mpsimage.md) class to provide advanced caching of unused memory, in order to increase performance and reduce memory footprint. [`MPSTemporaryImage`](./mpstemporaryimage.md) objects are intended as fast GPU-only storage for intermediate image data needed only transiently within a single [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) object. They accelerate the common case of image data which is created only to be consumed and destroyed immediately by the next operation(s) encoded in a command buffer. [`MPSTemporaryImage`](./mpstemporaryimage.md) objects provide a convenient and simple way to save memory by automatically aliasing other [`MPSTemporaryImage`](./mpstemporaryimage.md) objects in the same command buffer. Because they alias (i.e., share texel storage with) other textures in the same command buffer, the valid lifetime of the data in an [`MPSTemporaryImage`](./mpstemporaryimage.md) object is extremely short, limited to a portion of a the command buffer itself.

You can not read or write data to an [`MPSTemporaryImage`](./mpstemporaryimage.md) using the CPU, or use the data in other [`MTLCommandBuffer`](../Metal/mtlcommandbuffer.md) objects. Use regular [`MPSImage`](./mpsimage.md) objects for more persistent storage.

## Topics

### Initializers
- [convenience init(commandBuffer: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor)](./mpstemporaryimage/init%28commandbuffer,imagedescriptor%29.md)
  Initializes a temporary image for use on a command buffer.
- [class MPSImageDescriptor](./mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](./mpsimage.md).
- [convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor)](./mpstemporaryimage/init%28commandbuffer,texturedescriptor%29.md)
  Low-level interface for creating a temporary image using a texture descriptor.
- [class MTLTextureDescriptor](../Metal/mtltexturedescriptor.md)
  An instance that you use to configure new Metal texture instances.
- [convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor, featureChannels: Int)](./mpstemporaryimage/init%28commandbuffer,texturedescriptor,featurechannels%29.md)
### Methods
- [class func prefetchStorage(with: any MTLCommandBuffer, imageDescriptorList: [MPSImageDescriptor])](./mpstemporaryimage/prefetchstorage%28with,imagedescriptorlist%29.md)
  A method that helps the framework decide which allocations to make ahead of time.
### Methods to Get an Image Allocator
- [class func defaultAllocator() -> any MPSImageAllocator](./mpstemporaryimage/defaultallocator%28%29.md)
- [protocol MPSImageAllocator](./mpsimageallocator.md)
### Properties
- [var readCount: Int](./mpstemporaryimage/readcount.md)
  The number of times a temporary image may be read by a CNN kernel before its contents become undefined.

## Relationships

### Inherits From
- [MPSImage](./mpsimage.md)
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
- [class MPSImage](./mpsimage.md)
  A texture that may have more than four channels for use in convolutional neural networks.
- [Objects that Simplify the Creation of Neural Networks](./objects-that-simplify-the-creation-of-neural-networks.md)
  Simplify the creation of neural networks using networks of filter, image, and state nodes.
- [Convolutional Neural Network Kernels](./convolutional-neural-network-kernels.md)
  Build neural networks with layers.
- [Recurrent Neural Networks](./recurrent-neural-networks.md)
  Create recurrent neural networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage)*