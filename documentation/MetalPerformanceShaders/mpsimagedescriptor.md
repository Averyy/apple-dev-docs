# MPSImageDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

A description of the attributes used to create an [`MPSImage`](mpsimage.md).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageDescriptor
```

#### Overview

You use an [`MPSImageDescriptor`](mpsimagedescriptor.md) to describe and create the properties of an [`MPSImage`](mpsimage.md) such as its size, pixel format and CPU cache mode.

## Topics

### Methods
- [convenience init(channelFormat: MPSImageFeatureChannelFormat, width: Int, height: Int, featureChannels: Int)](mpsimagedescriptor/init(channelformat:width:height:featurechannels:).md)
  Creates an image descriptor for a single image.
- [convenience init(channelFormat: MPSImageFeatureChannelFormat, width: Int, height: Int, featureChannels: Int, numberOfImages: Int, usage: MTLTextureUsage)](mpsimagedescriptor/init(channelformat:width:height:featurechannels:numberofimages:usage:).md)
  Creates an image descriptor for an image container with options to set texture usage and batch size (number of images).
### Properties
- [var width: Int](mpsimagedescriptor/width.md)
  The width of the image.
- [var height: Int](mpsimagedescriptor/height.md)
  The height of the image.
- [var featureChannels: Int](mpsimagedescriptor/featurechannels.md)
  The number of feature channels per pixel.
- [var numberOfImages: Int](mpsimagedescriptor/numberofimages.md)
  The number of images for batch processing.
- [var pixelFormat: MTLPixelFormat](mpsimagedescriptor/pixelformat.md)
  The pixel format for the underlying texture.
- [var channelFormat: MPSImageFeatureChannelFormat](mpsimagedescriptor/channelformat.md)
  The storage format to use for each channel in the image.
- [var cpuCacheMode: MTLCPUCacheMode](mpsimagedescriptor/cpucachemode.md)
  The CPU cache mode of the underlying texture.
- [var storageMode: MTLStorageMode](mpsimagedescriptor/storagemode.md)
  The storage mode of underlying texture.
- [var usage: MTLTextureUsage](mpsimagedescriptor/usage.md)
  Options to specify the intended usage of the underlying texture.
### Instance Methods
- [func copy(with: NSZone?) -> Self](mpsimagedescriptor/copy(with:).md)

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

- [convenience init(device: any MTLDevice, imageDescriptor: MPSImageDescriptor)](mpsimage/init(device:imagedescriptor:).md)
  Initializes an empty image.
- [convenience init(texture: any MTLTexture, featureChannels: Int)](mpsimage/init(texture:featurechannels:).md)
  Initializes an image from a texture. The user-allocated texture has been created for a specific number of feature channels and number of images.
- [init(parentImage: MPSImage, sliceRange: NSRange, featureChannels: Int)](mpsimage/init(parentimage:slicerange:featurechannels:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor)*