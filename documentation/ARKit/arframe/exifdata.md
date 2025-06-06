# exifData

**Framework**: ARKit  
**Kind**: property

Auxiliary data for the captured image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var exifData: [String : Any] { get }
```

#### Discussion

The system’s image capture pipeline produces pixel data and auxiliary information for each exposure. The AR frame exposes this pixel data through [`capturedImage`](arframe/capturedimage.md) and the auxilliary info through this property ([`exifData`](arframe/exifdata.md)). Example EXIF data includes camera manufacturer, orientation, compression, resolution, exposure, and the date and time that the exposure occurred.

## See Also

- [var camera: ARCamera](arframe/camera.md)
  Information about the camera position, orientation, and imaging parameters used to capture the frame.
- [var capturedImage: CVPixelBuffer](arframe/capturedimage.md)
  A pixel buffer containing the image captured by the camera.
- [var timestamp: TimeInterval](arframe/timestamp.md)
  The time at which the frame was captured.
- [var cameraGrainIntensity: Float](arframe/cameragrainintensity.md)
  A value that specifies the amount of grain present in the camera grain texture.
- [var cameraGrainTexture: (any MTLTexture)?](arframe/cameragraintexture.md)
  A tileable Metal texture created by ARKit to match the visual characteristics of the current video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/exifdata)*