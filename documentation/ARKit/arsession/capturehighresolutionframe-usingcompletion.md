# captureHighResolutionFrame(using:completion:)

**Framework**: ARKit  
**Kind**: method

Requests a single, high resolution frame to be captured.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
func captureHighResolutionFrame(using photoSettings: AVCapturePhotoSettings?) async throws -> ARFrame
```

#### Discussion

Some video formats do not support a significantly higher still image resolution than the streaming camera resolution. Use the @c isRecommendedForHighResolutionFrameCapturing method on the video format to check if the format is recommended. For passing customized photo settings to this method, obtain a @c defaultPhotoSettings object from the video format and modify it.

## Parameters

- `photoSettings`: Custom AVCapturePhotoSettings to be used.
- `completion`: Block being called when the call completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/capturehighresolutionframe(using:completion:))*