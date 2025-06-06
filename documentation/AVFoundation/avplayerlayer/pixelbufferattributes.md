# pixelBufferAttributes

**Framework**: AVFoundation  
**Kind**: property

The attributes of the visual output that displays in the player layer during playback.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var pixelBufferAttributes: [String : Any]? { get set }
```

#### Discussion

Use this property to customize the format of the pixel buffers that the player layer vends.

## See Also

- [func displayedPixelBuffer() -> CVPixelBuffer?](avplayerlayer/displayedpixelbuffer.md)
  Returns the pixel buffer that the player layer currently displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlayer/pixelbufferattributes)*