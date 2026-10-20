# availableCaptureModes(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Retrieves the capture modes supported by the specified camera device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class func availableCaptureModes(for cameraDevice: UIImagePickerController.CameraDevice) -> [NSNumber]?
```

```objc
+ (NSArray<NSNumber *> *) availableCaptureModesForCameraDevice:(UIImagePickerControllerCameraDevice) cameraDevice;
```

#### Return Value

An array of [`NSNumber`](../../Foundation/nsnumber.md) objects indicating the capture modes supported by `cameraDevice`.

#### Discussion

See [`UIImagePickerController.CameraCaptureMode`](./cameracapturemode-swift.enum.md) for possible values.

## Parameters

- `cameraDevice`: A [`UIImagePickerController.CameraDevice`](./cameradevice-swift.enum.md) constant indicating the camera you want to interrogate.

## See Also

### Configuring the camera capture mode
- [var cameraCaptureMode: UIImagePickerController.CameraCaptureMode](./cameracapturemode-swift.property.md)
  The capture mode used by the camera.
- [UIImagePickerController.CameraCaptureMode](./cameracapturemode-swift.enum.md)
  Constants that specify the category of media for the camera to capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/availablecapturemodes(for:))*