# camera

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

Information about the camera position, orientation, and imaging parameters used to capture the frame.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
@NSCopying
var camera: ARCamera { get }
```

```objc
@property (nonatomic, copy, readonly) ARCamera * camera;
```

## See Also

### Accessing camera data
- [var capturedImage: CVPixelBuffer](./capturedimage.md)
  A pixel buffer containing the image captured by the camera.
- [var timestamp: TimeInterval](./timestamp.md)
  The time at which the frame was captured.
- [var cameraGrainIntensity: Float](./cameragrainintensity.md)
  A value that specifies the amount of grain present in the camera grain texture.
- [var cameraGrainTexture: (any MTLTexture)?](./cameragraintexture.md)
  A tileable Metal texture created by ARKit to match the visual characteristics of the current video stream.
- [var exifData: [String : Any]](./exifdata.md)
  Auxiliary data for the captured image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/camera)*