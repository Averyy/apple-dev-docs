# thumbnail

**Framework**: ImageCaptureCore  
**Kind**: property

The item’s thumbnail.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var thumbnail: CGImage? { get }
```

#### Discussion

The value of this property is `nil` until you call [`requestThumbnail()`](iccameraitem/requestthumbnail().md).

## See Also

- [func requestThumbnail()](iccameraitem/requestthumbnail.md)
  Requests a thumbnail for the item.
- [var thumbnailIfAvailable: CGImage?](iccameraitem/thumbnailifavailable.md)
  The item’s thumbnail if it is readily available.
- [var largeThumbnailIfAvailable: CGImage?](iccameraitem/largethumbnailifavailable.md)
  A large thumbnail for the item if one is readily available.
- [func flushThumbnailCache()](iccameraitem/flushthumbnailcache.md)
  Deletes the item’s cached thumbnail.
- [struct ICCameraItemThumbnailOption](iccameraitemthumbnailoption.md)
  An option for the item’s thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/thumbnail)*