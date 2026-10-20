# cameraDevice(_:didReceiveMetadataFor:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the client when the metadata requested for an item on a camera is available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.15
- visionOS 1.0+

## Declaration

```swift
optional func cameraDevice(_ camera: ICCameraDevice, didReceiveMetadataFor item: ICCameraItem)
```

```objc
- (void) cameraDevice:(ICCameraDevice *) camera didReceiveMetadataForItem:(ICCameraItem *) item;
```

## See Also

### Receiving Metadata
- [func cameraDevice(ICCameraDevice, didReceiveMetadata: [AnyHashable : Any]?, for: ICCameraItem, error: (any Error)?)](./cameradevice%28_,didreceivemetadata,for,error%29.md)
  Tells the client when the metadata requested for an item on a camera is available.
- [func cameraDevice(ICCameraDevice, shouldGetMetadataOf: ICCameraItem) -> Bool](./cameradevice%28_,shouldgetmetadataof%29.md)
  Tells the client when the camera is about to execute queued requests for the metadata of a specific item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didreceivemetadatafor:))*