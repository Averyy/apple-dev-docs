# timestamp

**Framework**: ARKit  
**Kind**: property

The time at which the frame was captured.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var timestamp: TimeInterval { get }
```

## See Also

- [var camera: ARCamera](arframe/camera.md)
  Information about the camera position, orientation, and imaging parameters used to capture the frame.
- [var capturedImage: CVPixelBuffer](arframe/capturedimage.md)
  A pixel buffer containing the image captured by the camera.
- [var cameraGrainIntensity: Float](arframe/cameragrainintensity.md)
  A value that specifies the amount of grain present in the camera grain texture.
- [var cameraGrainTexture: (any MTLTexture)?](arframe/cameragraintexture.md)
  A tileable Metal texture created by ARKit to match the visual characteristics of the current video stream.
- [var exifData: [String : Any]](arframe/exifdata.md)
  Auxiliary data for the captured image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/timestamp)*