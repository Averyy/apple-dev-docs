# cameraDevice

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The camera used by the image picker controller.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var cameraDevice: UIImagePickerController.CameraDevice { get set }
```

```objc
@property (nonatomic) UIImagePickerControllerCameraDevice cameraDevice;
```

#### Discussion

The default is [`UIImagePickerController.CameraDevice.rear`](./cameradevice-swift.enum/rear.md).

## See Also

### Related Documentation
- [class func isFlashAvailable(for: UIImagePickerController.CameraDevice) -> Bool](./isflashavailable%28for%29.md)
  Queries whether the specified camera has flash illumination capability.
- [class func availableCaptureModes(for: UIImagePickerController.CameraDevice) -> [NSNumber]?](./availablecapturemodes%28for%29.md)
  Retrieves the capture modes supported by the specified camera device.
### Configuring the camera to use
- [class func isCameraDeviceAvailable(UIImagePickerController.CameraDevice) -> Bool](./iscameradeviceavailable%28_%29.md)
  Queries whether the specified camera is available.
- [UIImagePickerController.CameraDevice](./cameradevice-swift.enum.md)
  Constants that specify the camera to use for image or movie capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameradevice-swift.property)*