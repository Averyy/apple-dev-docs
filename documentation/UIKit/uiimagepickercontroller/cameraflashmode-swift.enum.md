# UIImagePickerController.CameraFlashMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the flash mode to use with the active camera.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst

## Declaration

```swift
enum CameraFlashMode
```

```c
enum UIImagePickerControllerCameraFlashMode : NSInteger;
```

#### Overview

The constants in this enumeration are for use as values of the [`cameraFlashMode`](./cameraflashmode-swift.property.md) property.

The behavior of the flash depends on the camera capture mode.

- For a [`cameraCaptureMode`](./cameracapturemode-swift.property.md) value of [`UIImagePickerController.CameraCaptureMode.photo`](./cameracapturemode-swift.enum/photo.md), flash is used to transiently illuminate the subject during still image capture.
- For a [`cameraCaptureMode`](./cameracapturemode-swift.property.md) value of [`UIImagePickerController.CameraCaptureMode.video`](./cameracapturemode-swift.enum/video.md), flash is used to continuously illuminate the subject during movie capture.

For a given camera on a device, flash may or may not be available. You specify the active camera by way of the [`cameraDevice`](./cameradevice-swift.property.md) property. You can determine if the active camera has flash available by calling the [`isFlashAvailable(for:)`](./isflashavailable%28for%29.md) class method.

You can manipulate the flash directly to provide effects such as a strobe light. Present a picker interface set to use video capture mode. Then, turn the flash LED on or off by setting the [`cameraFlashMode`](./cameraflashmode-swift.property.md) property to [`UIImagePickerController.CameraFlashMode.on`](./cameraflashmode-swift.enum/on.md) or [`UIImagePickerController.CameraFlashMode.off`](./cameraflashmode-swift.enum/off.md).

## Topics

### Constants
- [UIImagePickerController.CameraFlashMode.off](./cameraflashmode-swift.enum/off.md)
  Specifies that flash illumination is always off, no matter what the ambient light conditions are.
- [UIImagePickerController.CameraFlashMode.auto](./cameraflashmode-swift.enum/auto.md)
  Specifies that the device should consider ambient light conditions to automatically determine whether or not to use flash illumination.
- [UIImagePickerController.CameraFlashMode.on](./cameraflashmode-swift.enum/on.md)
  Specifies that flash illumination is always on, no matter what the ambient light conditions are.
### Initializers
- [init?(rawValue: Int)](./cameraflashmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the flash behavior
- [class func isFlashAvailable(for: UIImagePickerController.CameraDevice) -> Bool](./isflashavailable%28for%29.md)
  Queries whether the specified camera has flash illumination capability.
- [var cameraFlashMode: UIImagePickerController.CameraFlashMode](./cameraflashmode-swift.property.md)
  The flash mode used by the active camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameraflashmode-swift.enum)*