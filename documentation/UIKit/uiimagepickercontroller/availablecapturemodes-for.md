# availableCaptureModes(for:)

**Framework**: UIKit  
**Kind**: method

Retrieves the capture modes supported by the specified camera device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class func availableCaptureModes(for cameraDevice: UIImagePickerController.CameraDevice) -> [NSNumber]?
```

#### Return Value

An array of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects indicating the capture modes supported by `cameraDevice`.

#### Discussion

See [`UIImagePickerController.CameraCaptureMode`](uiimagepickercontroller/cameracapturemode-swift.enum.md) for possible values.

## Parameters

- `cameraDevice`: A   constant indicating the camera you want to interrogate.

## See Also

- [var cameraCaptureMode: UIImagePickerController.CameraCaptureMode](uiimagepickercontroller/cameracapturemode-swift.property.md)
  The capture mode used by the camera.
- [UIImagePickerController.CameraCaptureMode](uiimagepickercontroller/cameracapturemode-swift.enum.md)
  Constants that specify the category of media for the camera to capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/availablecapturemodes(for:))*