# AVAssetImageGenerator.Images.Element

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

An element that provides the result of an image generation request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
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
- [AVAssetImageGenerator.Images.Element.success(requestedTime:image:actualTime:)](./element/success%28requestedtime,image,actualtime%29.md)
  A result that indicates an image generation request succeeded.
- [AVAssetImageGenerator.Images.Element.failure(requestedTime:error:)](./element/failure%28requestedtime,error%29.md)
  A result that indicates an image generation request failed.
### Accessing image data
- [var image: CGImage](./element/image.md)
  An image for a requested time.
- [var requestedTime: CMTime](./element/requestedtime.md)
  A time in the video timeline at which you request an image.
- [var actualTime: CMTime](./element/actualtime.md)
  The actual time in the video timeline at which the image generator creates the image.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Iterating elements
- [func next() async -> AVAssetImageGenerator.Images.Element?](./next%28%29.md)
  Returns the next element in the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element)*