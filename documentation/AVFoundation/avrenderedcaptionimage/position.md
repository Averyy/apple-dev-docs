# position

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A point that defines the position, in pixels, of the rendered caption image relative to the video frame.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var position: CGPoint { get }
```

```objc
@property (nonatomic, readonly) CGPoint position;
```

## See Also

### Inspecting the image
- [var pixelBuffer: CVPixelBuffer](./pixelbuffer.md)
  An object that contains pixel data for the rendered caption.
- [var readOnlyPixelBuffer: CVReadOnlyPixelBuffer](./readonlypixelbuffer.md)
  A CVReadOnlyPixelBuffer that contains pixel data for the rendered caption


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avrenderedcaptionimage/position)*