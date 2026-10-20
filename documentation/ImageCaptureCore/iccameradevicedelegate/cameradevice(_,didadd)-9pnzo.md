# cameraDevice(_:didAdd:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the client when an object is added to the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.15
- visionOS 1.0+

## Declaration

```swift
optional func cameraDevice(_ camera: ICCameraDevice, didAdd item: ICCameraItem)
```

```objc
- (void) cameraDevice:(ICCameraDevice *) camera didAddItem:(ICCameraItem *) item;
```

## See Also

### Adding Objects
- [func cameraDevice(ICCameraDevice, didAdd: [ICCameraItem])](./cameradevice%28_,didadd%29-8oukd.md)
  Tells the client when objects are added to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didadd:)-9pnzo)*