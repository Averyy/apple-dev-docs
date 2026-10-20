# cameraDevice(_:shouldGetMetadataOf:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the client when the camera is about to execute queued requests for the metadata of a specific item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetMetadataOf item: ICCameraItem) -> Bool
```

```objc
- (BOOL) cameraDevice:(ICCameraDevice *) cameraDevice shouldGetMetadataOfItem:(ICCameraItem *) item;
```

#### Discussion

If the request is no longer needed—for example, if the item is no longer displayed on the screen—the client can cancel sending a request to the camera, speeding up the execution queue.

## See Also

### Receiving Metadata
- [func cameraDevice(ICCameraDevice, didReceiveMetadata: [AnyHashable : Any]?, for: ICCameraItem, error: (any Error)?)](./cameradevice%28_,didreceivemetadata,for,error%29.md)
  Tells the client when the metadata requested for an item on a camera is available.
- [func cameraDevice(ICCameraDevice, didReceiveMetadataFor: ICCameraItem)](./cameradevice%28_,didreceivemetadatafor%29.md)
  Tells the client when the metadata requested for an item on a camera is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:shouldgetmetadataof:))*