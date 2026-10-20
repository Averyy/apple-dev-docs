# TVMediaItem.MediaType

**Framework**: TVMLKit  
**Kind**: struct  
**Role**: Structure

A value indicating whether the media is audio or video.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
struct MediaType
```

```c
typedef NSString * TVMediaItemType;
```

## Topics

### Media Types
- [static let audio: TVMediaItem.MediaType](./mediatype/audio.md)
  The media item is audio only.
- [static let video: TVMediaItem.MediaType](./mediatype/video.md)
  The media item incorporates video.
### Initializers
- [init(String)](./mediatype/init%28_%29.md)
- [init(rawValue: String)](./mediatype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var url: URL?](./url.md)
  The URL path to the media item.
- [var userInfo: [String : Any]](./userinfo.md)
  User-defined metadata, like a developer-specific identifier, for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/mediatype)*