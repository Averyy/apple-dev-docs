# producesRAWOutput

**Framework**: MediaExtension  
**Kind**: property

Indicates whether the decoder produces RAW output which requires the use of a RAW processor.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional var producesRAWOutput: Bool { get }
```

#### Discussion

The extension should implement this property returning [`YES`](https://developer.apple.com/documentation/ObjectiveC/YES) if the decoder produces RAW output which requires the use of an [`MERAWProcessor`](merawprocessor.md) for post-decode processing to produce renderable output.

This optional property is queried on the extension when a Video Toolbox client queries the [`kVTDecompressionPropertyKey_DecoderProducesRAWOutput`](https://developer.apple.com/documentation/VideoToolbox/kVTDecompressionPropertyKey_DecoderProducesRAWOutput) property on the hosting [`VTDecompressionSession`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSession).

## See Also

- [var contentHasInterframeDependencies: Bool](mevideodecoder/contenthasinterframedependencies.md)
  A Boolean that specifies whether the content has interframe dependencies, if the decoder knows.
- [var recommendedThreadCount: Int](mevideodecoder/recommendedthreadcount.md)
  The recommended number of threads for the decoder to use.
- [var actualThreadCount: Int](mevideodecoder/actualthreadcount.md)
  The actual number of threads the decoder uses.
- [var supportedPixelFormatsOrderedByQuality: [NSNumber]](mevideodecoder/supportedpixelformatsorderedbyquality.md)
  Provides hints about quality tradeoffs between pixel formats.
- [var reducedResolution: CGSize](mevideodecoder/reducedresolution.md)
  A request to decode at a lower resolution than full-size.
- [var pixelFormatsWithReducedResolutionDecodeSupport: [NSNumber]](mevideodecoder/pixelformatswithreducedresolutiondecodesupport.md)
  Provides a list of output pixel formats where the decoder supports reduced resolution decoding.
- [var isReadyForMoreMediaData: Bool](mevideodecoder/isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the decoder to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder/producesrawoutput)*