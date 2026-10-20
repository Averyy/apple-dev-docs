# reducedResolution

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

A request to decode at a lower resolution than full-size.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional var reducedResolution: CGSize { get set }
```

```objc
@property (readwrite) CGSize reducedResolution;
```

#### Discussion

This optional property conveys a request for reduced resolution for decoding. Decoders that only support a fixed set of resolutions should pick the smallest resolution greater than or equal to the requested width and height. If the output [CVPixelBuffer](../../CoreVideo/cvpixelbuffer-q2e.md) is not in a format where reduced resolution decoding is supported, this setting should be disregarded. This property is set on the extension when a Video Toolbox client sets the [`kVTDecompressionPropertyKey_ReducedResolutionDecode`](../../VideoToolbox/kvtdecompressionpropertykey_reducedresolutiondecode.md) property on the hosting [`VTDecompressionSession`](../../VideoToolbox/vtdecompressionsession.md).

## See Also

### Inspecting a video decoder
- [var contentHasInterframeDependencies: Bool](./contenthasinterframedependencies.md)
  A Boolean that specifies whether the content has interframe dependencies, if the decoder knows.
- [var recommendedThreadCount: Int](./recommendedthreadcount.md)
  The recommended number of threads for the decoder to use.
- [var actualThreadCount: Int](./actualthreadcount.md)
  The actual number of threads the decoder uses.
- [var supportedPixelFormatsOrderedByQuality: [NSNumber]](./supportedpixelformatsorderedbyquality.md)
  Provides hints about quality tradeoffs between pixel formats.
- [var pixelFormatsWithReducedResolutionDecodeSupport: [NSNumber]](./pixelformatswithreducedresolutiondecodesupport.md)
  Provides a list of output pixel formats where the decoder supports reduced resolution decoding.
- [var producesRAWOutput: Bool](./producesrawoutput.md)
  Indicates whether the decoder produces RAW output which requires the use of a RAW processor.
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the decoder to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder/reducedresolution)*