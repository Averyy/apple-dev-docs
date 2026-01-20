# encode(to:sourceTexture:histogram:histogramOffset:)

**Framework**: Metal Performance Shaders  
**Kind**: method

Encodes the filter to a command buffer using a compute command encoder.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encode(to commandBuffer: any MTLCommandBuffer, sourceTexture source: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)
```

#### Discussion

The filter will not begin to execute until after the command buffer has been enqueued and committed.

## Parameters

- `commandBuffer`: A valid command buffer.
- `source`: A valid texture containing the source image for the filter.
- `histogram`: A valid buffer to receive the histogram results.
- `histogramOffset`: The byte offset into the histogram buffer at which to write the histogram results. Must be a multiple of 32 bytes. The histogram results per channel are stored together. The number of channels for which histogram results are stored is determined by the number of channels in the image. If the   value of the   property is   and the source image is RGBA, then only histogram results for RGB channels are stored.

## See Also

- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](mpsimagehistogram/init(device:histograminfo:).md)
  Initializes a histogram with specific information.
- [struct MPSImageHistogramInfo](mpsimagehistograminfo.md)
  The information used to compute the histogram channels of an image.
- [func histogramSize(forSourceFormat: MTLPixelFormat) -> Int](mpsimagehistogram/histogramsize(forsourceformat:).md)
  The amount of space the histogram will take up in the output buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/encode(to:sourcetexture:histogram:histogramoffset:))*