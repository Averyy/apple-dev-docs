# timestamp

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The time at which the frame was captured.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var timestamp: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval timestamp;
```

## See Also

### Accessing camera data
- [var camera: ARCamera](./camera.md)
  Information about the camera position, orientation, and imaging parameters used to capture the frame.
- [var capturedImage: CVPixelBuffer](./capturedimage.md)
  A pixel buffer containing the image captured by the camera.
- [var cameraGrainIntensity: Float](./cameragrainintensity.md)
  A value that specifies the amount of grain present in the camera grain texture.
- [var cameraGrainTexture: (any MTLTexture)?](./cameragraintexture.md)
  A tileable Metal texture created by ARKit to match the visual characteristics of the current video stream.
- [var exifData: [String : Any]](./exifdata.md)
  Auxiliary data for the captured image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/timestamp)*