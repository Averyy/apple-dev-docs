# cameraFlashMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The flash mode used by the active camera.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var cameraFlashMode: UIImagePickerController.CameraFlashMode { get set }
```

```objc
@property (nonatomic) UIImagePickerControllerCameraFlashMode cameraFlashMode;
```

## Discussion

The various flash modes are listed in the [`UIImagePickerController.CameraFlashMode`](./cameraflashmode-swift.enum.md) enumeration. The default value is [`UIImagePickerController.CameraFlashMode.auto`](./cameraflashmode-swift.enum/auto.md).

The value of this property specifies the behavior of the still-image flash when the value of the [`cameraCaptureMode`](./cameracapturemode-swift.property.md) property is [`UIImagePickerController.CameraCaptureMode.photo`](./cameracapturemode-swift.enum/photo.md), and specifies the behavior of the video torch when [`cameraCaptureMode`](./cameracapturemode-swift.property.md) is [`UIImagePickerController.CameraCaptureMode.video`](./cameracapturemode-swift.enum/video.md).

## See Also

### Related Documentation
- [var cameraDevice: UIImagePickerController.CameraDevice](./cameradevice-swift.property.md)
  The camera used by the image picker controller.
- [var cameraCaptureMode: UIImagePickerController.CameraCaptureMode](./cameracapturemode-swift.property.md)
  The capture mode used by the camera.
### Configuring the flash behavior
- [class func isFlashAvailable(for: UIImagePickerController.CameraDevice) -> Bool](./isflashavailable%28for%29.md)
  Queries whether the specified camera has flash illumination capability.
- [UIImagePickerController.CameraFlashMode](./cameraflashmode-swift.enum.md)
  Constants that specify the flash mode to use with the active camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameraflashmode-swift.property)*