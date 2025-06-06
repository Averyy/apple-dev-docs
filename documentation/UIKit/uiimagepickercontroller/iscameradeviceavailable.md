# isCameraDeviceAvailable(_:)

**Framework**: UIKit  
**Kind**: method

Queries whether the specified camera is available.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class func isCameraDeviceAvailable(_ cameraDevice: UIImagePickerController.CameraDevice) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the camera indicated by `cameraDevice` is available, or [`false`](https://developer.apple.com/documentation/swift/false) if it is not available.

## Parameters

- `cameraDevice`: A   constant indicating the camera whose availability you want to check.

## See Also

- [class func isFlashAvailable(for: UIImagePickerController.CameraDevice) -> Bool](uiimagepickercontroller/isflashavailable(for:).md)
  Queries whether the specified camera has flash illumination capability.
- [class func availableCaptureModes(for: UIImagePickerController.CameraDevice) -> [NSNumber]?](uiimagepickercontroller/availablecapturemodes(for:).md)
  Retrieves the capture modes supported by the specified camera device.
- [var cameraDevice: UIImagePickerController.CameraDevice](uiimagepickercontroller/cameradevice-swift.property.md)
  The camera used by the image picker controller.
- [UIImagePickerController.CameraDevice](uiimagepickercontroller/cameradevice-swift.enum.md)
  Constants that specify the camera to use for image or movie capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/iscameradeviceavailable(_:))*