# cameraDevice(_:didReceiveMetadataFor:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the client when the metadata requested for an item on a camera is available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
optional func cameraDevice(_ camera: ICCameraDevice, didReceiveMetadataFor item: ICCameraItem)
```

## See Also

- [func cameraDevice(ICCameraDevice, didReceiveMetadata: [AnyHashable : Any]?, for: ICCameraItem, error: (any Error)?)](iccameradevicedelegate/cameradevice(_:didreceivemetadata:for:error:).md)
  Tells the client when the metadata requested for an item on a camera is available.
- [func cameraDevice(ICCameraDevice, shouldGetMetadataOf: ICCameraItem) -> Bool](iccameradevicedelegate/cameradevice(_:shouldgetmetadataof:).md)
  Tells the client when the camera is about to execute queued requests for the metadata of a specific item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didreceivemetadatafor:))*