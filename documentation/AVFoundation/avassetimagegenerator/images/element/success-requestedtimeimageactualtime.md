# AVAssetImageGenerator.Images.Element.success(requestedTime:image:actualTime:)

**Framework**: AVFoundation  
**Kind**: case

A result that indicates an image generation request succeeded.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case success(requestedTime: CMTime, image: CGImage, actualTime: CMTime)
```

## Parameters

- `requestedTime`: A time in the video timeline at which you requested an image.
- `image`: An image for the requested time.
- `actualTime`: A time in the video timeline at which the image generator created an image.

## See Also

- [AVAssetImageGenerator.Images.Element.failure(requestedTime:error:)](avassetimagegenerator/images/element/failure(requestedtime:error:).md)
  A result that indicates an image generation request failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element/success(requestedtime:image:actualtime:))*