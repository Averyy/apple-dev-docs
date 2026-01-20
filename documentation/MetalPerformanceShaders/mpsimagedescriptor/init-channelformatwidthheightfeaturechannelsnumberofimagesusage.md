# init(channelFormat:width:height:featureChannels:numberOfImages:usage:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Creates an image descriptor for an image container with options to set texture usage and batch size (number of images).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(channelFormat: MPSImageFeatureChannelFormat, width: Int, height: Int, featureChannels: Int, numberOfImages: Int, usage: MTLTextureUsage)
```

#### Return Value

A valid [`MPSImageDescriptor`](mpsimagedescriptor.md) object.

## Parameters

- `channelFormat`: The storage format to use for each channel in the image.
- `width`: The width of the image.
- `height`: The height of the image.
- `featureChannels`: The number of feature channels per pixel.
- `numberOfImages`: The number of images for batch processing.
- `usage`: The intended usage of the underlying texture.

## See Also

- [convenience init(channelFormat: MPSImageFeatureChannelFormat, width: Int, height: Int, featureChannels: Int)](mpsimagedescriptor/init(channelformat:width:height:featurechannels:).md)
  Creates an image descriptor for a single image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/init(channelformat:width:height:featurechannels:numberofimages:usage:))*