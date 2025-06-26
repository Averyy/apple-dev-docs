# ImmersiveVideoFrame

**Framework**: Immersive Media Support  
**Kind**: struct

A type that represents an immersive video frame. An immersive video frame contains: - layout (SideBySide, OverUnder, Separate, Mono) - presentationTime: frame presentation time - pixelBuffers: an array with one or more images representing the frame.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ImmersiveVideoFrame
```

## Topics

### Operators
- [static func == (ImmersiveVideoFrame, ImmersiveVideoFrame) -> Bool](immersivevideoframe/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(leftEye: CVPixelBuffer, rightEye: CVPixelBuffer, presentationTime: CMTime)](immersivevideoframe/init(lefteye:righteye:presentationtime:).md)
  Creates a video frame from the left and right eye pixel buffers.
- [init(pixelBuffer: CVPixelBuffer, presentationTime: CMTime, layout: ImmersiveVideoFrame.VideoLayout)](immersivevideoframe/init(pixelbuffer:presentationtime:layout:).md)
  Creates a video frame with one pixelBuffer and specified layout.
### Instance Properties
- [let layout: ImmersiveVideoFrame.VideoLayout](immersivevideoframe/layout.md)
  Video layout associated with the video frame pixel buffers
- [let pixelBuffers: [CVPixelBuffer]](immersivevideoframe/pixelbuffers.md)
  An array of pixel buffers associated with this immersive frame
- [let presentationTime: CMTime](immersivevideoframe/presentationtime.md)
  Presentation timestamp associated with the pixel buffers
### Enumerations
- [ImmersiveVideoFrame.VideoLayout](immersivevideoframe/videolayout.md)
  A value specifying the layout of left and right eyes within an immersive video frame.
### Default Implementations
- [Equatable Implementations](immersivevideoframe/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideoframe)*