# UIImagePickerController.CameraDevice

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the camera to use for image or movie capture.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst

## Declaration

```swift
enum CameraDevice
```

```c
enum UIImagePickerControllerCameraDevice : NSInteger;
```

## Overview

The constants in this enumeration are for use as values of the [`cameraDevice`](./cameradevice-swift.property.md) property.

## Topics

### Constants
- [UIImagePickerController.CameraDevice.rear](./cameradevice-swift.enum/rear.md)
  Specifies the camera on the rear of the device.
- [UIImagePickerController.CameraDevice.front](./cameradevice-swift.enum/front.md)
  Specifies the camera on the front of the device.
### Initializers
- [init?(rawValue: Int)](./cameradevice-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the camera to use
- [class func isCameraDeviceAvailable(UIImagePickerController.CameraDevice) -> Bool](./iscameradeviceavailable%28_%29.md)
  Queries whether the specified camera is available.
- [var cameraDevice: UIImagePickerController.CameraDevice](./cameradevice-swift.property.md)
  The camera used by the image picker controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameradevice-swift.enum)*