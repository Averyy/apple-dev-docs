# pixelFormat

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The pixel format for this video format.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var pixelFormat: OSType { get }
```

## See Also

### Getting camera video format information
- [var cameraPositions: [CameraFrameProvider.CameraPosition]](./camerapositions.md)
  The camera positions for this video format.
- [var cameraType: CameraFrameProvider.CameraType](./cameratype.md)
  The camera type for this video format.
- [var frameSize: CGSize](./framesize.md)
  The frame size for this video format.
- [var maxFrameDuration: Float](./maxframeduration.md)
  The maximum frame duration for this video format, in seconds.
- [var minFrameDuration: Float](./minframeduration.md)
  The minimum frame duration for this video format, in seconds.
- [static func supportedVideoFormats(for: CameraFrameProvider.CameraType, cameraPositions: [CameraFrameProvider.CameraPosition]) -> [CameraVideoFormat]](./supportedvideoformats%28for,camerapositions%29.md)
  Returns the video formats the provided camera type and camera position supports.
- [var description: String](./description.md)
  A textual representation of this camera video format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameravideoformat/pixelformat)*