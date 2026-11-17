# samples

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

All the camera frame samples on this frame.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var samples: [CameraFrame.Sample] { get }
```

## See Also

### Getting camera frame information
- [var primarySample: CameraFrame.Sample](./primarysample.md)
  The primary frame sample of a camera frame.
- [CameraFrame.Sample](./sample.md)
  Information that describes a sample from a camera frame.
- [func sample(for: CameraFrameProvider.CameraPosition) -> CameraFrame.Sample?](./sample%28for%29.md)
  Returns the camera frame sample for a given camera position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframe/samples)*