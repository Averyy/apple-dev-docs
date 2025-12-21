# readOnlyPixelBuffer

**Framework**: AVFoundation  
**Kind**: property

A CVReadOnlyPixelBuffer that contains pixel data for the rendered caption

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
var readOnlyPixelBuffer: CVReadOnlyPixelBuffer { get }
```

#### Discussion

The pixel format is fixed to `kCVPixelFormatType_32BGRA` defined in <CoreVideo/CVPixelBuffer.h>

## See Also

- [var pixelBuffer: CVPixelBuffer](avrenderedcaptionimage/pixelbuffer.md)
  An object that contains pixel data for the rendered caption.
- [var position: CGPoint](avrenderedcaptionimage/position.md)
  A point that defines the position, in pixels, of the rendered caption image relative to the video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avrenderedcaptionimage/readonlypixelbuffer)*