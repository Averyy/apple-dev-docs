# supportedVideoFormats(for:cameraPositions:)

**Framework**: ARKit  
**Kind**: method

Returns the video formats the provided camera type and camera position supports.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func supportedVideoFormats(for cameraType: CameraFrameProvider.CameraType, cameraPositions: [CameraFrameProvider.CameraPosition]) -> [CameraVideoFormat]
```

#### Return Value

An array of camera video formats.

## Parameters

- `cameraType`: The camera type.
- `cameraPositions`: The camera position.

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
- [var description: String](cameravideoformat/description.md)
  A textual representation of this camera video format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameravideoformat/supportedvideoformats(for:camerapositions:))*