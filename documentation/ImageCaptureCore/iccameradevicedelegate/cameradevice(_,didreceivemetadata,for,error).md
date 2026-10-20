# cameraDevice(_:didReceiveMetadata:for:error:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the client when the metadata requested for an item on a camera is available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func cameraDevice(_ camera: ICCameraDevice, didReceiveMetadata metadata: [AnyHashable : Any]?, for item: ICCameraItem, error: (any Error)?)
```

```objc
- (void) cameraDevice:(ICCameraDevice *) camera didReceiveMetadata:(NSDictionary *) metadata forItem:(ICCameraItem *) item error:(NSError *) error;
```

## See Also

### Receiving Metadata
- [func cameraDevice(ICCameraDevice, shouldGetMetadataOf: ICCameraItem) -> Bool](./cameradevice%28_,shouldgetmetadataof%29.md)
  Tells the client when the camera is about to execute queued requests for the metadata of a specific item.
- [func cameraDevice(ICCameraDevice, didReceiveMetadataFor: ICCameraItem)](./cameradevice%28_,didreceivemetadatafor%29.md)
  Tells the client when the metadata requested for an item on a camera is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didreceivemetadata:for:error:))*