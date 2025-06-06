# cameraDeviceCanTakePicture

**Framework**: ImageCaptureCore  
**Kind**: property

The capability for the client to request to take a picture while the camera is connected.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
static let cameraDeviceCanTakePicture: ICDeviceCapability
```

#### Discussion

When this capability is available, the client can call [`requestTakePicture()`](iccameradevice/requesttakepicture().md) to capture a picture.

## See Also

- [static let cameraDeviceCanTakePictureUsingShutterReleaseOnCamera: ICDeviceCapability](icdevicecapability/cameradevicecantakepictureusingshutterreleaseoncamera.md)
  The capability to capture a picture if the user presses the shutter release on the camera while the camera is connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicecapability/cameradevicecantakepicture)*