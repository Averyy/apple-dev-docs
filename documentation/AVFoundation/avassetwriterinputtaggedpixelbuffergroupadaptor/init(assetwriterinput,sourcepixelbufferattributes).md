# init(assetWriterInput:sourcePixelBufferAttributes:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates an object that appends tagged buffer groups to an asset writer input.

**Availability**:
- iOS 17.0+ - Deprecated in 27.0
- iPadOS 17.0+ - Deprecated in 27.0
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputTaggedPixelBufferGroupReceiver(for:pixelBufferAttributes:) instead

## Declaration

```swift
init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes: [String : Any]? = nil)
```

```objc
- (instancetype) initWithAssetWriterInput:(AVAssetWriterInput *) input sourcePixelBufferAttributes:(NSDictionary<NSString *,id> *) sourcePixelBufferAttributes;
```

## Discussion

To take advantage of the improved efficiency of appending buffers created from the adaptor’s pixel buffer pool, specify pixel buffer attributes that most closely accommodate the source format of the video frames of tagged buffer groups to append.

Pixel buffer attributes keys for the pixel buffer pool are defined in `<CoreVideo/CVPixelBuffer.h>`. To specify the pixel format type, the pixel buffer attributes dictionary should contain a value for [`kCVPixelBufferPixelFormatTypeKey`](../../CoreVideo/kcvpixelbufferpixelformattypekey.md). For example, specify a format of [`kCVPixelFormatType_32BGRA`](../../CoreVideo/kcvpixelformattype_32bgra.md) for 8-bit-per-channel BGRA. See [`append(_:withPresentationTime:)`](../avassetwriterinputpixelbufferadaptor/append%28_,withpresentationtime%29.md) in [`AVAssetWriterInputPixelBufferAdaptor`](../avassetwriterinputpixelbufferadaptor.md) for more information on choosing a pixel format.

## Parameters

- `input`: An asset writer input, that handles media data of type [`video`](../avmediatype/video.md), to use for appending tagged buffer groups.

  It’s an error to initialize an adaptor with an asset writer input that is already attached to another instance of tagged pixel buffer group adaptor, or to one th that progresses beyond its [`AVAssetWriter.Status.unknown`](../avassetwriter/status-swift.enum/unknown.md) state.
- `sourcePixelBufferAttributes`: Specifies the attributes of pixel buffers that the adaptor’s pixel buffer pool vends. If your app doesn’t require a pixel buffer pool, this this value to `nil`.

## See Also

### Creating an adaptor
- [+ assetWriterInputTaggedPixelBufferGroupAdaptorWithAssetWriterInput:sourcePixelBufferAttributes:](./assetwriterinputtaggedpixelbuffergroupadaptorwithassetwriterinput_sourcepixelbufferattributes_.md)
  Returns a new object that appends tagged buffer groups to an asset writer input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/init(assetwriterinput:sourcepixelbufferattributes:))*