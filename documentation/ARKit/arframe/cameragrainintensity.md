# cameraGrainIntensity

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A value that specifies the amount of grain present in the camera grain texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var cameraGrainIntensity: Float { get }
```

```objc
@property (nonatomic, readonly) float cameraGrainIntensity;
```

#### Discussion

This property is normalized within the range [0..1], where zero specifies no grain, and one specifies the maximum amount of grain.

When you apply this value to the depth component of the [`cameraGrainTexture`](./cameragraintexture.md), you select among variations of visual image noise data stored in the Metal texture that conceptually match this level of intensity.

## See Also

### Accessing camera data
- [var camera: ARCamera](./camera.md)
  Information about the camera position, orientation, and imaging parameters used to capture the frame.
- [var capturedImage: CVPixelBuffer](./capturedimage.md)
  A pixel buffer containing the image captured by the camera.
- [var timestamp: TimeInterval](./timestamp.md)
  The time at which the frame was captured.
- [var cameraGrainTexture: (any MTLTexture)?](./cameragraintexture.md)
  A tileable Metal texture created by ARKit to match the visual characteristics of the current video stream.
- [var exifData: [String : Any]](./exifdata.md)
  Auxiliary data for the captured image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/cameragrainintensity)*