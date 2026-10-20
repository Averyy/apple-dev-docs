# cameraDevice(_:didRenameItems:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the client when one or more objects are renamed on the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func cameraDevice(_ camera: ICCameraDevice, didRenameItems items: [ICCameraItem])
```

```objc
- (void) cameraDevice:(ICCameraDevice *) camera didRenameItems:(NSArray<ICCameraItem *> *) items;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didrenameitems:))*