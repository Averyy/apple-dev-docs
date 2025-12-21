# RCSService.Business.Card.Media

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure containing information about media in a card.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct Media
```

## Topics

### Accessing card media properties
- [let url: URL](rcsservice/business/card/media/url.md)
  URL of media.
- [let contentType: UTType?](rcsservice/business/card/media/contenttype.md)
  Content type of media.
- [let fileSize: Measurement<UnitInformationStorage>](rcsservice/business/card/media/filesize.md)
  File size of media.
- [let thumbnailURL: URL?](rcsservice/business/card/media/thumbnailurl.md)
  URL of thumbnail.
- [let thumbnailContentType: UTType?](rcsservice/business/card/media/thumbnailcontenttype.md)
  Content type of thumbnail.
- [let thumbnailFileSize: Measurement<UnitInformationStorage>?](rcsservice/business/card/media/thumbnailfilesize.md)
  File size of thumbnail.
- [let displayHeight: RCSService.Business.Card.Media.Height](rcsservice/business/card/media/displayheight.md)
  The display height for media.
- [RCSService.Business.Card.Media.Height](rcsservice/business/card/media/height.md)
  Enumeration indicating the height of the media.
- [let description: String?](rcsservice/business/card/media/description.md)
  Description of media.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [RCSService.Business.Card.Width](rcsservice/business/card/width.md)
  Enumeration specifying the width of a card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/media)*