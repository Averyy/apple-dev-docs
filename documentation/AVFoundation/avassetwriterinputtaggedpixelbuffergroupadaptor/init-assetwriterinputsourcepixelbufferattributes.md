# init(assetWriterInput:sourcePixelBufferAttributes:)

**Framework**: AVFoundation  
**Kind**: init

Creates an object that appends tagged buffer groups to an asset writer input.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes: [String : Any]? = nil)
```

#### Discussion

To take advantage of the improved efficiency of appending buffers created from the adaptor’s pixel buffer pool, specify pixel buffer attributes that most closely accommodate the source format of the video frames of tagged buffer groups to append.

Pixel buffer attributes keys for the pixel buffer pool are defined in `<CoreVideo/CVPixelBuffer.h>`. To specify the pixel format type, the pixel buffer attributes dictionary should contain a value for [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey). For example, specify a format of [`kCVPixelFormatType_32BGRA`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_32BGRA) for 8-bit-per-channel BGRA. See [`append(_:withPresentationTime:)`](avassetwriterinputpixelbufferadaptor/append(_:withpresentationtime:).md) in [`AVAssetWriterInputPixelBufferAdaptor`](avassetwriterinputpixelbufferadaptor.md) for more information on choosing a pixel format.

## Parameters

- `input`: It’s an error to initialize an adaptor with an asset writer input that is already attached to another instance of tagged pixel buffer group adaptor, or to one th that progresses beyond its   state.
- `sourcePixelBufferAttributes`: Specifies the attributes of pixel buffers that the adaptor’s pixel buffer pool vends. If your app doesn’t require a pixel buffer pool, this this value to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/init(assetwriterinput:sourcepixelbufferattributes:))*