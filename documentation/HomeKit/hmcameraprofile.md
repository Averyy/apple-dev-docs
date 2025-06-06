# HMCameraProfile

**Framework**: HomeKit  
**Kind**: class

A camera profile that interacts with an accessory’s camera.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HMCameraProfile
```

#### Overview

Each profile control is optional, because an individual camera vendor may not support all of the features defined by the HomeKit camera specifications.

## Topics

### Controlling camera settings
- [var settingsControl: HMCameraSettingsControl?](hmcameraprofile/settingscontrol.md)
  Controls the settings on the camera.
- [class HMCameraSettingsControl](hmcamerasettingscontrol.md)
  An object that represents the ability to control a camera’s settings.
- [class HMCameraControl](hmcameracontrol.md)
  An abstract class that represents a camera control.
### Playing audio
- [var microphoneControl: HMCameraAudioControl?](hmcameraprofile/microphonecontrol.md)
  Controls the microphone settings on the camera.
- [var speakerControl: HMCameraAudioControl?](hmcameraprofile/speakercontrol.md)
  Controls the speaker settings on the camera.
- [class HMCameraAudioControl](hmcameraaudiocontrol.md)
  An object that controls a camera’s audio settings.
### Streaming
- [var streamControl: HMCameraStreamControl?](hmcameraprofile/streamcontrol.md)
  Controls the camera stream.
- [class HMCameraStreamControl](hmcamerastreamcontrol.md)
  An object that can start and stop the camera stream and contains the view into which the stream is rendered.
### Capturing snapshots
- [var snapshotControl: HMCameraSnapshotControl?](hmcameraprofile/snapshotcontrol.md)
  Controls the camera’s snapshot function.
- [class HMCameraSnapshotControl](hmcamerasnapshotcontrol.md)
  An object that can take an image snapshot from a camera.

## Relationships

### Inherits From
- [HMAccessoryProfile](hmaccessoryprofile.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var profiles: [HMAccessoryProfile]](hmaccessory/profiles.md)
  An array of profiles implemented by the accessory.
- [class HMAccessoryProfile](hmaccessoryprofile.md)
  A profile that certain accessories implement.
- [class HMNetworkConfigurationProfile](hmnetworkconfigurationprofile.md)
  A profile that provides information about network protection for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcameraprofile)*