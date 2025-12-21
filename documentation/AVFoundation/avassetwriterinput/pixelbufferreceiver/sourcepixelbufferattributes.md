# sourcePixelBufferAttributes

**Framework**: AVFoundation  
**Kind**: property

The pixel buffer attributes of pixel buffers that will be vended by the receiver’s pixel buffer pool.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var sourcePixelBufferAttributes: CVPixelBufferCreationAttributes? { get }
```

## See Also

- [var pixelBufferPool: CVMutablePixelBuffer.Pool?](avassetwriterinput/pixelbufferreceiver/pixelbufferpool.md)
  A pixel buffer pool that will vend and efficiently recycle pixel buffer objects that can be appended to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver/sourcepixelbufferattributes)*