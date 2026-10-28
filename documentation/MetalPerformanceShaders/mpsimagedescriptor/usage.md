# usage

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

Options to specify the intended usage of the underlying texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var usage: MTLTextureUsage { get set }
```

```objc
@property (nonatomic, readwrite) MTLTextureUsage usage;
```

## Discussion

The default value is [`shaderRead`](../../Metal/mtltextureusage/shaderread.md)`|`[`shaderWrite`](../../Metal/mtltextureusage/shaderwrite.md).

## See Also

### Properties
- [var width: Int](./width.md)
  The width of the image.
- [var height: Int](./height.md)
  The height of the image.
- [var featureChannels: Int](./featurechannels.md)
  The number of feature channels per pixel.
- [var numberOfImages: Int](./numberofimages.md)
  The number of images for batch processing.
- [var pixelFormat: MTLPixelFormat](./pixelformat.md)
  The pixel format for the underlying texture.
- [var channelFormat: MPSImageFeatureChannelFormat](./channelformat.md)
  The storage format to use for each channel in the image.
- [var cpuCacheMode: MTLCPUCacheMode](./cpucachemode.md)
  The CPU cache mode of the underlying texture.
- [var storageMode: MTLStorageMode](./storagemode.md)
  The storage mode of underlying texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/usage)*