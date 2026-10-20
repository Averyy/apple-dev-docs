# isCameraDeviceAvailable(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Queries whether the specified camera is available.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class func isCameraDeviceAvailable(_ cameraDevice: UIImagePickerController.CameraDevice) -> Bool
```

```objc
+ (BOOL) isCameraDeviceAvailable:(UIImagePickerControllerCameraDevice) cameraDevice;
```

#### Return Value

[`true`](../../Swift/true.md) if the camera indicated by `cameraDevice` is available, or [`false`](../../Swift/false.md) if it is not available.

## Parameters

- `cameraDevice`: A [`UIImagePickerController.CameraDevice`](./cameradevice-swift.enum.md) constant indicating the camera whose availability you want to check.

## See Also

### Related Documentation
- [class func isFlashAvailable(for: UIImagePickerController.CameraDevice) -> Bool](./isflashavailable%28for%29.md)
  Queries whether the specified camera has flash illumination capability.
- [class func availableCaptureModes(for: UIImagePickerController.CameraDevice) -> [NSNumber]?](./availablecapturemodes%28for%29.md)
  Retrieves the capture modes supported by the specified camera device.
### Configuring the camera to use
- [var cameraDevice: UIImagePickerController.CameraDevice](./cameradevice-swift.property.md)
  The camera used by the image picker controller.
- [UIImagePickerController.CameraDevice](./cameradevice-swift.enum.md)
  Constants that specify the camera to use for image or movie capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/iscameradeviceavailable(_:))*