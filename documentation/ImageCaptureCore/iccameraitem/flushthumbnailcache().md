# flushThumbnailCache()

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Deletes the item’s cached thumbnail.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func flushThumbnailCache()
```

```objc
- (void) flushThumbnailCache;
```

## See Also

### Requesting Thumbnails
- [func requestThumbnail()](./requestthumbnail%28%29.md)
  Requests a thumbnail for the item.
- [var thumbnail: CGImage?](./thumbnail.md)
  The item’s thumbnail.
- [var thumbnailIfAvailable: CGImage?](./thumbnailifavailable.md)
  The item’s thumbnail if it is readily available.
- [var largeThumbnailIfAvailable: CGImage?](./largethumbnailifavailable.md)
  A large thumbnail for the item if one is readily available.
- [struct ICCameraItemThumbnailOption](../iccameraitemthumbnailoption.md)
  An option for the item’s thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/flushthumbnailcache())*