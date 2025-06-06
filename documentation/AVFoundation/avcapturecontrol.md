# AVCaptureControl

**Framework**: AVFoundation  
**Kind**: class

An abstract base class for controls that interact with the camera system.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
class AVCaptureControl
```

## Mentions

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

#### Overview

Capture controls provide the interface for interacting with the camera system from the Camera Control button on iPhone 16 devices. The framework provides several concrete subclasses of this class that allow apps to access built-in functionality and define custom controls.

## Topics

### Setting the enabled state
- [var isEnabled: Bool](avcapturecontrol/isenabled.md)
  A Boolean value that indicates whether this control supports user interaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVCaptureIndexPicker](avcaptureindexpicker.md)
- [AVCaptureSlider](avcaptureslider.md)
- [AVCaptureSystemExposureBiasSlider](avcapturesystemexposurebiasslider.md)
- [AVCaptureSystemZoomSlider](avcapturesystemzoomslider.md)
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
- [class AVCaptureSystemZoomSlider](avcapturesystemzoomslider.md)
  A control that adjusts the video zoom factor of a capture device within the system-recommended range.
- [class AVCaptureSystemExposureBiasSlider](avcapturesystemexposurebiasslider.md)
  A control that adjusts the exposure bias of a capture device within the system-recommended range.
- [class AVCaptureSlider](avcaptureslider.md)
  A slider control that selects a value from a bounded range.
- [class AVCaptureIndexPicker](avcaptureindexpicker.md)
  A control for selecting from a set of mutually exclusive values by index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturecontrol)*