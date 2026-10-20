# ICCameraDeviceDelegate

**Framework**: ImageCaptureCore  
**Kind**: protocol  
**Role**: Protocol

Methods for detecting cameras, getting metadata and thumbnails, handling access and capability changes, and performing other actions on connected cameras.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
protocol ICCameraDeviceDelegate : ICDeviceDelegate
```

```objc
@protocol ICCameraDeviceDelegate <ICDeviceDelegate>
```

## Topics

### Determining Device Readiness
- [func deviceDidBecomeReady(withCompleteContentCatalog: ICCameraDevice)](./iccameradevicedelegate/devicedidbecomeready%28withcompletecontentcatalog%29.md)
  Tells the client that the camera device is done enumerating its content and is ready to receive requests.
### Adding Objects
- [func cameraDevice(ICCameraDevice, didAdd: [ICCameraItem])](./iccameradevicedelegate/cameradevice%28_,didadd%29-8oukd.md)
  Tells the client when objects are added to the device.
- [func cameraDevice(ICCameraDevice, didAdd: ICCameraItem)](./iccameradevicedelegate/cameradevice%28_,didadd%29-9pnzo.md)
  Tells the client when an object is added to the device.
### Removing Objects
- [func cameraDevice(ICCameraDevice, didRemove: [ICCameraItem])](./iccameradevicedelegate/cameradevice%28_,didremove%29-4m5al.md)
  Tells the client when objects are removed from the device.
- [func cameraDevice(ICCameraDevice, didCompleteDeleteFilesWithError: (any Error)?)](./iccameradevicedelegate/cameradevice%28_,didcompletedeletefileswitherror%29.md)
  Tells the client when the camera completes a delete operation.
- [func cameraDevice(ICCameraDevice, didRemove: ICCameraItem)](./iccameradevicedelegate/cameradevice%28_,didremove%29-9rz34.md)
  Tells the client when an object is removed from the device.
### Renaming Objects
- [func cameraDevice(ICCameraDevice, didRenameItems: [ICCameraItem])](./iccameradevicedelegate/cameradevice%28_,didrenameitems%29.md)
  Tells the client when one or more objects are renamed on the device.
### Receiving Metadata
- [func cameraDevice(ICCameraDevice, didReceiveMetadata: [AnyHashable : Any]?, for: ICCameraItem, error: (any Error)?)](./iccameradevicedelegate/cameradevice%28_,didreceivemetadata,for,error%29.md)
  Tells the client when the metadata requested for an item on a camera is available.
- [func cameraDevice(ICCameraDevice, shouldGetMetadataOf: ICCameraItem) -> Bool](./iccameradevicedelegate/cameradevice%28_,shouldgetmetadataof%29.md)
  Tells the client when the camera is about to execute queued requests for the metadata of a specific item.
- [func cameraDevice(ICCameraDevice, didReceiveMetadataFor: ICCameraItem)](./iccameradevicedelegate/cameradevice%28_,didreceivemetadatafor%29.md)
  Tells the client when the metadata requested for an item on a camera is available.
### Receiving Thumbnails
- [func cameraDevice(ICCameraDevice, didReceiveThumbnail: CGImage?, for: ICCameraItem, error: (any Error)?)](./iccameradevicedelegate/cameradevice%28_,didreceivethumbnail,for,error%29.md)
  Tells the client when the requested thumbnail is available.
- [func cameraDevice(ICCameraDevice, didReceiveThumbnailFor: ICCameraItem)](./iccameradevicedelegate/cameradevice%28_,didreceivethumbnailfor%29.md)
  Tells the client when the requested thumbnail is available.
- [func cameraDevice(ICCameraDevice, shouldGetThumbnailOf: ICCameraItem) -> Bool](./iccameradevicedelegate/cameradevice%28_,shouldgetthumbnailof%29.md)
  Tells the client when the camera is about to execute queued requests for the thumbnail of a specific item.
### Responding to Capability Changes
- [func cameraDeviceDidChangeCapability(ICCameraDevice)](./iccameradevicedelegate/cameradevicedidchangecapability%28_%29.md)
  Tells the client when a capability of a camera changes.
### Responding to Access Restrictions
- [func cameraDeviceDidEnableAccessRestriction(ICDevice)](./iccameradevicedelegate/cameradevicedidenableaccessrestriction%28_%29.md)
  Tells the client when an Apple device has been locked, and media is unavailable until the restriction has been removed.
- [func cameraDeviceDidRemoveAccessRestriction(ICDevice)](./iccameradevicedelegate/cameradevicedidremoveaccessrestriction%28_%29.md)
  Tells the client when an Apple device has been unlocked, paired to the host, and media is available.
### Responding to PTP Events
- [func cameraDevice(ICCameraDevice, didReceivePTPEvent: Data)](./iccameradevicedelegate/cameradevice%28_,didreceiveptpevent%29.md)
  Tells the client about a PTP event.

## Relationships

### Inherits From
- [ICDeviceDelegate](./icdevicedelegate.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Cameras
- [class ICCameraDevice](./iccameradevice.md)
  An object that represents a camera.
- [class ICCameraItem](./iccameraitem.md)
  An abstract class that represents a camera item.
- [class ICCameraFile](./iccamerafile.md)
  An object that represents a file on a camera.
- [class ICCameraFolder](./iccamerafolder.md)
  An object that represents a folder on a camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate)*