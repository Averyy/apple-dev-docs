# cameraDevice(_:didCompleteDeleteFilesWithError:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) cameraDevice:(ICCameraDevice *) camera didCompleteDeleteFilesWithError:(NSError *) error;
```

## Discussion

Initiate a delete operation using [`requestDeleteFiles(_:)`](../iccameradevice/requestdeletefiles%28_%29.md).

## See Also

### Removing Objects
- [func cameraDevice(ICCameraDevice, didRemove: [ICCameraItem])](./cameradevice%28_,didremove%29-4m5al.md)
  Tells the client when objects are removed from the device.
- [func cameraDevice(ICCameraDevice, didRemove: ICCameraItem)](./cameradevice%28_,didremove%29-9rz34.md)
  Tells the client when an object is removed from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didcompletedeletefileswitherror:))*