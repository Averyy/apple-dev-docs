# requestThumbnail()

**Framework**: ImageCaptureCore  
**Kind**: method

Requests a thumbnail for the item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func requestThumbnail()
```

#### Discussion

If a thumbnail is not readily available, accessing this property will send a message to the device requesting a thumbnail for the file. The delegate of the device will be notified via method [`cameraDevice(_:didReceiveThumbnail:for:error:)`](iccameradevicedelegate/cameradevice(_:didreceivethumbnail:for:error:).md), if this method is implemented by the delegate. Execution of the delegate callback will occur on the main thread.

## See Also

- [var thumbnail: CGImage?](iccameraitem/thumbnail.md)
  The item’s thumbnail.
- [var thumbnailIfAvailable: CGImage?](iccameraitem/thumbnailifavailable.md)
  The item’s thumbnail if it is readily available.
- [var largeThumbnailIfAvailable: CGImage?](iccameraitem/largethumbnailifavailable.md)
  A large thumbnail for the item if one is readily available.
- [func flushThumbnailCache()](iccameraitem/flushthumbnailcache.md)
  Deletes the item’s cached thumbnail.
- [struct ICCameraItemThumbnailOption](iccameraitemthumbnailoption.md)
  An option for the item’s thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/requestthumbnail())*