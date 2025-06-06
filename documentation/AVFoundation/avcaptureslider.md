# AVCaptureSlider

**Framework**: AVFoundation  
**Kind**: class

A slider control that selects a value from a bounded range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
class AVCaptureSlider
```

## Mentions

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

#### Overview

Sliders are appropriate for controls that provide a single float value.

## Topics

### Creating a slider
- [convenience init(String, symbolName: String, in: ClosedRange<Float>)](avcaptureslider/init(_:symbolname:in:).md)
  Creates a continuous slider control that selects a value from a bounded range.
- [convenience init(String, symbolName: String, in: ClosedRange<Float>, step: Float)](avcaptureslider/init(_:symbolname:in:step:).md)
  Creates a discrete slider control that selects a stepped value from a bounded range.
- [convenience init(String, symbolName: String, values: [Float])](avcaptureslider/init(_:symbolname:values:).md)
  Creates a discrete slider control that selects a value from a list.
### Handling interaction
- [func setActionQueue(DispatchQueue, action: (Float) -> ())](avcaptureslider/setactionqueue(_:action:).md)
  Sets the action to perform on the specified dispatch queue when the control’s value changes.
### Accessing the control value
- [var value: Float](avcaptureslider/value.md)
  The current value of the slider.
- [var prominentValues: [Float]](avcaptureslider/prominentvalues-199dz.md)
  Values in this array may receive unique visual representations or behaviors.
- [var localizedValueFormat: String?](avcaptureslider/localizedvalueformat.md)
  A localized string that defines the presentation of the slider’s value.
### Setting an accessibility identifier
- [var accessibilityIdentifier: String?](avcaptureslider/accessibilityidentifier.md)
  A string identifier for the slider.
### Inspecting presentation attributes
- [var symbolName: String](avcaptureslider/symbolname.md)
  The name of the SF Symbol that represents this control.
- [var localizedTitle: String](avcaptureslider/localizedtitle.md)
  A localized title that describes the control’s action.

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
- [class AVCaptureSystemExposureBiasSlider](avcapturesystemexposurebiasslider.md)
  A control that adjusts the exposure bias of a capture device within the system-recommended range.
- [class AVCaptureIndexPicker](avcaptureindexpicker.md)
  A control for selecting from a set of mutually exclusive values by index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureslider)*