# pixelBufferAttributes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) NSDictionary<NSString *,id> * pixelBufferAttributes;
```

## Discussion

Use this property to customize the format of the pixel buffers that the player layer vends.

## See Also

### Processing pixel buffers
- [func displayedPixelBuffer() -> CVPixelBuffer?](./displayedpixelbuffer%28%29.md)
  Returns the pixel buffer that the player layer currently displays.
- [func displayedReadOnlyPixelBuffer() -> CVReadOnlyPixelBuffer?](./displayedreadonlypixelbuffer%28%29.md)
  Returns the pixel buffer which is currently being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlayer/pixelbufferattributes)*