# cameraCaptureMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The capture mode used by the camera.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var cameraCaptureMode: UIImagePickerController.CameraCaptureMode { get set }
```

```objc
@property (nonatomic) UIImagePickerControllerCameraCaptureMode cameraCaptureMode;
```

#### Discussion

The various capture modes are listed in the [`UIImagePickerController.CameraCaptureMode`](./cameracapturemode-swift.enum.md) enumeration. The default value is [`UIImagePickerController.CameraCaptureMode.photo`](./cameracapturemode-swift.enum/photo.md).

## See Also

### Related Documentation
- [var cameraDevice: UIImagePickerController.CameraDevice](./cameradevice-swift.property.md)
  The camera used by the image picker controller.
### Configuring the camera capture mode
- [class func availableCaptureModes(for: UIImagePickerController.CameraDevice) -> [NSNumber]?](./availablecapturemodes%28for%29.md)
  Retrieves the capture modes supported by the specified camera device.
- [UIImagePickerController.CameraCaptureMode](./cameracapturemode-swift.enum.md)
  Constants that specify the category of media for the camera to capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameracapturemode-swift.property)*