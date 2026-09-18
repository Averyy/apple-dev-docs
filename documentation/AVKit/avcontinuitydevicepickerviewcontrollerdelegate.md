# AVContinuityDevicePickerViewControllerDelegate

**Framework**: AVKit  
**Kind**: protocol

An interface that responds to events from a continuity device picker view controller.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
protocol AVContinuityDevicePickerViewControllerDelegate : NSObjectProtocol
```

#### Overview

Your app can respond to the various outcome events from an [`AVContinuityDevicePickerViewController`](avcontinuitydevicepickerviewcontroller.md) instance with the following steps:

1. Adopt the [`AVContinuityDevicePickerViewControllerDelegate`](avcontinuitydevicepickerviewcontrollerdelegate.md) protocol with one of the app’s classes.
2. Create an instance of that class.
3. Assign that instance to the view controller’s [`delegate`](avcontinuitydevicepickerviewcontroller/delegate.md) property.

## Topics

### Responding to continuity device events
- [func continuityDevicePickerWillBeginPresenting(AVContinuityDevicePickerViewController)](avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerwillbeginpresenting(_:).md)
  Informs the delegate that a continuity device picker is about to present its UI so that a person can select and connect a continuity device.
- [func continuityDevicePickerDidCancel(AVContinuityDevicePickerViewController)](avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidcancel(_:).md)
  Informs the delegate when a person declines to select a continuity device by dismissing an app’s continuity device picker.
- [func continuityDevicePicker(AVContinuityDevicePickerViewController, didConnect: AVContinuityDevice)](avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepicker(_:didconnect:).md)
  Informs the delegate when a person selects and connects a continuity device to the system with a continuity device picker.
- [func continuityDevicePickerDidEndPresenting(AVContinuityDevicePickerViewController)](avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidendpresenting(_:).md)
  Informs the delegate that a continuity device picker is no longer presenting its UI to a person.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Supporting Continuity Camera in your tvOS app](supporting-continuity-camera-in-your-tvos-app.md)
  Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [class AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md)
  A view controller that provides an interface to a person so they can select and connect a continuity device to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate)*