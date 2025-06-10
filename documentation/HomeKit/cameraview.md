# CameraView

**Framework**: HomeKit  
**Kind**: struct

A SwiftUI view into which a video stream or an image snapshot is rendered.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency struct CameraView
```

## Topics

### Creating a camera view
- [init(source: HMCameraSource)](cameraview/init(source:).md)
  Creates a new camera view using the given source.
- [class HMCameraSource](hmcamerasource.md)
  An abstract class for a camera’s data source.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [var cameraProfiles: [HMCameraProfile]?](hmaccessory/cameraprofiles.md)
  An array of camera profiles implemented by the accessory.
- [class HMCameraProfile](hmcameraprofile.md)
  A camera profile that interacts with an accessory’s camera.
- [class HMCameraView](hmcameraview.md)
  The view into which a video stream or an image snapshot is rendered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/cameraview)*