# exifData

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

Auxiliary data for the captured image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
var exifData: [String : Any] { get }
```

```objc
@property (nonatomic, strong, readonly) NSDictionary<NSString *,id> * exifData;
```

## Discussion

The system’s image capture pipeline produces pixel data and auxiliary information for each exposure. The AR frame exposes this pixel data through [`capturedImage`](./capturedimage.md) and the auxilliary info through this property ([`exifData`](./exifdata.md)). Example EXIF data includes camera manufacturer, orientation, compression, resolution, exposure, and the date and time that the exposure occurred.

## See Also

### Accessing camera data
- [var camera: ARCamera](./camera.md)
  Information about the camera position, orientation, and imaging parameters used to capture the frame.
- [var capturedImage: CVPixelBuffer](./capturedimage.md)
  A pixel buffer containing the image captured by the camera.
- [var timestamp: TimeInterval](./timestamp.md)
  The time at which the frame was captured.
- [var cameraGrainIntensity: Float](./cameragrainintensity.md)
  A value that specifies the amount of grain present in the camera grain texture.
- [var cameraGrainTexture: (any MTLTexture)?](./cameragraintexture.md)
  A tileable Metal texture created by ARKit to match the visual characteristics of the current video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/exifdata)*