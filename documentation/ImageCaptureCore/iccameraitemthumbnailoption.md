# ICCameraItemThumbnailOption

**Framework**: ImageCaptureCore  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * ICCameraItemThumbnailOption;
```

## Topics

### Initializers
- [init(rawValue: String)](./iccameraitemthumbnailoption/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Requesting Thumbnails
- [func requestThumbnail()](./iccameraitem/requestthumbnail%28%29.md)
  Requests a thumbnail for the item.
- [var thumbnail: CGImage?](./iccameraitem/thumbnail.md)
  The item’s thumbnail.
- [var thumbnailIfAvailable: CGImage?](./iccameraitem/thumbnailifavailable.md)
  The item’s thumbnail if it is readily available.
- [var largeThumbnailIfAvailable: CGImage?](./iccameraitem/largethumbnailifavailable.md)
  A large thumbnail for the item if one is readily available.
- [func flushThumbnailCache()](./iccameraitem/flushthumbnailcache%28%29.md)
  Deletes the item’s cached thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitemthumbnailoption)*