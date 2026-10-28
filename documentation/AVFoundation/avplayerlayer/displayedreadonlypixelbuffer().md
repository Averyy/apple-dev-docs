# displayedReadOnlyPixelBuffer()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the pixel buffer which is currently being displayed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func displayedReadOnlyPixelBuffer() -> CVReadOnlyPixelBuffer?
```

## Return Value

A CVReadOnlyPixelBuffer object.

## Discussion

CVReadOnlyPixelBuffer can be nil if the current player’s rate is non-zero, displayed pixel buffer is protected, no image is currently being displayed, or if the image is unavailable.

## See Also

### Processing pixel buffers
- [var pixelBufferAttributes: [String : Any]?](./pixelbufferattributes.md)
  The attributes of the visual output that displays in the player layer during playback.
- [func displayedPixelBuffer() -> CVPixelBuffer?](./displayedpixelbuffer%28%29.md)
  Returns the pixel buffer that the player layer currently displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlayer/displayedreadonlypixelbuffer())*