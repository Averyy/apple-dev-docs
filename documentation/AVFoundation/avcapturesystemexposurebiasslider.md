# AVCaptureSystemExposureBiasSlider

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptureSystemExposureBiasSlider : AVCaptureControl
```

## Mentions

- [Enhancing your app experience with the Camera Control](./enhancing-your-app-experience-with-the-camera-control.md)

## Overview

This control defines its range by querying the [`systemRecommendedExposureBiasRange`](./avcapturedevice/format/systemrecommendedexposurebiasrange.md) property of the device’s active format. If a device’s [`activeFormat`](./avcapturedevice/activeformat.md) value changes, the slider updates its range with the new format’s system-recommended value.

To use this control, add it to the capture session by calling the session’s [`addControl(_:)`](./avcapturesession/addcontrol%28_%29.md) method.

## Topics

### Creating an exposure bias slider
- [init(device: AVCaptureDevice)](./avcapturesystemexposurebiasslider/init%28device%29.md)
  Creates a slider to control the exposure bias of the specified capture device.
- [init(device: AVCaptureDevice, action: (Float) -> Void)](./avcapturesystemexposurebiasslider/init%28device,action%29.md)
  Creates a slider to control the exposure bias of the specified capture device with an action to respond to exposure bias changes.

## Relationships

### Inherits From
- [AVCaptureControl](./avcapturecontrol.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Capture controls
- [Enhancing your app experience with the Camera Control](./enhancing-your-app-experience-with-the-camera-control.md)
  Provide direct access to your camera app’s features to help people quickly capture the perfect shot.
- [class AVCaptureControl](./avcapturecontrol.md)
  An abstract base class for controls that interact with the camera system.
- [class AVCaptureSystemZoomSlider](./avcapturesystemzoomslider.md)
  A control that adjusts the video zoom factor of a capture device within the system-recommended range.
- [class AVCaptureSlider](./avcaptureslider.md)
  A slider control that selects a value from a bounded range.
- [class AVCaptureIndexPicker](./avcaptureindexpicker.md)
  A control for selecting from a set of mutually exclusive values by index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesystemexposurebiasslider)*