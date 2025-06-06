# cameraFlashMode

**Framework**: UIKit  
**Kind**: property

The flash mode used by the active camera.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var cameraFlashMode: UIImagePickerController.CameraFlashMode { get set }
```

#### Discussion

The various flash modes are listed in the [`UIImagePickerController.CameraFlashMode`](uiimagepickercontroller/cameraflashmode-swift.enum.md) enumeration. The default value is [`UIImagePickerController.CameraFlashMode.auto`](uiimagepickercontroller/cameraflashmode-swift.enum/auto.md).

The value of this property specifies the behavior of the still-image flash when the value of the [`cameraCaptureMode`](uiimagepickercontroller/cameracapturemode-swift.property.md) property is [`UIImagePickerController.CameraCaptureMode.photo`](uiimagepickercontroller/cameracapturemode-swift.enum/photo.md), and specifies the behavior of the video torch when [`cameraCaptureMode`](uiimagepickercontroller/cameracapturemode-swift.property.md) is [`UIImagePickerController.CameraCaptureMode.video`](uiimagepickercontroller/cameracapturemode-swift.enum/video.md).

## See Also

- [var cameraDevice: UIImagePickerController.CameraDevice](uiimagepickercontroller/cameradevice-swift.property.md)
  The camera used by the image picker controller.
- [var cameraCaptureMode: UIImagePickerController.CameraCaptureMode](uiimagepickercontroller/cameracapturemode-swift.property.md)
  The capture mode used by the camera.
- [class func isFlashAvailable(for: UIImagePickerController.CameraDevice) -> Bool](uiimagepickercontroller/isflashavailable(for:).md)
  Queries whether the specified camera has flash illumination capability.
- [UIImagePickerController.CameraFlashMode](uiimagepickercontroller/cameraflashmode-swift.enum.md)
  Constants that specify the flash mode to use with the active camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameraflashmode-swift.property)*