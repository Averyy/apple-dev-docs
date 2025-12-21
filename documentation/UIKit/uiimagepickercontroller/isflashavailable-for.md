# isFlashAvailable(for:)

**Framework**: UIKit  
**Kind**: method

Queries whether the specified camera has flash illumination capability.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class func isFlashAvailable(for cameraDevice: UIImagePickerController.CameraDevice) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `cameraDevice` can use flash illumination, or [`false`](https://developer.apple.com/documentation/Swift/false) if it cannot.

## Parameters

- `cameraDevice`: A   constant indicating the camera whose flash capability you want to know.

## See Also

- [var cameraDevice: UIImagePickerController.CameraDevice](uiimagepickercontroller/cameradevice-swift.property.md)
  The camera used by the image picker controller.
- [var cameraFlashMode: UIImagePickerController.CameraFlashMode](uiimagepickercontroller/cameraflashmode-swift.property.md)
  The flash mode used by the active camera.
- [UIImagePickerController.CameraFlashMode](uiimagepickercontroller/cameraflashmode-swift.enum.md)
  Constants that specify the flash mode to use with the active camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/isflashavailable(for:))*