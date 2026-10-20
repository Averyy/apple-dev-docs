# actualTime

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The actual time in the video timeline at which the image generator creates the image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var actualTime: CMTime { get throws }
```

#### Discussion

This value may differ from the [`requestedTime`](./requestedtime.md) depending on the configuration of the image generator’s [`requestedTimeToleranceBefore`](../../requestedtimetolerancebefore.md) and [`requestedTimeToleranceAfter`](../../requestedtimetoleranceafter.md) properties.

## See Also

### Accessing image data
- [var image: CGImage](./image.md)
  An image for a requested time.
- [var requestedTime: CMTime](./requestedtime.md)
  A time in the video timeline at which you request an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element/actualtime)*