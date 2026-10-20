# requestedTime

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A time in the video timeline at which you request an image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var requestedTime: CMTime { get }
```

## See Also

### Accessing image data
- [var image: CGImage](./image.md)
  An image for a requested time.
- [var actualTime: CMTime](./actualtime.md)
  The actual time in the video timeline at which the image generator creates the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element/requestedtime)*