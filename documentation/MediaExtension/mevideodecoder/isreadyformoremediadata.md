# isReadyForMoreMediaData

**Framework**: MediaExtension  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates the readiness of the decoder to accept more sample buffers.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var isReadyForMoreMediaData: Bool { get }
```

#### Discussion

Video decoders which operate asynchronously often have a fixed capacity for buffers in flight in the decoder. This property allows the decoder to signal to [`Video Toolbox`](https://developer.apple.com/documentation/VideoToolbox) that its internal buffers are full and it can’t accept more samples. The decoder needs to use [`MEVideoDecoderReadyForMoreMediaDataDidChangeNotification`](mevideodecoderreadyformoremediadatadidchangenotification.md) to notify Video Toolbox when this property changes.

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
- [var producesRAWOutput: Bool](mevideodecoder/producesrawoutput.md)
  Indicates whether the decoder produces RAW output which requires the use of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder/isreadyformoremediadata)*