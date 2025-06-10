# displayedReadOnlyPixelBuffer()

**Framework**: AVFoundation  
**Kind**: method

Returns the pixel buffer which is currently being displayed.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func displayedReadOnlyPixelBuffer() -> CVReadOnlyPixelBuffer?
```

#### Return Value

A CVReadOnlyPixelBuffer object.

#### Discussion

CVReadOnlyPixelBuffer can be nil if the current player’s rate is non-zero, displayed pixel buffer is protected, no image is currently being displayed, or if the image is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlayer/displayedreadonlypixelbuffer())*