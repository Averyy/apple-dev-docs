# largeThumbnailIfAvailable

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

A large thumbnail for the item if one is readily available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.15
- visionOS 1.0+

## Declaration

```swift
var largeThumbnailIfAvailable: CGImage? { get }
```

```objc
@property (readonly, nullable) CGImageRef largeThumbnailIfAvailable;
```

#### Discussion

If a large thumbnail is not readily available, accessing this property requests it from the device.

When the thumbnail is received, [`cameraDevice(_:didReceiveThumbnailFor:)`](../iccameradevicedelegate/cameradevice%28_,didreceivethumbnailfor%29.md) is called on the the device’s [`delegate`](../icdevice/delegate.md).

Execution of the delegate callback occurs on the main thread.

## See Also

### Requesting Thumbnails
- [func requestThumbnail()](./requestthumbnail%28%29.md)
  Requests a thumbnail for the item.
- [var thumbnail: CGImage?](./thumbnail.md)
  The item’s thumbnail.
- [var thumbnailIfAvailable: CGImage?](./thumbnailifavailable.md)
  The item’s thumbnail if it is readily available.
- [func flushThumbnailCache()](./flushthumbnailcache%28%29.md)
  Deletes the item’s cached thumbnail.
- [struct ICCameraItemThumbnailOption](../iccameraitemthumbnailoption.md)
  An option for the item’s thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/largethumbnailifavailable)*