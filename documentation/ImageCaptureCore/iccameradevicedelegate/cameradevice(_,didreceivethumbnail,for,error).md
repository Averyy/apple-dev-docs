# cameraDevice(_:didReceiveThumbnail:for:error:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Required**: Yes

Tells the client when the requested thumbnail is available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func cameraDevice(_ camera: ICCameraDevice, didReceiveThumbnail thumbnail: CGImage?, for item: ICCameraItem, error: (any Error)?)
```

## See Also

- [func cameraDevice(ICCameraDevice, didReceiveThumbnailFor: ICCameraItem)](iccameradevicedelegate/cameradevice(_:didreceivethumbnailfor:).md)
  Tells the client when the requested thumbnail is available.
- [func cameraDevice(ICCameraDevice, shouldGetThumbnailOf: ICCameraItem) -> Bool](iccameradevicedelegate/cameradevice(_:shouldgetthumbnailof:).md)
  Tells the client when the camera is about to execute queued requests for the thumbnail of a specific item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate/cameradevice(_:didreceivethumbnail:for:error:))*