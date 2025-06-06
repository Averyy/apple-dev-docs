# description

**Framework**: ARKit  
**Kind**: property

A textual representation of this camera video format.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var description: String { get }
```

## See Also

- [var cameraPositions: [CameraFrameProvider.CameraPosition]](cameravideoformat/camerapositions.md)
  The camera positions for this video format.
- [var cameraType: CameraFrameProvider.CameraType](cameravideoformat/cameratype.md)
  The camera type for this video format.
- [var frameSize: CGSize](cameravideoformat/framesize.md)
  The frame size for this video format.
- [var pixelFormat: OSType](cameravideoformat/pixelformat.md)
  The pixel format for this video format.
- [var maxFrameDuration: Float](cameravideoformat/maxframeduration.md)
  The maximum frame duration for this video format, in seconds.
- [var minFrameDuration: Float](cameravideoformat/minframeduration.md)
  The minimum frame duration for this video format, in seconds.
- [static func supportedVideoFormats(for: CameraFrameProvider.CameraType, cameraPositions: [CameraFrameProvider.CameraPosition]) -> [CameraVideoFormat]](cameravideoformat/supportedvideoformats(for:camerapositions:).md)
  Returns the video formats the provided camera type and camera position supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameravideoformat/description)*