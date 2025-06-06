# ICCameraItemThumbnailOption

**Framework**: ImageCaptureCore  
**Kind**: struct

An option for the item’s thumbnail.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct ICCameraItemThumbnailOption
```

## Topics

### Initializers
- [init(rawValue: String)](iccameraitemthumbnailoption/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func requestThumbnail()](iccameraitem/requestthumbnail.md)
  Requests a thumbnail for the item.
- [var thumbnail: CGImage?](iccameraitem/thumbnail.md)
  The item’s thumbnail.
- [var thumbnailIfAvailable: CGImage?](iccameraitem/thumbnailifavailable.md)
  The item’s thumbnail if it is readily available.
- [var largeThumbnailIfAvailable: CGImage?](iccameraitem/largethumbnailifavailable.md)
  A large thumbnail for the item if one is readily available.
- [func flushThumbnailCache()](iccameraitem/flushthumbnailcache.md)
  Deletes the item’s cached thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitemthumbnailoption)*