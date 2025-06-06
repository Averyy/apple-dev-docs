# cameraDevice(_:didReceiveThumbnailFor:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the client when the requested thumbnail is available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
optional func cameraDevice(_ camera: ICCameraDevice, didReceiveThumbnailFor item: ICCameraItem)
```

#### Discussion

This method is deprecated. Use [`cameraDevice(_:didReceiveThumbnail:for:error:)`](iccameradevicedelegate/cameradevice(_:didreceivethumbnail:for:error:).md) instead.

## See Also

- [func cameraDevice(ICCameraDevice, didReceiveThumbnail: CGImage?, for: ICCameraItem, error: (any Error)?)](iccameradevicedelegate/cameradevice(_:didreceivethumbnail:for:error:).md)
  Tells the client when the requested thumbnail is available.
- [func cameraDevice(ICCameraDevice, shouldGetThumbnailOf: ICCameraItem) -> Bool](iccameradevicedelegate/cameradevice(_:shouldgetthumbnailof:).md)
  Tells the client when the camera is about to execute queued requests for the thumbnail of a specific item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didreceivethumbnailfor:))*