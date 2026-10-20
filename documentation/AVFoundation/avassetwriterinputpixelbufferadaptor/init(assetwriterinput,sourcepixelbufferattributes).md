# init(assetWriterInput:sourcePixelBufferAttributes:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a new pixel buffer adaptor to receive pixel buffers for writing to the output file.

**Availability**:
- iOS 4.1+ - Deprecated in 27.0
- iPadOS 4.1+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputPixelBufferReceiver(for:pixelBufferAttributes:) instead

## Declaration

```swift
init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes: [String : Any]? = nil)
```

```objc
- (instancetype) initWithAssetWriterInput:(AVAssetWriterInput *) input sourcePixelBufferAttributes:(NSDictionary<NSString *,id> *) sourcePixelBufferAttributes;
```

#### Discussion

To take advantage of the efficiency of appending buffers created from the adaptor’s pixel buffer pool, specify pixel buffer attributes that most closely accommodate the format of the buffers you append.

## Parameters

- `input`: An asset writer input that accepts [`video`](../avmediatype/video.md) as its media type.

  The system raises an error if you specify an input that’s already connected to a pixel buffer adaptor.
- `sourcePixelBufferAttributes`: A dictionary that describes the attributes of pixel buffers that the input’s pixel buffer pool vends. If your app doesn’t need a pixel buffer pool for allocating buffers, set this value to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/init(assetwriterinput:sourcepixelbufferattributes:))*