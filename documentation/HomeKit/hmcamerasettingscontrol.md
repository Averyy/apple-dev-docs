# HMCameraSettingsControl

**Framework**: HomeKit  
**Kind**: class

An object that represents the ability to control a camera’s settings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HMCameraSettingsControl
```

## Topics

### Controlling camera characteristics
- [var currentHorizontalTilt: HMCharacteristic?](hmcamerasettingscontrol/currenthorizontaltilt.md)
  Characteristic corresponding to the camera’s current horizontal tilt setting.
- [var targetHorizontalTilt: HMCharacteristic?](hmcamerasettingscontrol/targethorizontaltilt.md)
  Characteristic corresponding to adjusting the camera’s horizontal tilt setting.
- [var currentVerticalTilt: HMCharacteristic?](hmcamerasettingscontrol/currentverticaltilt.md)
  Characteristic corresponding to the camera’s current vertical tilt setting.
- [var targetVerticalTilt: HMCharacteristic?](hmcamerasettingscontrol/targetverticaltilt.md)
  Characteristic corresponding to adjusting the camera’s vertical tilt setting.
- [var opticalZoom: HMCharacteristic?](hmcamerasettingscontrol/opticalzoom.md)
  Characteristic corresponding to the camera’s optical zoom setting.
- [var digitalZoom: HMCharacteristic?](hmcamerasettingscontrol/digitalzoom.md)
  Characteristic corresponding to the camera’s digital zoom setting.
- [var imageMirroring: HMCharacteristic?](hmcamerasettingscontrol/imagemirroring.md)
  Characteristic corresponding to the camera’s image mirroring setting.
- [var imageRotation: HMCharacteristic?](hmcamerasettingscontrol/imagerotation.md)
  Characteristic corresponding to the camera’s image rotation setting.
- [var nightVision: HMCharacteristic?](hmcamerasettingscontrol/nightvision.md)
  Characteristic corresponding to the camera’s night vision setting.

## Relationships

### Inherits From
- [HMCameraControl](hmcameracontrol.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var settingsControl: HMCameraSettingsControl?](hmcameraprofile/settingscontrol.md)
  Controls the settings on the camera.
- [class HMCameraControl](hmcameracontrol.md)
  An abstract class that represents a camera control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasettingscontrol)*