# userInfo

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

User-defined metadata, like a developer-specific identifier, for a media item.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var userInfo: [String : Any] { get }
```

```objc
@property (nonatomic, strong, readonly) NSDictionary<NSString *,id> * userInfo;
```

## See Also

### Identifying Media Items
- [var artworkImageURL: URL?](./artworkimageurl.md)
  The URL path to the artwork that accompanies the media item.
- [var itemDescription: String?](./itemdescription.md)
  The description for a media item.
- [var subtitle: String?](./subtitle.md)
  The subtitle for a media item.
- [var title: String?](./title.md)
  The title for a media item.
- [var type: TVMediaItem.MediaType?](./type.md)
  The type of media item.
- [TVMediaItem.MediaType](./mediatype.md)
  A value indicating whether the media is audio or video.
- [var url: URL?](./url.md)
  The URL path to the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/userinfo)*