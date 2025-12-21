# ImmersiveVideoFrame

**Framework**: Immersive Media Support  
**Kind**: struct

A type that represents an immersive video frame. An immersive video frame contains: - layout (SideBySide, OverUnder, Separate, Mono) - presentationTime: frame presentation time - pixelBuffers: an array with one or more images representing the frame.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ImmersiveVideoFrame
```

## Topics

### Initializers
- [init(leftEye: CVPixelBuffer, rightEye: CVPixelBuffer, presentationTime: CMTime)](immersivevideoframe/init(lefteye:righteye:presentationtime:).md)
  Creates a video frame from the left and right eye pixel buffers.
- [init(pixelBuffer: CVPixelBuffer, presentationTime: CMTime, layout: ImmersiveVideoFrame.VideoLayout)](immersivevideoframe/init(pixelbuffer:presentationtime:layout:).md)
  Creates a video frame with one pixelBuffer and specified layout.
### Instance Properties
- [let layout: ImmersiveVideoFrame.VideoLayout](immersivevideoframe/layout.md)
  Video layout associated with the video frame pixel buffers.
- [let pixelBuffers: [CVPixelBuffer]](immersivevideoframe/pixelbuffers.md)
  An array of pixel buffers associated with this immersive frame.
- [let presentationTime: CMTime](immersivevideoframe/presentationtime.md)
  Presentation timestamp associated with the pixel buffers.
### Enumerations
- [ImmersiveVideoFrame.VideoLayout](immersivevideoframe/videolayout.md)
  A value that specifies the layout of left and right eyes within an immersive video frame.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideoframe)*