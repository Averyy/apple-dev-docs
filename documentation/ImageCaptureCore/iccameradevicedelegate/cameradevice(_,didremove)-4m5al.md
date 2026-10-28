# cameraDevice(_:didRemove:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) cameraDevice:(ICCameraDevice *) camera didRemoveItems:(NSArray<ICCameraItem *> *) items;
```

## Discussion

The objects in items are instances of the ICCameraFile class.

## See Also

### Removing Objects
- [func cameraDevice(ICCameraDevice, didCompleteDeleteFilesWithError: (any Error)?)](./cameradevice%28_,didcompletedeletefileswitherror%29.md)
  Tells the client when the camera completes a delete operation.
- [func cameraDevice(ICCameraDevice, didRemove: ICCameraItem)](./cameradevice%28_,didremove%29-9rz34.md)
  Tells the client when an object is removed from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didremove:)-4m5al)*