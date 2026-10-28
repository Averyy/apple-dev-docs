# producesRAWOutput

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

Indicates whether the decoder produces RAW output which requires the use of a RAW processor.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional var producesRAWOutput: Bool { get }
```

```objc
@property (readonly) BOOL producesRAWOutput;
```

## Discussion

The extension should implement this property returning [`YES`](../../ObjectiveC/yes.md) if the decoder produces RAW output which requires the use of an [`MERAWProcessor`](../merawprocessor.md) for post-decode processing to produce renderable output.

This optional property is queried on the extension when a Video Toolbox client queries the [`kVTDecompressionPropertyKey_DecoderProducesRAWOutput`](../../VideoToolbox/kvtdecompressionpropertykey_decoderproducesrawoutput.md) property on the hosting [`VTDecompressionSession`](../../VideoToolbox/vtdecompressionsession.md).

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
- [var reducedResolution: CGSize](./reducedresolution.md)
  A request to decode at a lower resolution than full-size.
- [var pixelFormatsWithReducedResolutionDecodeSupport: [NSNumber]](./pixelformatswithreducedresolutiondecodesupport.md)
  Provides a list of output pixel formats where the decoder supports reduced resolution decoding.
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the decoder to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder/producesrawoutput)*