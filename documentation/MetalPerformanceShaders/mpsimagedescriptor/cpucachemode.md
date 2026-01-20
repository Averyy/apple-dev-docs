# cpuCacheMode

**Framework**: Metal Performance Shaders  
**Kind**: property

The CPU cache mode of the underlying texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var cpuCacheMode: MTLCPUCacheMode { get set }
```

#### Discussion

The default value is [`MTLCPUCacheMode.defaultCache`](https://developer.apple.com/documentation/Metal/MTLCPUCacheMode/defaultCache).

## See Also

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
- [var storageMode: MTLStorageMode](mpsimagedescriptor/storagemode.md)
  The storage mode of underlying texture.
- [var usage: MTLTextureUsage](mpsimagedescriptor/usage.md)
  Options to specify the intended usage of the underlying texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/cpucachemode)*