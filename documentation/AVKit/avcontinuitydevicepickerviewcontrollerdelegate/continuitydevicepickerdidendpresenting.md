# continuityDevicePickerDidEndPresenting(_:)

**Framework**: AVKit  
**Kind**: method

Informs the delegate that a continuity device picker is no longer presenting its UI to a person.

**Availability**:
- tvOS 17.0+

## Declaration

```swift
optional func continuityDevicePickerDidEndPresenting(_ pickerViewController: AVContinuityDevicePickerViewController)
```

## Parameters

- `pickerViewController`: The continuity device picker that’s informing the delegate.

## See Also

- [func continuityDevicePickerWillBeginPresenting(AVContinuityDevicePickerViewController)](avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerwillbeginpresenting(_:).md)
  Informs the delegate that a continuity device picker is about to present its UI so that a person can select and connect a continuity device.
- [func continuityDevicePickerDidCancel(AVContinuityDevicePickerViewController)](avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidcancel(_:).md)
  Informs the delegate when a person declines to select a continuity device by dismissing an app’s continuity device picker.
- [func continuityDevicePicker(AVContinuityDevicePickerViewController, didConnect: AVContinuityDevice)](avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepicker(_:didconnect:).md)
  Informs the delegate when a person selects and connects a continuity device to the system with a continuity device picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidendpresenting(_:))*