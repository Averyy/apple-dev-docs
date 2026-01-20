# MPSTemporaryImage

**Framework**: Metal Performance Shaders  
**Kind**: class

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

#### Overview

[`MPSTemporaryImage`](mpstemporaryimage.md) objects can provide a profound reduction in the aggregate texture memory and associated CPU-side allocation cost in your app. Metal Performance Shaders achieves this by automatically identifying [`MPSTemporaryImage`](mpstemporaryimage.md) objects that do not overlap in time over the course of a [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) object’s lifetime and can therefore reuse the same memory. [`MPSTemporaryImage`](mpstemporaryimage.md) objects leverage an internal cache of preallocated reusable memory to hold pixel data to avoid typical memory allocation performance penalties common to ordinary [`MPSImage`](mpsimage.md) and [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) objects.

To avoid data corruption due to aliasing, [`MPSTemporaryImage`](mpstemporaryimage.md) objects impose some important restrictions:

- The underlying texture storage mode is [`MTLStorageMode.private`](https://developer.apple.com/documentation/Metal/MTLStorageMode/private). You cannot, for example, use the [`getBytes(_:bytesPerRow:from:mipmapLevel:)`](https://developer.apple.com/documentation/Metal/MTLTexture/getBytes(_:bytesPerRow:from:mipmapLevel:)) or [`replace(region:mipmapLevel:withBytes:bytesPerRow:)`](https://developer.apple.com/documentation/Metal/MTLTexture/replace(region:mipmapLevel:withBytes:bytesPerRow:)) methods with them. Temporary images are strictly read and written by the GPU.
- The temporary image may be used only on a single [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) object. This limits the chronology to a single linear time stream.
- The [`readCount`](mpstemporaryimage/readcount.md) property must be managed correctly.
- Temporary images must also adhere to the general pixel format restrictions for [`MPSImage`](mpsimage.md) objects.

Since temporary images can only be used with a single command buffer, and can not be used off the GPU, they generally should not be kept around past the completion of their associated command buffer. The lifetime of a temporary image is typically expected to be extremely short, perhaps spanning only a few lines of code.

To keep the lifetime of the underlying texture allocation as short as possible, the texture is not allocated until the first time the [`MPSTemporaryImage`](mpstemporaryimage.md) object is used by an [`MPSCNNKernel`](mpscnnkernel.md) object or until the first time the [`texture`](mpsimage/texture.md) property is read. The [`readCount`](mpstemporaryimage/readcount.md) property serves to limit the lifetime of the texture on deallocation.

You may use the [`texture`](mpsimage/texture.md) property with the `encode` methods of an [`MPSUnaryImageKernel`](mpsunaryimagekernel.md) subclass, if `featureChannels<=4` and the texture conforms to the requirements of the given kernel. In such cases, the [`readCount`](mpstemporaryimage/readcount.md) property is not modified, since the enclosing object is not available. There is no locking mechanism provided to prevent a [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) object returned from the [`texture`](mpsimage/texture.md) property from becoming invalid when the value of the [`readCount`](mpstemporaryimage/readcount.md) property reaches 0.

[`MPSTemporaryImage`](mpstemporaryimage.md) objects can otherwise be used wherever [`MPSImage`](mpsimage.md) objects are used.

##### The Mpstemporaryimage Class

The [`MPSTemporaryImage`](mpstemporaryimage.md) class extends the [`MPSImage`](mpsimage.md) class to provide advanced caching of unused memory, in order to increase performance and reduce memory footprint. [`MPSTemporaryImage`](mpstemporaryimage.md) objects are intended as fast GPU-only storage for intermediate image data needed only transiently within a single [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) object. They accelerate the common case of image data which is created only to be consumed and destroyed immediately by the next operation(s) encoded in a command buffer. [`MPSTemporaryImage`](mpstemporaryimage.md) objects provide a convenient and simple way to save memory by automatically aliasing other [`MPSTemporaryImage`](mpstemporaryimage.md) objects in the same command buffer. Because they alias (i.e., share texel storage with) other textures in the same command buffer, the valid lifetime of the data in an [`MPSTemporaryImage`](mpstemporaryimage.md) object is extremely short, limited to a portion of a the command buffer itself.

You can not read or write data to an [`MPSTemporaryImage`](mpstemporaryimage.md) using the CPU, or use the data in other [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) objects. Use regular [`MPSImage`](mpsimage.md) objects for more persistent storage.

## Topics

### Initializers
- [convenience init(commandBuffer: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor)](mpstemporaryimage/init(commandbuffer:imagedescriptor:).md)
  Initializes a temporary image for use on a command buffer.
- [class MPSImageDescriptor](mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](mpsimage.md).
- [convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor)](mpstemporaryimage/init(commandbuffer:texturedescriptor:).md)
  Low-level interface for creating a temporary image using a texture descriptor.
- [class MTLTextureDescriptor](../Metal/MTLTextureDescriptor.md)
  An instance that you use to configure new Metal texture instances.
- [convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor, featureChannels: Int)](mpstemporaryimage/init(commandbuffer:texturedescriptor:featurechannels:).md)
### Methods
- [class func prefetchStorage(with: any MTLCommandBuffer, imageDescriptorList: [MPSImageDescriptor])](mpstemporaryimage/prefetchstorage(with:imagedescriptorlist:).md)
  A method that helps the framework decide which allocations to make ahead of time.
### Methods to Get an Image Allocator
- [class func defaultAllocator() -> any MPSImageAllocator](mpstemporaryimage/defaultallocator.md)
- [protocol MPSImageAllocator](mpsimageallocator.md)
### Properties
- [var readCount: Int](mpstemporaryimage/readcount.md)
  The number of times a temporary image may be read by a CNN kernel before its contents become undefined.

## Relationships

### Inherits From
- [MPSImage](mpsimage.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Training a Neural Network with Metal Performance Shaders](training-a-neural-network-with-metal-performance-shaders.md)
  Use an MPS neural network graph to train a simple neural network digit classifier.
- [class MPSImage](mpsimage.md)
  A texture that may have more than four channels for use in convolutional neural networks.
- [Objects that Simplify the Creation of Neural Networks](objects-that-simplify-the-creation-of-neural-networks.md)
  Simplify the creation of neural networks using networks of filter, image, and state nodes.
- [Convolutional Neural Network Kernels](convolutional-neural-network-kernels.md)
  Build neural networks with layers.
- [Recurrent Neural Networks](recurrent-neural-networks.md)
  Create recurrent neural networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage)*