# cameraCaptureMode

**Framework**: UIKit  
**Kind**: property

The capture mode used by the camera.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var cameraCaptureMode: UIImagePickerController.CameraCaptureMode { get set }
```

#### Discussion

The various capture modes are listed in the [`UIImagePickerController.CameraCaptureMode`](uiimagepickercontroller/cameracapturemode-swift.enum.md) enumeration. The default value is [`UIImagePickerController.CameraCaptureMode.photo`](uiimagepickercontroller/cameracapturemode-swift.enum/photo.md).

## See Also

- [var cameraDevice: UIImagePickerController.CameraDevice](uiimagepickercontroller/cameradevice-swift.property.md)
  The camera used by the image picker controller.
- [class func availableCaptureModes(for: UIImagePickerController.CameraDevice) -> [NSNumber]?](uiimagepickercontroller/availablecapturemodes(for:).md)
  Retrieves the capture modes supported by the specified camera device.
- [UIImagePickerController.CameraCaptureMode](uiimagepickercontroller/cameracapturemode-swift.enum.md)
  Constants that specify the category of media for the camera to capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameracapturemode-swift.property)*