# CameraFrame.Sample

**Framework**: ARKit  
**Kind**: struct

Information that describes a sample from a camera frame.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Sample
```

#### Overview

Use this structure to access information about a sample from a [`CameraFrame`](cameraframe.md), such as the frame’s settings and parameters, a pixel buffer that contains the sample’s data, and so on.

## Topics

### Inspecting camera frame samples
- [var parameters: CameraFrame.Sample.Parameters](cameraframe/sample/parameters-swift.property.md)
  The frame’s parameters.
- [CameraFrame.Sample.Parameters](cameraframe/sample/parameters-swift.struct.md)
  A frame’s parameters, such as the camera type, intrinsics, timestamps, exposure, and so on.
- [var pixelBuffer: CVPixelBuffer](cameraframe/sample/pixelbuffer.md)
### Instance Properties
- [var description: String](cameraframe/sample/description.md)
  A textual representation of this camera frame sample.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var primarySample: CameraFrame.Sample](cameraframe/primarysample.md)
  Gets the primary frame sample for a camera frame.
- [func sample(for: CameraFrameProvider.CameraPosition) -> CameraFrame.Sample?](cameraframe/sample(for:).md)
  Returns the camera frame sample for a given camera position.
- [var description: String](cameraframe/description.md)
  A textual representation of this camera frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframe/sample)*