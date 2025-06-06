# cameraDevice

**Framework**: UIKit  
**Kind**: property

The camera used by the image picker controller.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var cameraDevice: UIImagePickerController.CameraDevice { get set }
```

#### Discussion

The default is [`UIImagePickerController.CameraDevice.rear`](uiimagepickercontroller/cameradevice-swift.enum/rear.md).

## See Also

- [class func isFlashAvailable(for: UIImagePickerController.CameraDevice) -> Bool](uiimagepickercontroller/isflashavailable(for:).md)
  Queries whether the specified camera has flash illumination capability.
- [class func availableCaptureModes(for: UIImagePickerController.CameraDevice) -> [NSNumber]?](uiimagepickercontroller/availablecapturemodes(for:).md)
  Retrieves the capture modes supported by the specified camera device.
- [class func isCameraDeviceAvailable(UIImagePickerController.CameraDevice) -> Bool](uiimagepickercontroller/iscameradeviceavailable(_:).md)
  Queries whether the specified camera is available.
- [UIImagePickerController.CameraDevice](uiimagepickercontroller/cameradevice-swift.enum.md)
  Constants that specify the camera to use for image or movie capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameradevice-swift.property)*