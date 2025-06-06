# cameraDevice(_:didRemove:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the client when an object is removed from the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
optional func cameraDevice(_ camera: ICCameraDevice, didRemove item: ICCameraItem)
```

## See Also

- [func cameraDevice(ICCameraDevice, didRemove: [ICCameraItem])](iccameradevicedelegate/cameradevice(_:didremove:)-4m5al.md)
  Tells the client when objects are removed from the device.
- [func cameraDevice(ICCameraDevice, didCompleteDeleteFilesWithError: (any Error)?)](iccameradevicedelegate/cameradevice(_:didcompletedeletefileswitherror:).md)
  Tells the client when the camera completes a delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didremove:)-9rz34)*