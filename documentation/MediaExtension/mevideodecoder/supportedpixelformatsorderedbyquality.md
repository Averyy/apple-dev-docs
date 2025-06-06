# supportedPixelFormatsOrderedByQuality

**Framework**: MediaExtension  
**Kind**: property

Provides hints about quality tradeoffs between pixel formats.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional var supportedPixelFormatsOrderedByQuality: [NSNumber] { get }
```

#### Discussion

This array contains [`CMPixelFormatType`](https://developer.apple.com/documentation/CoreMedia/CMPixelFormatType) values, ordered by quality from best to worst. The system queries this property on the extension when [`Video Toolbox`](https://developer.apple.com/documentation/VideoToolbox) queries the [`kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality`](https://developer.apple.com/documentation/VideoToolbox/kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality) on the hosting [`VTDecompressionSession`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSession).

## See Also

- [var contentHasInterframeDependencies: Bool](mevideodecoder/contenthasinterframedependencies.md)
  A Boolean that specifies whether the content has interframe dependencies, if the decoder knows.
- [var recommendedThreadCount: Int](mevideodecoder/recommendedthreadcount.md)
  The recommended number of threads for the decoder to use.
- [var actualThreadCount: Int](mevideodecoder/actualthreadcount.md)
  The actual number of threads the decoder uses.
- [var reducedResolution: CGSize](mevideodecoder/reducedresolution.md)
  A request to decode at a lower resolution than full-size.
- [var pixelFormatsWithReducedResolutionDecodeSupport: [NSNumber]](mevideodecoder/pixelformatswithreducedresolutiondecodesupport.md)
  Provides a list of output pixel formats where the decoder supports reduced resolution decoding.
- [var producesRAWOutput: Bool](mevideodecoder/producesrawoutput.md)
  Indicates whether the decoder produces RAW output which requires the use of a RAW processor.
- [var isReadyForMoreMediaData: Bool](mevideodecoder/isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the decoder to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder/supportedpixelformatsorderedbyquality)*