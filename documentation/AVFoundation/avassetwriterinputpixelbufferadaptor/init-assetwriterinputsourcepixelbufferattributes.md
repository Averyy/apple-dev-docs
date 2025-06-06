# init(assetWriterInput:sourcePixelBufferAttributes:)

**Framework**: AVFoundation  
**Kind**: init

Creates a new pixel buffer adaptor to receive pixel buffers for writing to the output file.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes: [String : Any]? = nil)
```

#### Discussion

To take advantage of the efficiency of appending buffers created from the adaptor’s pixel buffer pool, specify pixel buffer attributes that most closely accommodate the format of the buffers you append.

## Parameters

- `input`: The system raises an error if you specify an input that’s already connected to a pixel buffer adaptor.
- `sourcePixelBufferAttributes`: A dictionary that describes the attributes of pixel buffers that the input’s pixel buffer pool vends. If your app doesn’t need a pixel buffer pool for allocating buffers, set this value to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/init(assetwriterinput:sourcepixelbufferattributes:))*