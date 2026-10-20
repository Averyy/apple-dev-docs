# AVAssetImageGenerator.Images.Element.failure(requestedTime:error:)

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

A result that indicates an image generation request failed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
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

### Cases
- [AVAssetImageGenerator.Images.Element.success(requestedTime:image:actualTime:)](./success%28requestedtime,image,actualtime%29.md)
  A result that indicates an image generation request succeeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/element/failure(requestedtime:error:))*