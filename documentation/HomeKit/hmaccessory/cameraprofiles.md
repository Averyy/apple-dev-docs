# cameraProfiles

**Framework**: HomeKit  
**Kind**: property

An array of camera profiles implemented by the accessory.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var cameraProfiles: [HMCameraProfile]? { get }
```

#### Discussion

An accessory can contain one or more cameras. Each camera is represented as a an [`HMCameraProfile`](hmcameraprofile.md) instance. If the accessory doesn’t contain a camera, this property is `nil`.

## See Also

- [struct CameraView](cameraview.md)
  A SwiftUI view into which a video stream or an image snapshot is rendered.
- [class HMCameraProfile](hmcameraprofile.md)
  A camera profile that interacts with an accessory’s camera.
- [class HMCameraView](hmcameraview.md)
  The view into which a video stream or an image snapshot is rendered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/cameraprofiles)*