# pixelBufferPool

**Framework**: AVFoundation  
**Kind**: property

A pixel buffer pool that will vend and efficiently recycle pixel buffer objects that can be appended to the receiver.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var pixelBufferPool: CVMutablePixelBuffer.Pool? { get }
```

## See Also

- [var sourcePixelBufferAttributes: CVPixelBufferCreationAttributes?](avassetwriterinput/taggedpixelbuffergroupreceiver/sourcepixelbufferattributes.md)
  The pixel buffer attributes of pixel buffers that will be vended by the receiver’s pixel buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/pixelbufferpool)*