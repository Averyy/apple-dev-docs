# pixelBuffer

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An object that contains pixel data for the rendered caption.

**Availability**:
- iOS 18.0+ - Deprecated in 27.0
- iPadOS 18.0+ - Deprecated in 27.0
- Mac Catalyst 18.0+ - Deprecated in 27.0
- macOS 15.0+ - Deprecated in 27.0

> **Deprecated**: Use readOnlyPixelBuffer instead

## Declaration

```swift
var pixelBuffer: CVPixelBuffer { get }
```

```objc
@property (nonatomic, readonly) CVPixelBufferRef pixelBuffer;
```

## See Also

### Inspecting the image
- [var readOnlyPixelBuffer: CVReadOnlyPixelBuffer](./readonlypixelbuffer.md)
  A CVReadOnlyPixelBuffer that contains pixel data for the rendered caption
- [var position: CGPoint](./position.md)
  A point that defines the position, in pixels, of the rendered caption image relative to the video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avrenderedcaptionimage/pixelbuffer)*