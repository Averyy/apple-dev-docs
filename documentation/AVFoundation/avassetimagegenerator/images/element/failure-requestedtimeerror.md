# AVAssetImageGenerator.Images.Element.failure(requestedTime:error:)

**Framework**: AVFoundation  
**Kind**: case

A result that indicates an image generation request failed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case failure(requestedTime: CMTime, error: any Error)
```

## Parameters

- `requestedTime`: A time in the video timeline at which you requested an image.
- `error`: An error that indicates the reason for the failure.

## See Also

- [AVAssetImageGenerator.Images.Element.success(requestedTime:image:actualTime:)](avassetimagegenerator/images/element/success(requestedtime:image:actualtime:).md)
  A result that indicates an image generation request succeeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element/failure(requestedtime:error:))*