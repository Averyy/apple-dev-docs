# actualTime

**Framework**: AVFoundation  
**Kind**: property

The actual time in the video timeline at which the image generator creates the image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var actualTime: CMTime { get throws }
```

#### Discussion

This value may differ from the [`requestedTime`](avassetimagegenerator/images/element/requestedtime.md) depending on the configuration of the image generator’s [`requestedTimeToleranceBefore`](avassetimagegenerator/requestedtimetolerancebefore.md) and [`requestedTimeToleranceAfter`](avassetimagegenerator/requestedtimetoleranceafter.md) properties.

## See Also

- [var image: CGImage](avassetimagegenerator/images/element/image.md)
  An image for a requested time.
- [var requestedTime: CMTime](avassetimagegenerator/images/element/requestedtime.md)
  A time in the video timeline at which you request an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element/actualtime)*