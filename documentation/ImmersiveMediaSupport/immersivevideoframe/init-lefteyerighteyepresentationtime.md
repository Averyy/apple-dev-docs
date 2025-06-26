# init(leftEye:rightEye:presentationTime:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a video frame from the left and right eye pixel buffers.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(leftEye: CVPixelBuffer, rightEye: CVPixelBuffer, presentationTime: CMTime)
```

## Parameters

- `leftEye`: leftEye pixel buffer.
- `rightEye`: rightEye pixel buffer.
- `presentationTime`: Presentation time of the video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideoframe/init(lefteye:righteye:presentationtime:))*