# cameraDevice(_:didCompleteDeleteFilesWithError:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the client when the camera completes a delete operation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
optional func cameraDevice(_ camera: ICCameraDevice, didCompleteDeleteFilesWithError error: (any Error)?)
```

#### Discussion

Initiate a delete operation using [`requestDeleteFiles(_:)`](iccameradevice/requestdeletefiles(_:).md).

## See Also

- [func cameraDevice(ICCameraDevice, didRemove: [ICCameraItem])](iccameradevicedelegate/cameradevice(_:didremove:)-4m5al.md)
  Tells the client when objects are removed from the device.
- [func cameraDevice(ICCameraDevice, didRemove: ICCameraItem)](iccameradevicedelegate/cameradevice(_:didremove:)-9rz34.md)
  Tells the client when an object is removed from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didcompletedeletefileswitherror:))*