# cameraDevice(_:didRemove:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Required**: Yes

Tells the client when objects are removed from the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func cameraDevice(_ camera: ICCameraDevice, didRemove items: [ICCameraItem])
```

#### Discussion

The objects in items are instances of the ICCameraFile class.

## See Also

- [func cameraDevice(ICCameraDevice, didCompleteDeleteFilesWithError: (any Error)?)](iccameradevicedelegate/cameradevice(_:didcompletedeletefileswitherror:).md)
  Tells the client when the camera completes a delete operation.
- [func cameraDevice(ICCameraDevice, didRemove: ICCameraItem)](iccameradevicedelegate/cameradevice(_:didremove:)-9rz34.md)
  Tells the client when an object is removed from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didremove:)-4m5al)*