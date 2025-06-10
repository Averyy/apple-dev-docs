# sourcePixelBufferAttributes

**Framework**: AVFoundation  
**Kind**: property

The attributes of buffers that the adaptor’s pixel buffer pool vends.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var sourcePixelBufferAttributes: [String : any Sendable]? { get }
```

#### Discussion

The value of this property is a dictionary containing pixel buffer attribute keys defined in `<CoreVideo/CVPixelBuffer.h>`.

## See Also

- [var pixelBufferPool: CVPixelBufferPool?](avassetwriterinputtaggedpixelbuffergroupadaptor/pixelbufferpool.md)
  A pixel buffer pool that vends and efficiently recycles the pixel buffers of tagged buffer groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/sourcepixelbufferattributes)*