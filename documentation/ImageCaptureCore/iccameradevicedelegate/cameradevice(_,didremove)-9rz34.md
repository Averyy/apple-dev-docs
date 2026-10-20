# cameraDevice(_:didRemove:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the client when an object is removed from the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.15
- visionOS 1.0+

## Declaration

```swift
optional func cameraDevice(_ camera: ICCameraDevice, didRemove item: ICCameraItem)
```

```objc
- (void) cameraDevice:(ICCameraDevice *) camera didRemoveItem:(ICCameraItem *) item;
```

## See Also

### Removing Objects
- [func cameraDevice(ICCameraDevice, didRemove: [ICCameraItem])](./cameradevice%28_,didremove%29-4m5al.md)
  Tells the client when objects are removed from the device.
- [func cameraDevice(ICCameraDevice, didCompleteDeleteFilesWithError: (any Error)?)](./cameradevice%28_,didcompletedeletefileswitherror%29.md)
  Tells the client when the camera completes a delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didremove:)-9rz34)*