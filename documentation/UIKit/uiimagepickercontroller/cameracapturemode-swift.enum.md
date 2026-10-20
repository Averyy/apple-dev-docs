# UIImagePickerController.CameraCaptureMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the category of media for the camera to capture.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst

## Declaration

```swift
enum CameraCaptureMode
```

```c
enum UIImagePickerControllerCameraCaptureMode : NSInteger;
```

#### Overview

The constants in this enumeration are for use as values of the [`cameraCaptureMode`](./cameracapturemode-swift.property.md) property.

## Topics

### Constants
- [UIImagePickerController.CameraCaptureMode.photo](./cameracapturemode-swift.enum/photo.md)
  Specifies that the camera captures still images.
- [UIImagePickerController.CameraCaptureMode.video](./cameracapturemode-swift.enum/video.md)
  Specifies that the camera captures movies.
### Initializers
- [init?(rawValue: Int)](./cameracapturemode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the camera capture mode
- [class func availableCaptureModes(for: UIImagePickerController.CameraDevice) -> [NSNumber]?](./availablecapturemodes%28for%29.md)
  Retrieves the capture modes supported by the specified camera device.
- [var cameraCaptureMode: UIImagePickerController.CameraCaptureMode](./cameracapturemode-swift.property.md)
  The capture mode used by the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameracapturemode-swift.enum)*