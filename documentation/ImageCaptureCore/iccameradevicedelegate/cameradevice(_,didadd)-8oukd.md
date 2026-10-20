# cameraDevice(_:didAdd:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the client when objects are added to the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func cameraDevice(_ camera: ICCameraDevice, didAdd items: [ICCameraItem])
```

```objc
- (void) cameraDevice:(ICCameraDevice *) camera didAddItems:(NSArray<ICCameraItem *> *) items;
```

## See Also

### Adding Objects
- [func cameraDevice(ICCameraDevice, didAdd: ICCameraItem)](./cameradevice%28_,didadd%29-9pnzo.md)
  Tells the client when an object is added to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didadd:)-8oukd)*