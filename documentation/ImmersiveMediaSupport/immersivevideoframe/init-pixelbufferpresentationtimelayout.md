# init(pixelBuffer:presentationTime:layout:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a video frame with one pixelBuffer and specified layout.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(pixelBuffer: CVPixelBuffer, presentationTime: CMTime, layout: ImmersiveVideoFrame.VideoLayout = .sideBySide)
```

## Parameters

- `pixelBuffer`: pixelBuffer containing the video frame.
- `presentationTime`: Presentation time of the video frame.
- `layout`: How left and right eye is packed into the pixelBuffer. See   for the valid options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideoframe/init(pixelbuffer:presentationtime:layout:))*