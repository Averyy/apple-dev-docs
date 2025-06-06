# cameraDevice(_:shouldGetThumbnailOf:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the client when the camera is about to execute queued requests for the thumbnail of a specific item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetThumbnailOf item: ICCameraItem) -> Bool
```

#### Discussion

If the request is no longer needed—for example, if the item is no longer displayed on the screen—the client can cancel sending a request to the camera, speeding up the execution queue.

## See Also

- [func cameraDevice(ICCameraDevice, didReceiveThumbnail: CGImage?, for: ICCameraItem, error: (any Error)?)](iccameradevicedelegate/cameradevice(_:didreceivethumbnail:for:error:).md)
  Tells the client when the requested thumbnail is available.
- [func cameraDevice(ICCameraDevice, didReceiveThumbnailFor: ICCameraItem)](iccameradevicedelegate/cameradevice(_:didreceivethumbnailfor:).md)
  Tells the client when the requested thumbnail is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:shouldgetthumbnailof:))*