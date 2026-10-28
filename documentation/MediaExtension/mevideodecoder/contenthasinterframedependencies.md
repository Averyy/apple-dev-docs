# contentHasInterframeDependencies

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

A Boolean that specifies whether the content has interframe dependencies, if the decoder knows.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional var contentHasInterframeDependencies: Bool { get }
```

```objc
@property (readonly) BOOL contentHasInterframeDependencies;
```

## Discussion

The system queries this property on the extension when [Video Toolbox](../../VideoToolbox/VideoToolbox.md) queries the [`kVTDecompressionPropertyKey_ContentHasInterframeDependencies`](../../VideoToolbox/kvtdecompressionpropertykey_contenthasinterframedependencies.md) on the hosting [`VTDecompressionSession`](../../VideoToolbox/vtdecompressionsession.md).

## See Also

### Inspecting a video decoder
- [var recommendedThreadCount: Int](./recommendedthreadcount.md)
  The recommended number of threads for the decoder to use.
- [var actualThreadCount: Int](./actualthreadcount.md)
  The actual number of threads the decoder uses.
- [var supportedPixelFormatsOrderedByQuality: [NSNumber]](./supportedpixelformatsorderedbyquality.md)
  Provides hints about quality tradeoffs between pixel formats.
- [var reducedResolution: CGSize](./reducedresolution.md)
  A request to decode at a lower resolution than full-size.
- [var pixelFormatsWithReducedResolutionDecodeSupport: [NSNumber]](./pixelformatswithreducedresolutiondecodesupport.md)
  Provides a list of output pixel formats where the decoder supports reduced resolution decoding.
- [var producesRAWOutput: Bool](./producesrawoutput.md)
  Indicates whether the decoder produces RAW output which requires the use of a RAW processor.
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the decoder to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder/contenthasinterframedependencies)*