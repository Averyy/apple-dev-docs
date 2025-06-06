# reducedResolution

**Framework**: MediaExtension  
**Kind**: property

A request to decode at a lower resolution than full-size.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional var reducedResolution: CGSize { get set }
```

#### Discussion

This optional property conveys a request for reduced resolution for decoding. Decoders that only support a fixed set of resolutions should pick the smallest resolution greater than or equal to the requested width and height. If the output [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) is not in a format where reduced resolution decoding is supported, this setting should be disregarded. This property is set on the extension when a Video Toolbox client sets the [`kVTDecompressionPropertyKey_ReducedResolutionDecode`](https://developer.apple.com/documentation/VideoToolbox/kVTDecompressionPropertyKey_ReducedResolutionDecode) property on the hosting [`VTDecompressionSession`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSession).

## See Also

- [var contentHasInterframeDependencies: Bool](mevideodecoder/contenthasinterframedependencies.md)
  A Boolean that specifies whether the content has interframe dependencies, if the decoder knows.
- [var recommendedThreadCount: Int](mevideodecoder/recommendedthreadcount.md)
  The recommended number of threads for the decoder to use.
- [var actualThreadCount: Int](mevideodecoder/actualthreadcount.md)
  The actual number of threads the decoder uses.
- [var supportedPixelFormatsOrderedByQuality: [NSNumber]](mevideodecoder/supportedpixelformatsorderedbyquality.md)
  Provides hints about quality tradeoffs between pixel formats.
- [var pixelFormatsWithReducedResolutionDecodeSupport: [NSNumber]](mevideodecoder/pixelformatswithreducedresolutiondecodesupport.md)
  Provides a list of output pixel formats where the decoder supports reduced resolution decoding.
- [var producesRAWOutput: Bool](mevideodecoder/producesrawoutput.md)
  Indicates whether the decoder produces RAW output which requires the use of a RAW processor.
- [var isReadyForMoreMediaData: Bool](mevideodecoder/isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the decoder to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder/reducedresolution)*