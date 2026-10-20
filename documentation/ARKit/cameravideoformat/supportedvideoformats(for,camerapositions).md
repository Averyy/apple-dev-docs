# supportedVideoFormats(for:cameraPositions:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Type Method

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

### Getting camera video format information
- [var cameraPositions: [CameraFrameProvider.CameraPosition]](./camerapositions.md)
  The camera positions for this video format.
- [var cameraType: CameraFrameProvider.CameraType](./cameratype.md)
  The camera type for this video format.
- [var frameSize: CGSize](./framesize.md)
  The frame size for this video format.
- [var pixelFormat: OSType](./pixelformat.md)
  The pixel format for this video format.
- [var maxFrameDuration: Float](./maxframeduration.md)
  The maximum frame duration for this video format, in seconds.
- [var minFrameDuration: Float](./minframeduration.md)
  The minimum frame duration for this video format, in seconds.
- [var description: String](./description.md)
  A textual representation of this camera video format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameravideoformat/supportedvideoformats(for:camerapositions:))*