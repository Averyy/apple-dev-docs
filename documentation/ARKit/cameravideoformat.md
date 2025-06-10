# CameraVideoFormat

**Framework**: ARKit  
**Kind**: struct

A structure that represents a camera video format.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct CameraVideoFormat
```

## Topics

### Getting camera video format information
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
- [var description: String](cameravideoformat/description.md)
  A textual representation of this camera video format.
### Instance Properties
- [var cameraRectification: CameraFrameProvider.CameraRectification](cameravideoformat/camerarectification.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CameraFrameProvider](cameraframeprovider.md)
  An object that provides camera streams.
- [struct CameraFrame](cameraframe.md)
  The representation of a camera frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameravideoformat)*