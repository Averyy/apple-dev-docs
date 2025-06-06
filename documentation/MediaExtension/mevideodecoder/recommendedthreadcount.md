# recommendedThreadCount

**Framework**: MediaExtension  
**Kind**: property

The recommended number of threads for the decoder to use.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional var recommendedThreadCount: Int { get set }
```

#### Discussion

The system sets this property on the extension when [`Video Toolbox`](https://developer.apple.com/documentation/VideoToolbox) sets [`kVTDecompressionPropertyKey_ThreadCount`](https://developer.apple.com/documentation/VideoToolbox/kVTDecompressionPropertyKey_ThreadCount) on the hosting [`VTDecompressionSession`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSession).

## See Also

- [var contentHasInterframeDependencies: Bool](mevideodecoder/contenthasinterframedependencies.md)
  A Boolean that specifies whether the content has interframe dependencies, if the decoder knows.
- [var actualThreadCount: Int](mevideodecoder/actualthreadcount.md)
  The actual number of threads the decoder uses.
- [var supportedPixelFormatsOrderedByQuality: [NSNumber]](mevideodecoder/supportedpixelformatsorderedbyquality.md)
  Provides hints about quality tradeoffs between pixel formats.
- [var reducedResolution: CGSize](mevideodecoder/reducedresolution.md)
  A request to decode at a lower resolution than full-size.
- [var pixelFormatsWithReducedResolutionDecodeSupport: [NSNumber]](mevideodecoder/pixelformatswithreducedresolutiondecodesupport.md)
  Provides a list of output pixel formats where the decoder supports reduced resolution decoding.
- [var producesRAWOutput: Bool](mevideodecoder/producesrawoutput.md)
  Indicates whether the decoder produces RAW output which requires the use of a RAW processor.
- [var isReadyForMoreMediaData: Bool](mevideodecoder/isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the decoder to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder/recommendedthreadcount)*