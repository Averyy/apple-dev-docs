# cameraDevice(_:didReceiveThumbnailFor:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the client when the requested thumbnail is available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.15
- visionOS 1.0+

## Declaration

```swift
optional func cameraDevice(_ camera: ICCameraDevice, didReceiveThumbnailFor item: ICCameraItem)
```

```objc
- (void) cameraDevice:(ICCameraDevice *) camera didReceiveThumbnailForItem:(ICCameraItem *) item;
```

#### Discussion

This method is deprecated. Use [`cameraDevice(_:didReceiveThumbnail:for:error:)`](./cameradevice%28_,didreceivethumbnail,for,error%29.md) instead.

## See Also

### Receiving Thumbnails
- [func cameraDevice(ICCameraDevice, didReceiveThumbnail: CGImage?, for: ICCameraItem, error: (any Error)?)](./cameradevice%28_,didreceivethumbnail,for,error%29.md)
  Tells the client when the requested thumbnail is available.
- [func cameraDevice(ICCameraDevice, shouldGetThumbnailOf: ICCameraItem) -> Bool](./cameradevice%28_,shouldgetthumbnailof%29.md)
  Tells the client when the camera is about to execute queued requests for the thumbnail of a specific item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didreceivethumbnailfor:))*