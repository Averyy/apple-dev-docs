# thumbnail

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) CGImageRef thumbnail;
```

#### Discussion

The value of this property is `nil` until you call [`requestThumbnail()`](./requestthumbnail%28%29.md).

## See Also

### Requesting Thumbnails
- [func requestThumbnail()](./requestthumbnail%28%29.md)
  Requests a thumbnail for the item.
- [var thumbnailIfAvailable: CGImage?](./thumbnailifavailable.md)
  The item’s thumbnail if it is readily available.
- [var largeThumbnailIfAvailable: CGImage?](./largethumbnailifavailable.md)
  A large thumbnail for the item if one is readily available.
- [func flushThumbnailCache()](./flushthumbnailcache%28%29.md)
  Deletes the item’s cached thumbnail.
- [struct ICCameraItemThumbnailOption](../iccameraitemthumbnailoption.md)
  An option for the item’s thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/thumbnail)*