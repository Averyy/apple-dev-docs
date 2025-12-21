# AVAssetImageGenerator.Images.Element

**Framework**: AVFoundation  
**Kind**: enum

An element that provides the result of an image generation request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@frozen
enum Element
```

## Topics

### Cases
- [AVAssetImageGenerator.Images.Element.success(requestedTime:image:actualTime:)](avassetimagegenerator/images/element/success(requestedtime:image:actualtime:).md)
  A result that indicates an image generation request succeeded.
- [AVAssetImageGenerator.Images.Element.failure(requestedTime:error:)](avassetimagegenerator/images/element/failure(requestedtime:error:).md)
  A result that indicates an image generation request failed.
### Accessing image data
- [var image: CGImage](avassetimagegenerator/images/element/image.md)
  An image for a requested time.
- [var requestedTime: CMTime](avassetimagegenerator/images/element/requestedtime.md)
  A time in the video timeline at which you request an image.
- [var actualTime: CMTime](avassetimagegenerator/images/element/actualtime.md)
  The actual time in the video timeline at which the image generator creates the image.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func next() async -> AVAssetImageGenerator.Images.Element?](avassetimagegenerator/images/next.md)
  Returns the next element in the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element)*