# AVCaptureSystemExposureBiasSlider

**Framework**: AVFoundation  
**Kind**: class

A control that adjusts the exposure bias of a capture device within the system-recommended range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
class AVCaptureSystemExposureBiasSlider
```

## Mentions

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

#### Overview

This control defines its range by querying the [`systemRecommendedExposureBiasRange`](avcapturedevice/format/systemrecommendedexposurebiasrange.md) property of the device’s active format. If a device’s [`activeFormat`](avcapturedevice/activeformat.md) value changes, the slider updates its range with the new format’s system-recommended value.

To use this control, add it to the capture session by calling the session’s [`addControl(_:)`](avcapturesession/addcontrol(_:).md) method.

## Topics

### Creating an exposure bias slider
- [init(device: AVCaptureDevice)](avcapturesystemexposurebiasslider/init(device:).md)
  Creates a slider to control the exposure bias of the specified capture device.
- [init(device: AVCaptureDevice, action: (Float) -> Void)](avcapturesystemexposurebiasslider/init(device:action:).md)
  Creates a slider to control the exposure bias of the specified capture device with an action to respond to exposure bias changes.

## Relationships

### Inherits From
- [AVCaptureControl](avcapturecontrol.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)
  Provide direct access to your camera app’s features to help people quickly capture the perfect shot.
- [class AVCaptureControl](avcapturecontrol.md)
  An abstract base class for controls that interact with the camera system.
- [class AVCaptureSystemZoomSlider](avcapturesystemzoomslider.md)
  A control that adjusts the video zoom factor of a capture device within the system-recommended range.
- [class AVCaptureSlider](avcaptureslider.md)
  A slider control that selects a value from a bounded range.
- [class AVCaptureIndexPicker](avcaptureindexpicker.md)
  A control for selecting from a set of mutually exclusive values by index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesystemexposurebiasslider)*