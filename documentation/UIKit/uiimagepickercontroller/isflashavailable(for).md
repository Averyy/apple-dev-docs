# isFlashAvailable(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Queries whether the specified camera has flash illumination capability.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class func isFlashAvailable(for cameraDevice: UIImagePickerController.CameraDevice) -> Bool
```

```objc
+ (BOOL) isFlashAvailableForCameraDevice:(UIImagePickerControllerCameraDevice) cameraDevice;
```

## Return Value

[`true`](../../Swift/true.md) if `cameraDevice` can use flash illumination, or [`false`](../../Swift/false.md) if it cannot.

## Parameters

- `cameraDevice`: A [`UIImagePickerController.CameraDevice`](./cameradevice-swift.enum.md) constant indicating the camera whose flash capability you want to know.

## See Also

### Related Documentation
- [var cameraDevice: UIImagePickerController.CameraDevice](./cameradevice-swift.property.md)
  The camera used by the image picker controller.
### Configuring the flash behavior
- [var cameraFlashMode: UIImagePickerController.CameraFlashMode](./cameraflashmode-swift.property.md)
  The flash mode used by the active camera.
- [UIImagePickerController.CameraFlashMode](./cameraflashmode-swift.enum.md)
  Constants that specify the flash mode to use with the active camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/isflashavailable(for:))*