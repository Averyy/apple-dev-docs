# CameraFrame

**Framework**: ARKit  
**Kind**: struct

The representation of a camera frame.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct CameraFrame
```

## Topics

### Getting camera frame information
- [var primarySample: CameraFrame.Sample](cameraframe/primarysample.md)
  Gets the primary frame sample for a camera frame.
- [CameraFrame.Sample](cameraframe/sample.md)
  Information that describes a sample from a camera frame.
- [func sample(for: CameraFrameProvider.CameraPosition) -> CameraFrame.Sample?](cameraframe/sample(for:).md)
  Returns the camera frame sample for a given camera position.
- [var description: String](cameraframe/description.md)
  A textual representation of this camera frame.
### Instance Properties
- [var samples: [CameraFrame.Sample]](cameraframe/samples.md)
  All the camera frame samples on this frame.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CameraFrameProvider](cameraframeprovider.md)
  An object that provides camera streams.
- [struct CameraVideoFormat](cameravideoformat.md)
  A structure that represents a camera video format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframe)*