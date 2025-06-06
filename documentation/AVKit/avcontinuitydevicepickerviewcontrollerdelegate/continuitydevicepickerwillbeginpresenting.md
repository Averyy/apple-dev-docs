# continuityDevicePickerWillBeginPresenting(_:)

**Framework**: AVKit  
**Kind**: method

Informs the delegate that a continuity device picker is about to present its UI so that a person can select and connect a continuity device.

**Availability**:
- tvOS 17.0+

## Declaration

```swift
optional func continuityDevicePickerWillBeginPresenting(_ pickerViewController: AVContinuityDevicePickerViewController)
```

## Parameters

- `pickerViewController`: The continuity device picker that’s informing the delegate.

## See Also

- [func continuityDevicePickerDidCancel(AVContinuityDevicePickerViewController)](avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidcancel(_:).md)
  Informs the delegate when a person declines to select a continuity device by dismissing an app’s continuity device picker.
- [func continuityDevicePicker(AVContinuityDevicePickerViewController, didConnect: AVContinuityDevice)](avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepicker(_:didconnect:).md)
  Informs the delegate when a person selects and connects a continuity device to the system with a continuity device picker.
- [func continuityDevicePickerDidEndPresenting(AVContinuityDevicePickerViewController)](avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidendpresenting(_:).md)
  Informs the delegate that a continuity device picker is no longer presenting its UI to a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerwillbeginpresenting(_:))*