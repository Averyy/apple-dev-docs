# primarySample

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The primary frame sample of a camera frame.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var primarySample: CameraFrame.Sample { get }
```

## See Also

### Getting camera frame information
- [var samples: [CameraFrame.Sample]](./samples.md)
  All the camera frame samples on this frame.
- [CameraFrame.Sample](./sample.md)
  Information that describes a sample from a camera frame.
- [func sample(for: CameraFrameProvider.CameraPosition) -> CameraFrame.Sample?](./sample%28for%29.md)
  Returns the camera frame sample for a given camera position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframe/primarysample)*